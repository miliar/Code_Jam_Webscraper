// Google Code Jam - Qualification Round 2009
// A. Alien Language

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct node {
	node* alpha[26];
};


void OpenFiles(ifstream &in, ofstream &out) {
	in.open("A-large.in");
	out.open("result.txt");
	
	if(in.fail() || out.fail())
		cout << "Failed to open input or output file." << endl;
}

vector<string> Tokenize(string line, int wordLength) {
	int pos = 0;
	vector<string> tokenizedWord;
	
	for (int i = 0; i < wordLength; ++i) {
		string token;
		if (line[pos] == '(') {
			++pos;
			token = "";
			while (line[pos] != ')') {
				token += line[pos];
				++pos;
			}
		} else {
			token = line[pos];
		}
		++pos;
		tokenizedWord.push_back(token);
	}
	return tokenizedWord;
}

bool inDictionary(string word, node* dictionary) {
	node *traverse = dictionary;
	int wordSize = word.size();
	for (int i = 0; i < wordSize; ++i) {
		traverse = traverse->alpha[word[i] - 97];
		if (traverse == NULL) return false;
	}
	return true;
}

void ProcessTestWordRec(vector<string> &word, int pos, string wordAttempt, node* dictionary, int &count) {
	if (!inDictionary(wordAttempt, dictionary)) return; // for efficiency
		
	if (pos == word.size()) {
		if (inDictionary(wordAttempt, dictionary)) ++count;
	} else {
		string letters = word[pos];
		int lettersSize = letters.size();
		for (int i = 0; i < lettersSize; ++i) {
			ProcessTestWordRec(word, pos+1, wordAttempt + letters[i], dictionary, count);
		}
	}
}

void ProcessTestWord(vector<string> &word, node* dictionary, int caseNumber, ofstream &out) {
	int count = 0;
	ProcessTestWordRec(word, 0, "", dictionary, count);
	out << "Case #" << caseNumber << ": " << count << endl;
}

void nullAlphaVector(node *theNode) {
	for (int i = 0; i < 26; ++i) {
		theNode->alpha[i] = NULL;
	}
}

int main (int argc, char * const argv[]) {
	ifstream in;
	ofstream out;
	OpenFiles(in, out);
	
	// Get starting parameters
	int wordLength, dictionarySize, numTestCases;
	in >> wordLength;
	in.get();
	in >> dictionarySize; 
	in.get();
	in >> numTestCases;
	in.get();
	    
	// fill dictionary (tree)
	node *dictionary = new node;
	nullAlphaVector(dictionary);
	
	for (int i = 0; i < dictionarySize; ++i) {
		string line;
		getline(in, line);
		
		node *traverse = dictionary;
		for (int i = 0; i < wordLength; ++i) {
			if (traverse->alpha[line[i] - 97] == NULL) {
				node *newNode = new node;
				nullAlphaVector(newNode);
				traverse->alpha[line[i] - 97] = newNode;
				traverse = newNode;
			} else {
				traverse = traverse->alpha[line[i] - 97];
			}
		}
	}
	
	// fill test cases vector
	vector<vector<string> > testCases;
	for (int i = 0; i < numTestCases; ++i) {
		string line;
		getline(in, line);
		vector<string> tokenizedVector = Tokenize(line, wordLength);
		testCases.push_back(tokenizedVector);
	}
	
	int caseNumber = 1;
	for (vector<vector<string> >::iterator itr = testCases.begin(); itr != testCases.end(); ++itr) {
		ProcessTestWord(*itr, dictionary, caseNumber++, out);
	}
	
	in.close();
	out.close();
	return 0;
}
