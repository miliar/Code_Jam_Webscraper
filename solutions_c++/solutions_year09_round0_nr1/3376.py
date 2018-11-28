/*
* Murat Ergun, 2009
*/

#include <iostream>
#include <fstream>
#include <string>
#include "Dictionary.h"
using namespace std;



void findWords (string prefix, string suffix, Dictionary &dictionary, int &count)
{
	if (suffix.size() == 0) // if no more letters left to process, look up dictionary
	{
		if( dictionary.findWord(prefix) )
		{
			count++;
		}
	}
	else if (suffix[0] == '(') // if corresponding char is a start paranthesis, process the chars inside paranthesis
	{
		int closeParan = suffix.find(')');
		for (int i = 1; i < closeParan; i++) // for each letter up until close paranthesis
		{
			if (dictionary.findPrefix(prefix + suffix[i]))
			{
				findWords ( prefix + suffix[i], suffix.substr(closeParan+1, suffix.size()), dictionary, count);
			}
		}
	}
	else
	{
		if (dictionary.findPrefix(prefix + suffix[0]))
		{
			findWords (prefix + suffix[0], suffix.substr(1, suffix.size()), dictionary, count);
		}
	}
}

int main()
{
	string fname, word;
	int len, dict, cases;
	//cout << "Please enter input file name: ";
	//cin >> fname;
	//ifstream input(fname.c_str());
	cin >> len >> dict >> cases;
	Dictionary dictionary(26);
	for (int i=0; i < dict; i++)
	{
		cin >> word;
		dictionary.insertWord(word);
	}
	for (int j=0; j < cases; j++)
	{
		cin >> word;
		int count = 0;
		findWords("", word, dictionary, count);
		cout << "Case #" << j+1 << ": " << count << endl;
	}
	return 0;
}