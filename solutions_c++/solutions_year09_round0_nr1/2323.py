#include <fstream>
#include <string>
#include <vector>

using namespace std;

//function prototypes
int wordsMatchingPattern(string*, string &, int);
bool isInToken(char, string &, int);
int findToken(string &, int);

int main()
{
	ifstream infile;
	infile.open("testdata.txt");

	int wordLength;
	int numWords;
	int numTestCases;
	string* alienWords;
	string* patterns;

	infile>>wordLength>>numWords>>numTestCases;
	alienWords = new string[numWords];

	for(int i = 0; i < numWords; i++)
		infile>>alienWords[i];

	patterns = new string[numTestCases];

	for(int i = 0; i < numTestCases; i++)
		infile>>patterns[i];

	infile.close();
	ofstream outfile;
	outfile.open("output.txt");

	for(int i = 0; i < numTestCases; i++)
	{
		outfile<<"Case #"<<i + 1<<": ";
		outfile<<wordsMatchingPattern(alienWords, patterns[i], numWords);
		outfile<<endl;
	}

	return 0;
}

int wordsMatchingPattern(string* theWords, string & pattern, int num)
{
	int matches = 0;

	//for each word, see if it can be made from the pattern
	//if it can, matches++
	for(int i = 0; i < num; i++)
	{
		//for each letter of a word, see if it can be found in that token
		for(int j = 0; j < theWords[i].size(); j++)
		{
			//if the jth letter of the word isn't in the jth token of the pattern, no dice
			if(!isInToken(theWords[i][j], pattern, j))
				break;

			//if we've made it this far, 
			if(j == theWords[i].size() - 1)
				matches++;
		}
	}

	return matches;
}

bool isInToken(char letter, string & pattern, int tokenNum)
{
	//go to correct token number
	//findToken returns index of first elem in token tokenNum
	int position = findToken(pattern, tokenNum);

	if(pattern[position] == '(')
	{
		while(pattern[position] != ')')
		{
			if(pattern[position] == letter)
				return true;
			position++;
		}
		return false;
	}

	return (pattern[position] == letter);
}

//return index of first letter in token tokenNum
//tokens are numbered starting from 0
int findToken(string & pattern, int tokenNum)
{
	bool insideParen = false;
	int currentToken = -1;
	int position = 0;

	while(currentToken != tokenNum)
	{
		if(pattern[position] == '(')
		{
			currentToken++;
			insideParen = true;
		}

		else if(pattern[position] == ')')
			insideParen = false;

		else if(!insideParen)
			currentToken++;

		position++;
	}

	return position - 1;
}