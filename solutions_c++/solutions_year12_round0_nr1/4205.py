// Google Speaking in Tongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;


char Convert(char Raw)
{
	if ( Raw == 'y' ) return 'a';
	if ( Raw == 'n' ) return 'b';
	if ( Raw == 'f' ) return 'c';
	if ( Raw == 'i' ) return 'd';
	if ( Raw == 'c' ) return 'e';
	if ( Raw == 'w' ) return 'f';
	if ( Raw == 'l' ) return 'g';
	if ( Raw == 'b' ) return 'h';
	if ( Raw == 'k' ) return 'i';
	if ( Raw == 'u' ) return 'j';
	if ( Raw == 'o' ) return 'k';
	if ( Raw == 'm' ) return 'l';
	if ( Raw == 'x' ) return 'm';
	if ( Raw == 's' ) return 'n';
	if ( Raw == 'e' ) return 'o';
	if ( Raw == 'v' ) return 'p';
	if ( Raw == 'z' ) return 'q';
	if ( Raw == 'p' ) return 'r';
	if ( Raw == 'd' ) return 's';
	if ( Raw == 'r' ) return 't';
	if ( Raw == 'j' ) return 'u';
	if ( Raw == 'g' ) return 'v';
	if ( Raw == 't' ) return 'w';
	if ( Raw == 'h' ) return 'x';
	if ( Raw == 'a' ) return 'y';
	if ( Raw == 'q' ) return 'z';
}



int main()
{
	fstream InputFile;
	InputFile.open("A-small-attempt0.in");
	string NumberOfCases;
	getline(InputFile, NumberOfCases);
	int Cases = atoi(NumberOfCases.c_str());
	string CurrentLine;
	vector<string> Translated;
	for ( int i = 1; i <= Cases ; i++ )
	{
		getline(InputFile, CurrentLine);
		for ( int t = 0; t < CurrentLine.length(); t++ )
		{
			CurrentLine[t] = Convert(CurrentLine[t]);
		}
		Translated.push_back(CurrentLine);
	}
	for ( int t = 0; t < Translated.size(); t++ )
	{
		cout<<Translated[t]<<endl;
	}
	ofstream OutputFile;
	OutputFile.open("Output.txt");
	for ( int t = 1; t <= Cases; t++ )
	{
		OutputFile<<"Case #"<<t<<": "<<Translated[t-1]<<endl;
	}
	OutputFile.close();
	InputFile.close();
}
