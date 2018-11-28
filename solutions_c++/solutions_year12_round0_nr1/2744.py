// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <assert.h>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	//FILE *cin = fopen ( "Asmall.in", "r" );
	//FILE *cout = fopen ( "Asmall.out", "w" );

	map<char,char> tabTranlation;
	tabTranlation['a'] = 'y';
	tabTranlation['b'] = 'h';
	tabTranlation['c'] = 'e';
	tabTranlation['d'] = 's';
	tabTranlation['e'] = 'o';
	tabTranlation['f'] = 'c';
	tabTranlation['g'] = 'v';
	tabTranlation['h'] = 'x';
	tabTranlation['i'] = 'd';
	tabTranlation['j'] = 'u';
	tabTranlation['k'] = 'i';
	tabTranlation['l'] = 'g';
	tabTranlation['m'] = 'l';
	tabTranlation['n'] = 'b';
	tabTranlation['o'] = 'k';
	tabTranlation['p'] = 'r';
	tabTranlation['q'] = 'z';
	tabTranlation['r'] = 't';
	tabTranlation['s'] = 'n';
	tabTranlation['t'] = 'w';
	tabTranlation['u'] = 'j';
	tabTranlation['v'] = 'p';
	tabTranlation['w'] = 'f';
	tabTranlation['x'] = 'm';
	tabTranlation['y'] = 'a';
	tabTranlation['z'] = 'q';
	tabTranlation[' '] = ' ';

	char buffer[200];
	int numCase;
	cin >> numCase;
	string googleString;
	cin.getline(buffer,199);
	for (int i = 0; i < numCase; i++)
	{
		string result;
		
		cin.getline(buffer,199);
		googleString = buffer;
		
		for (int j = 0; j < googleString.length(); j++)
		{
			char c = googleString[j];
			result+= tabTranlation[c];
		}
		
		cout << "Case #" << (i+1) << ": " << result.c_str() << endl;
	}

	return 0;
}

