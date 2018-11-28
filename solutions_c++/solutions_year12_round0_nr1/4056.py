// Test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>
#include <vector>

using namespace std;

char Translate(char input)
{
	switch(input) {
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case 'm':
		return 'l';
	case 'n':
		return 'b';
	case 'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case 't':
		return 'w';
	case 'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	case ' ':
		return ' ';
	default:
		cout << "error" << endl;
	}
}

int main()
{
	int numTest;
	char num[3];
	ifstream in;
	in.open("A-small-attempt0.in");
	in.getline(num, 3);
	numTest = atoi(num);
	ofstream out;
	out.open("output.txt");
	for(int i=0; i<numTest; i++) {
		char buf[1024];
		in.getline(buf, 1024);
		out << "Case #" << i+1 << ": ";
		for(int i=0; i<strlen(buf); i++) {
			out << Translate(buf[i]);
		}
		if(i != numTest-1)
			out << endl;
	}
	in.close();
	out.close();
	return 0;
}