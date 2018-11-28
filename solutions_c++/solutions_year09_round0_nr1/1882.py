
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <fstream>
#include <assert.h>

using namespace std;
int L, N, D;

vector<string> g_knowedWord;
vector<int> g_matchNum;


vector<string> ParsePatternWord(const string &word)
{
	vector<string> patternWords;
	bool bPattern = false;
	string buffer;
	for (unsigned int i=0; i<word.size(); i++)
	{
		if (word[i] == '(')
		{
			bPattern = true;
		}
		else if (word[i] == ')')
		{
			bPattern = false;
			patternWords.push_back(buffer);
			buffer.resize(0);
		}
		else{
			if (bPattern)
			{
				buffer+=word[i];
			}
			else
			{
				string letterStr(1, word[i]);
				patternWords.push_back(letterStr);
				buffer.resize(0);
			}
		}
	}
	return patternWords;
}

list<string*> g_matchString;

void InitMatchString()
{
	g_matchString.clear();
	for (int i=0; i<g_knowedWord.size(); i++)
	{
		g_matchString.push_back(&(g_knowedWord[i]));
	}
}


void FilterLetter(char letter, int index)
{
	list<string*>::iterator it;
	string *str = 0;
	vector<string*> notMatchstring;
	for (it=g_matchString.begin(); it != g_matchString.end(); it++)
	{
		str  = *it;
		if (str->at(index) != letter)
		{
			notMatchstring.push_back(str);
		}
	}
	for (int i=0; i<notMatchstring.size(); i++)
	{
		g_matchString.remove(notMatchstring[i]);
	}
}

void FilterMatchNumLetter(const string &letters, int index)
{
	string *str = 0;
	list<string*>::iterator it;
	vector<string*> notMatchstring;
	for (it=g_matchString.begin(); it != g_matchString.end(); it++)
	{
		str  = *it;
		if (letters.find(str->at(index)) == string::npos)
		{
			notMatchstring.push_back(str);
		}
	}
	for (int i=0; i<notMatchstring.size(); i++)
	{
		g_matchString.remove(notMatchstring[i]);
	}
}


int FindMatchNum(const vector<string> &patternWord)
{
	for (int i=0; i<patternWord.size(); i++)
	{
		FilterMatchNumLetter(patternWord[i], i);
	}
	return g_matchString.size();
}


ofstream g_outFile;
void PrintOutput()
{
	for (int i=0; i<g_matchNum.size(); i++)
	{
		g_outFile << "Case #" << i+1 << ": " << g_matchNum[i] << endl;
	}
}


ifstream g_file;
void ParseTestCase(vector<string> &testCase)
{
	
	for (int caseNum = 0; caseNum < N; caseNum++)
	{
		string caseWord;
		g_file >> caseWord; 
		testCase.push_back(caseWord);
	}
}

void ParseKnowedWord()
{
	for (int strNum=0; strNum < D; strNum++)
	{
		string knownWord;
		g_file >> knownWord;
		g_knowedWord.push_back(knownWord);
	}
}

int main(int argc, char* argv[])
{
	
	const char *fileName = "A-large.in";
	g_file.open(fileName);
	g_outFile.open("A-large.out");

	assert(g_file.is_open());
	g_file >> L >> D >> N;

	vector<string> testCase;
	int i=0;
	vector<string> patternWord;
	int num =0;

	ParseKnowedWord();
	ParseTestCase(testCase);
	for (i=0; i<testCase.size(); i++)
	{
		InitMatchString();
		patternWord = ParsePatternWord(testCase[i]);
		num = FindMatchNum(patternWord);
		g_matchNum.push_back(num);
	}

	PrintOutput();
	return 0;
}

