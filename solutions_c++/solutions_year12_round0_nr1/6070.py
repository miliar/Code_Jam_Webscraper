// CJProject.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

#define sz(a) int((a).size())
#define fr(i, a, b) for(i = (a); i < (b); ++i)


int main(void)
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	string googlerese = "yhesocvxduiglbkrztnwjpfmaq";

	int n = 0, k = 0, i = 0, j = 0; string sin; string sout; string s;

	fin >> n;
	getline(fin, s); // dummy

	fr(i, 0, n)
	{
		fout << "Case #" << i+1 << ": ";
		getline(fin, sin);

		k = sz(sin);
		fr(j, 0, k) 
		{
			if ( sin[j] == ' ' ) { sout += ' '; continue; }
			
			sout += googlerese[sin[j] - 97];
		}

		fout << sout << endl;
		sout.clear(); sin.clear();
	}
	
	return 0;
}

