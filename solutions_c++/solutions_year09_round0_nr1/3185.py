#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <fstream>
#include <regex>

using namespace std;

int findWord(string word, vector<string>& input)
{
	for(int i =0; i < word.size(); i++)
	{
		if((input[i]).find(word[i]) == string::npos)
		{
			return (0);
		}
	}

	return (1);
}

string getNextChars(string::iterator &si1, string::iterator si2)
{
	string chs;

	if (si1 == si2)
		return (chs);

	if (*si1 != '(')
	{
		chs = *si1++;
		return (chs);
	}
		
	while(*(++si1) != ')')
		chs += *si1;

	si1++;
	
	return (chs);
}

int main (void)
{
	int nLen =0, nDic =0, nCases =0;
	vector<string> d;
	fstream infile("alien.in");

	infile >> nLen >> nDic >> nCases;
	
	for(int i =0; i < nDic; i++)
	{
	    string word;
		infile >> word;
		d.insert(d.end(), word);
	}

	for(int i =0; i < nCases; i++)
	{
		int wc = 0;
		string phrase, chs;
		infile >> phrase;

	    vector<string> input;

		string::iterator si = phrase.begin();
		while ((chs = getNextChars(si, phrase.end())) != "")
		{
			input.insert(input.end(), chs);
		}

		for(int j =0; j < d.size(); j++)
		{
			if (findWord(d[j], input) == 1) 
			{
				wc++;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << wc << endl;

		//for(vector<string>::iterator vi =input.begin(); vi != input.end(); vi++)
		//	cout << *vi << endl;	
	}

	return (0);
}
