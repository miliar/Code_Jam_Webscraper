// codeJam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

void removeSpaces (std::string & input)
{
	std::string::iterator end_pos = std::remove(input.begin(), input.end(), ' ');
	input.erase(end_pos, input.end());
}

void addToTranslate(std::map <char, char> &tranChart, int size, char* key, char* value)
{
	for(int i = 0; i < size; i++)
	{
		tranChart.insert( std::pair<char, char>( key[i], value[i] ) );
	}
}

void findSpaces(std::string input, int* spaces)
{
	int spaceIdx = 0;

	for(int idx = 0; idx < input.size()-1; idx++)
	{
		if (input[idx] == ' ') 
		{
			spaces[spaceIdx++] = idx;
		}
	}
}

void addSpaces(std::string & input, int* spaces)
{
	int i = 0;
	int grouthVector = 0;
	while(spaces[i] >0 )
	{
		input.insert(input.begin() + spaces[i],' ');
		i++;
		grouthVector++;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	//std::map <int english, int googlense> tranChart;
	std::map <char, char> tranChart;

	char eAlphabet [] = 
	{'a','b','c','d','e','f','g','h','i','j','k','l',
	'm','n','o','p','q','r','s','t','u','v','w','x','y','z'};

	char googlensAlphabet [26];
	
	std::string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	std::string a1 ="our language is impossible to understand";

	std::string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	std::string b1 ="there are twenty six factorial possibilities";

	std::string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	std::string c1 ="so it is okay if you want to just give up";

	std::string d = "zq";
	std::string d1 ="qz";

	removeSpaces(a);
	removeSpaces(a1);
	removeSpaces(b);
	removeSpaces(b1);
	removeSpaces(c);
	removeSpaces(c1);

	char *_a = (char*)a.c_str();
	char *_a1 = (char*)a1.c_str();

	char *_b = (char*)b.c_str();
	char *_b1 = (char*)b1.c_str();

	char *_c = (char*)c.c_str();
	char *_c1 = (char*)c1.c_str();
	
	char *_d = (char*)d.c_str();
	char *_d1 = (char*)d1.c_str();

	addToTranslate(tranChart, a.size()-1, _a, _a1);
	addToTranslate(tranChart, b.size()-1, _b, _b1);
	addToTranslate(tranChart, c.size()-1, _c, _c1);
	addToTranslate(tranChart, d.size(), _d, _d1);

	std::string googlens;
	std::ifstream infile;
	std::ofstream myfile("C:\\EmguCam\\codeJam1\\codeJam1\\A-small-attempt2.out");
	infile.open ("C:\\EmguCam\\codeJam1\\codeJam1\\A-small-attempt2.in");

	int caseIndx = 1;
	std::map<char,char>::iterator it;
	int line = 0;

	while(!infile.eof()) // To get you all the lines.
    {
	
        getline(infile, googlens); // Saves the line in STRING.
		if(line == 0)
		{
			getline(infile, googlens);
			line ++;
		}

		if(googlens.size() == 0)
		{break;}
		int* spaceIdx = new int[1024];
		findSpaces(googlens, spaceIdx);
	
		removeSpaces(googlens);
		char * tranlated = new char[googlens.size()+1];
		tranlated[googlens.size()] = '\0';

		for(int i = 0; i < googlens.size(); i++)
		{
			it=tranChart.find(googlens[i]);
			tranlated[i] = it->second;
		}
		std::string english = tranlated;		
		addSpaces(english, spaceIdx);
		  
		myfile <<  "Case #" << caseIndx++ << ": "<< english << "\n"; 
		delete [] spaceIdx;
    }
	infile.close();
	myfile.close();	

	system("pause");
	return 0;
}

