// p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>


using namespace std;

class Pattern{
private:
enum state {NORMAL,INBRACKET};
set<char> patn[16];
public:
		Pattern(string s)
		{
			
			state st=NORMAL;
			int index = -1;
			for (int i = 0;i<s.length();++i)
			{
				char a = s[i];
				if (st == NORMAL) ++index;
				if (a == '(') st = INBRACKET;
				else if (a == ')') st = NORMAL;
				else patn[index].insert(a);
			}

		}
		bool matches (string s)
		{
			for (int i = 0;i<s.length();++i)
			{
				char a = s[i];
				if (patn[i].find(a) == patn[i].end()) return false;
			}
			return true;
		}

};


int main(int argc, char* argv[])
{
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	
	char junk[30];
	int tokLength;
	int numWords;
	int numTests;
	vector<string> words;
	vector<string> patterns;
	fin >> tokLength >> numWords >> numTests;
	fin.getline(junk,30);
	for (int i=0;i<numWords;++i)
	{
		char word[256];
		fin.getline(word,256);
		words.push_back(word);
	}
	for (int j=0;j< numTests;++j)
	{
		char pattern[2000];
		fin.getline(pattern,2000);
		patterns.push_back(pattern);
	}
	for (int k=0;k< numTests;++k)
	{
		Pattern currPattern(patterns[k]);
		int numMatches = 0;
		for (int l=0;l<numWords;++l)
		{
			if (currPattern.matches(words[l])) ++numMatches;
		}
		
		fprintf(f2,"Case #%d: %d\n",k+1,numMatches);

	}

	return 0;
  
}


