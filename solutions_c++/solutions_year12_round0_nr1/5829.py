// SpeakingInTongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <iostream>
#include <conio.h>
#include <fstream>
#include <string>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	string strInput, strOutput;
	ifstream ifile ;
	ifile.open("input.in");
	ofstream  ofile;
	ofile.open("output.txt");  

	if (!ifile.is_open())
		return 0;

	getline (ifile, strInput);
	int iTestCaseCount = atoi(strInput.c_str());
	if (iTestCaseCount<=1 || iTestCaseCount>30)
		return 0;


	map<char, char> mapGoogleReseToSaneEnglish;
	mapGoogleReseToSaneEnglish['a'] = 'y';	mapGoogleReseToSaneEnglish['b'] = 'h';
	mapGoogleReseToSaneEnglish['c'] = 'e';	mapGoogleReseToSaneEnglish['d'] = 's';
	mapGoogleReseToSaneEnglish['e'] = 'o';	mapGoogleReseToSaneEnglish['f'] = 'c';
	mapGoogleReseToSaneEnglish['g'] = 'v';	mapGoogleReseToSaneEnglish['h'] = 'x';
	mapGoogleReseToSaneEnglish['i'] = 'd';	mapGoogleReseToSaneEnglish['j'] = 'u';
	mapGoogleReseToSaneEnglish['k'] = 'i';	mapGoogleReseToSaneEnglish['l'] = 'g';
	mapGoogleReseToSaneEnglish['m'] = 'l';	mapGoogleReseToSaneEnglish['n'] = 'b';
	mapGoogleReseToSaneEnglish['o'] = 'k';	mapGoogleReseToSaneEnglish['p'] = 'r';
	mapGoogleReseToSaneEnglish['q'] = 'z';	mapGoogleReseToSaneEnglish['r'] = 't';
	mapGoogleReseToSaneEnglish['s'] = 'n';	mapGoogleReseToSaneEnglish['t'] = 'w';
	mapGoogleReseToSaneEnglish['u'] = 'j';	mapGoogleReseToSaneEnglish['v'] = 'p';
	mapGoogleReseToSaneEnglish['w'] = 'f';	mapGoogleReseToSaneEnglish['x'] = 'm';
	mapGoogleReseToSaneEnglish['y'] = 'a';	mapGoogleReseToSaneEnglish['z'] = 'q';
	mapGoogleReseToSaneEnglish[' '] = ' ';


	for (int index=1; index<=iTestCaseCount; ++index)
	{
		strOutput = "Case #";
		char buff[32];
		memset(buff, 0, 32);
		_itoa(index, buff, 10);
		strOutput += buff;
		strOutput += ": ";

		getline (ifile, strInput);
		basic_string<char>::iterator itr = strInput.begin();
		while (itr!=strInput.end())
		{
			char test = *itr;
			test = mapGoogleReseToSaneEnglish[test];
			strOutput += test;

			itr++;
		}

		ofile.write(strOutput.c_str(), strOutput.length());
		ofile.write("\n", 1);
	}

	ifile.close();
	ofile.close();

	_getch();
	return 0;
}

