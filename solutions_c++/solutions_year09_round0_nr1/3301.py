#include <iostream>
#include <set>
#include <fstream>
#include <string>
#include <vector>
#define CHAR_START 97
using namespace std;

// Contains one letter or ( ) collection of letters.


struct language {
	set<string> dict[26];
};

struct langData {
	int L, D, N;
};

void read_language(language& language, char* filename);
int get_paren_length(string thisPoss, int parenLocation);
bool containsPrefix(language& lang, string prefix);
int get_num_possibilities(language& lang, string thisPoss, int length);

int main(int argc, char* argv[])
{
	language lang;	
	if(argc == 2) 
		read_language(lang, argv[1]);
	else return -1;
	return 0;
}

void read_language(language& lang, char* filename)
{
	langData ld;
	ifstream input(filename);
	input >> ld.L;
	input >> ld.D;
	input >> ld.N;
	
	for (int i = 0; i < ld.D; ++i)
	{
		string thisWord;
		input >> thisWord;
		lang.dict[thisWord[0] - CHAR_START].insert(thisWord);
	}
	ofstream out("output.txt");
	for (int i = 0; i < ld.N; ++i)
	{
		string thisPoss;
		input >> thisPoss;
		int numPoss = get_num_possibilities(lang, thisPoss, ld.L);
		out << "Case #" << i + 1 << ": " << numPoss << endl;
	}
}

int get_num_possibilities(language& lang, string thisPoss, int length)
{
	int numPossibilities = 0;
//	cout << "Current: " << thisPoss << endl;
	if (thisPoss.length() == length) 
	{
		if (lang.dict[thisPoss[0] - CHAR_START].count(thisPoss))
			numPossibilities++;
	} 
	else 
	{
		int parenLoc = thisPoss.find('(');
		string preParen = thisPoss.substr(0, parenLoc);
	//	cout << "thisPrefix: " << preParen << endl;
		if (containsPrefix(lang, preParen))
		{
			int parenLength = get_paren_length(thisPoss, parenLoc);
		//	cout << parenLength << endl;
			for (int i = 0; i < parenLength; ++i)
			{
				char thisChar = thisPoss[i + parenLoc + 1];
				string remaining = thisPoss.substr(parenLength + 2 + parenLoc);
				string newPoss = preParen + thisChar + remaining;
			//	cout << "New: " << newPoss << endl; 
				numPossibilities += get_num_possibilities(lang, newPoss, length);
			}
		}
	}
	return numPossibilities;
}

bool containsPrefix(language& lang, string prefix) 
{	
	int size = prefix.size();
	if(size == 0) return true;
	set<string> location = lang.dict[prefix[0] - CHAR_START];
	for (set<string>::iterator itr = location.begin(); itr != location.end(); ++itr)
	{
		string word = itr->substr(0, size);
		if (word.compare(prefix) == 0) {
			return true;
		}
	}
	return false;
}

int get_paren_length(string thisPoss, int parenLocation)
{
	return thisPoss.find(')', parenLocation + 1) - parenLocation - 1;
}