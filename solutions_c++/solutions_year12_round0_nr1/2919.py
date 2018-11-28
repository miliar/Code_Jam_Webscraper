// Qualification.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");

	//ifstream in("A-large.in");
 //   ofstream out("A-large.out");
	map<char, char> mpMap;
	mpMap['a'] = 'y';
	mpMap['b'] = 'h';
	mpMap['c'] = 'e';
	mpMap['d'] = 's';
	mpMap['e'] = 'o';
	mpMap['f'] = 'c';
	mpMap['g'] = 'v';
	mpMap['h'] = 'x';
	mpMap['i'] = 'd';
	mpMap['j'] = 'u';
	mpMap['k'] = 'i';
	mpMap['l'] = 'g';
	mpMap['m'] = 'l';
	mpMap['n'] = 'b';
	mpMap['o'] = 'k';
	mpMap['p'] = 'r';
	mpMap['q'] = 'z';
	mpMap['r'] = 't';
	mpMap['s'] = 'n';
	mpMap['t'] = 'w';
	mpMap['u'] = 'j';
	mpMap['v'] = 'p';
	mpMap['w'] = 'f';
	mpMap['x'] = 'm';
	mpMap['y'] = 'a';
	mpMap['z'] = 'q';

	int iTasks;
	in >> iTasks;
	string sSentence;	
	getline(in, sSentence);
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		getline(in, sSentence);
		stringstream sStream(sSentence);
		string sWord;
		stringstream sTranslated;
		sStream >> sWord;
		do
		{		
			for( size_t i = 0; i < sWord.size(); i++ )
			{
				sTranslated << mpMap[sWord[i]];
			}
			sWord = "";
			sStream >> sWord;
			if( !sWord.empty() )
				sTranslated << ' ';
		}while(!sWord.empty());
		getline(sTranslated, sSentence);
		out << "Case #" << iCount << ": " << sSentence << endl;
	}
	return 0;
}
