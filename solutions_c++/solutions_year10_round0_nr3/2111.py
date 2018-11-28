#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#define _INPUT_FILE_PATH "G:\\C-small-attempt0.in"
#define _OUTUT_FILE_PATH "G:\\C-small-attempt0.out"

// compiled on visual studio 2010

using namespace std;

unsigned int cases;
unsigned int pow10[9] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };
unsigned int pow2[32] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648};


void readinputfile();
unsigned int str2int(string s) { unsigned int i=0,C=s.length(); for (unsigned int c=0;c<C;c++) i += (s[C-c-1]-'0')*pow10[c]; return (i); }

void main() {
	ifstream inputfile; ofstream outputfile;
	inputfile.open(_INPUT_FILE_PATH); outputfile.open(_OUTUT_FILE_PATH);
	if (inputfile.is_open() && outputfile.is_open())
	{
		string inputline;
		getline(inputfile,inputline,'\n'); cases = str2int(inputline);
		for (unsigned int t=1; t<=cases; t++) {
			getline(inputfile,inputline,' '); unsigned int r = str2int(inputline);
			getline(inputfile,inputline,' '); unsigned int k = str2int(inputline);
			getline(inputfile,inputline,'\n'); unsigned int n = str2int(inputline);
			unsigned long long revenue = 0;
			unsigned int *g = new unsigned int[100];
			for (unsigned int ni=0; ni<n; ni++) {
				if (ni+1<n) getline(inputfile,inputline,' ');
				if (ni+1==n) getline(inputfile,inputline,'\n');
				g[ni] = str2int(inputline);
			}
			for (unsigned int ri=0, gi=0, ki=0, gifirst; ri<r; ri++, ki=0) {
				gifirst = gi;
				while (true) {
					unsigned int gnext = g[gi];
					if( (ki+gnext<=k) ) { ki +=gnext; revenue += gnext; if (gi+1<n) gi++; else gi=0; }
					else break;
					if (gi == gifirst) break;
				}
			}
			//cout << "Case #" << t << ": r = " << r << " rides, k = " << k << " capacity, n = " << n << " groups: " << revenue << endl;
			//for (unsigned int ni=0; ni<n; ni++) { cout << " " << g[ni]; } cout << endl;
			outputfile << "Case #" << t << ": " << revenue << endl;
		}
		inputfile.close(); outputfile.close();
	}
	else cout << "couldn't open file" << endl;
}


