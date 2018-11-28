#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <vector>

using namespace std;

void SplitString(char * input, char * & output)
{
	if ((*input) == '\0')
	{
		output = input;
		return;
	}
	if ((*input) != '(')
	{
		output = input + 1;
		return;
	}
	else
	{
		output = input + 1;
		while((*output) != ')') ++output;
		++output;
		return;
	}
}


void GetAllAvailableLetters(const string & InputString, vector<vector<char> *> & _buffer)
{
	char * _start = const_cast<char *>(InputString.c_str());
	char * _next = const_cast<char *>(InputString.c_str());
	while ( (*_next)!='\0' )
	{
		SplitString( _start, _next );
		vector<char> *_tmpList = new vector<char>;
		// Get a single letter.
		if ((*_start) == '(') ++_start;
		while(_start != _next)
		{
			if ((*_start) != ')')
				_tmpList->push_back((*_start));
			++_start;
		}
		_buffer.push_back(_tmpList);
	}
}

bool IsMatch(vector<vector<char> *> & _buffer, const string & InputString)
{
	for (int i = 0; i < (int)InputString.size(); ++i)
	{
		vector<char> & _tmp = *_buffer[i];
		if (find(_tmp.begin(), _tmp.end(), InputString[i]) == _tmp.end()) return false;
	}
	return true;
}

int MatchHowMany(string & RegExp, list<string *> & WordList)
{
	vector<vector<char> *> _buffer;
	GetAllAvailableLetters(RegExp, _buffer);
	int nRtn = 0;
	for (list<string *>::iterator lstIt = WordList.begin();
		lstIt != WordList.end(); ++lstIt)
	{
		if (IsMatch(_buffer, *(*lstIt))) ++nRtn;
	}
	//for (int i = 0; i < (int)_buffer.size(); ++i, delete _buffer[i]);
	for (vector<vector<char> *>::iterator vIt = _buffer.begin(); 
		vIt != _buffer.end(); delete (*vIt), ++vIt);
	return nRtn;
}

int main(int argc, char * argv[])
{	
	if (argc != 2) return -1;
	ifstream inputFile(argv[1], ios_base::in);
	int L = 0, D = 0, N = 0;
	inputFile >> L >> D >> N;

	list<string *> _WordList;
	list<string *> _CaseList;

	for (int i = 0; i < D; ++i)
	{
		string * _word = new string;
		inputFile >> (*_word);
		_WordList.push_back(_word);
	}

	for (int i = 0; i < N; ++i)
	{
		string * _case = new string;
		inputFile >> (*_case);
		_CaseList.push_back(_case);
	}

	list<string *>::iterator lstIt = _CaseList.begin();
	ofstream outFile("out.txt", ios_base::out);
	for (int i = 0; i < N; ++i, ++lstIt)
	{
		int rtn = MatchHowMany(*(*lstIt), _WordList);
		outFile << "Case #" << i + 1 << ":\t" << rtn << endl;
	}

	// Release the resource.
	for (list<string *>::iterator lstIt = _WordList.begin(); lstIt != _WordList.end(); delete *lstIt, ++lstIt);
	for (list<string *>::iterator lstIt = _CaseList.begin(); lstIt != _CaseList.end(); delete *lstIt, ++lstIt);

	return 0;
}