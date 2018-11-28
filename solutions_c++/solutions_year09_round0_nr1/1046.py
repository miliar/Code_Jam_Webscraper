/* ****************************************
	c.cpp - Greg Tourville - September 2nd - Google Code Jam - Problem C
*/


#include <iostream>
#include <fstream>
#include <assert.h>

const int MAX_WORDS = 5000;
const int MAX_LETTERS = 16;
const int MAX_LINE = 3000;


class DictionaryNode
{
public:
	DictionaryNode()
	{
		for (int i = 0; i < 26; i++)
			nodes[i] = NULL;
	}

	~DictionaryNode()
	{
		for (int i = 0; i < 26; i++)
			if (nodes[i])
				delete nodes[i];
	}

	void AddWord(const char* word)
	{
		if (word[0] != '\0')
		{
			int n = word[0] - 'a';
			if (!nodes[n])
				nodes[n] = new DictionaryNode();
			nodes[n]->AddWord(&word[1]);
		}
	}

	bool CheckWord(const char* word)
	{
		if (word[0] == '\0')
			return true;
		int n = word[0] - 'a';
		if (nodes[n])
			return nodes[n]->CheckWord(&word[1]);
		return false;
	}

	DictionaryNode* GetNode(char c)
	{
		c -= 'a';
		return nodes[c];
	}

private:
	DictionaryNode*	nodes[26];
};



int CheckWords(const char* word, DictionaryNode* d)
{
	if (word[0] == '\0')
		return 1;

	int count = 0;

	DictionaryNode* next;
	if (word[0] == '(')
	{
		int i = 1;
		while (word[i] != ')')
			i++;
		for (int j = 1; j < i; j++)
		{
			next = d->GetNode(word[j]);
			if (next)
				count += CheckWords(&word[i+1], next);
		}
	} else {
		next = d->GetNode(word[0]);
		if (next)
			count += CheckWords(&word[1], next);
	}

	return count;
}




// ****************************************************************************

int main(int argc, const char* argv[])	// Arguments to executed program should be 1) input file and 2) output file
{
	assert(argc == 3);

	std::ofstream output(argv[2]);
	std::ifstream input(argv[1], std::ifstream::in);

	assert(output.good());
	assert(input.good());
		

	int letters;
	int words;
	input >> letters;
	input >> words;

	// Process all cases
	int cases;
	input >> cases;

	input.ignore(1, '\n');

	DictionaryNode* root = new DictionaryNode;

	for (int j = 0; j < words; j++)
	{
		char word[MAX_LETTERS];
		input.getline(word, MAX_LETTERS, '\n');
		root->AddWord(word);
	}

	for (int i = 1; i <= cases; i++)
	{
		char testWord[MAX_LINE];
		input.getline(testWord, MAX_LINE, '\n');

		int count = CheckWords(testWord, root);
		
		// compute and output
		
		output << "Case #" << i << ": " << count << std::endl;
	}

	delete root;

	// Clean up
	input.close();
	output.close();

	return 0;
}
