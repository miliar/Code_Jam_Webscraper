// GoogleLang.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <map>

using namespace std;

#define CHAR_SIZE 36000

filebuf fb;
int iNumberOfTests = 0;
map<char, char> mpLetter;

void FillMap()
{
	mpLetter['a'] = 'y';
	mpLetter['b'] = 'h';
	mpLetter['c'] = 'e';
	mpLetter['d'] = 's';
	mpLetter['e'] = 'o';
	mpLetter['f'] = 'c';
	mpLetter['g'] = 'v';
	mpLetter['h'] = 'x';
	mpLetter['i'] = 'd';
	mpLetter['j'] = 'u';
	mpLetter['k'] = 'i';
	mpLetter['l'] = 'g';
	mpLetter['m'] = 'l';
	mpLetter['n'] = 'b';
	mpLetter['o'] = 'k';
	mpLetter['p'] = 'r';
	mpLetter['q'] = 'z';
	mpLetter['r'] = 't';
	mpLetter['s'] = 'n';
	mpLetter['t'] = 'w';
	mpLetter['u'] = 'j';
	mpLetter['v'] = 'p';
	mpLetter['w'] = 'f';
	mpLetter['x'] = 'm';
	mpLetter['y'] = 'a';
	mpLetter['z'] = 'q';
	// just to avoid special treatment.
	mpLetter[' '] = ' ';
}

void ReadLineFromFile(char *s)
{
	if(!fb.is_open())
	{
		fb.open("A-small-attempt0.in", ios::in);//Done & Correct
	}
	istream is(&fb);
	if(iNumberOfTests == 0)
	{
		is.getline(s, CHAR_SIZE);
		iNumberOfTests = ::atoi(s);
	}
	is.getline(s, CHAR_SIZE);
}

void OutputData(int iCase, char* pLine)
{
#ifdef _DEBUG
	cout << "Case #"<<iCase<< ": " << pLine << "\r\n";
#endif

	ofstream outfile("google.txt", ios::out | ios::app);
	outfile << "Case #"<<iCase<< ": " << pLine << "\r\n";
	outfile.flush();
	if(iCase == (iNumberOfTests))
	{
		fb.close();
	}
}

void ChangeLetter(char * Line)
{
	char * pLineBeg = Line; 
	while(*Line != '\0')
	{
		*Line = mpLetter.find(*Line)->second;
		Line+= sizeof(char);
	}
	Line = pLineBeg;
	return; 
}

int main()
{
	char * Line; 
	int iCase = 1;

	FillMap();
	do{
	Line = new char[CHAR_SIZE];
	ReadLineFromFile(Line);
	ChangeLetter(Line);
	OutputData(iCase, Line);
	iCase++;
	delete Line;
	}while (iCase <= iNumberOfTests);
	return 0;
}

