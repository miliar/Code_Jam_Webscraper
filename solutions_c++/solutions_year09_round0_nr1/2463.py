#include<fstream>
#include<string>
#include<vector>

using namespace std;

class WordTable
{
private:
	vector<string> _wordList;
public:
	WordTable(vector<string> wordList);
	bool find(string word);
	bool findSubStr(string word);
};

class Matcher
{
private:
	WordTable* _wordTable;
public:
	Matcher(WordTable* wordTable);
	int getMatchNum(string pattern);
};

void AlienLanguage(ifstream& inputFile, ofstream& outputFile);

vector<string> GenPossibleWords(string pattern);