// GCJ 2011 Qual 4.cpp : main project file.

// Test.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

string eval(long long N, long long PD, long long PG) {
	bool possible = false;
	for(int i = 1; i <= N && i <= 100; i++) {
		if(PD * i % 100 == 0) possible = true;
	}
	if(!possible) return "Broken";
	if(PD < 100 && PG == 100) return "Broken";
	if(PD > 0 && PG == 0) return "Broken";
	return "Possible";
}

int main()
{
	ifstream infile;
	infile.open("A-small-attempt0.in");
	ofstream outfile("A-small-attempt0.out");
	string str, input;
	if (infile.is_open())
	while (!infile.eof()) {
		getline(infile,str);
		input = input + " " + str;
	}
	stringstream ss;
	int cases;
	ss << input;
	ss >> cases;
	cout << cases << endl;
	for(int i = 0; i < cases; i++) {
		long long N, PD, PG;
		ss >> N >> PD >> PG;
		outfile << "Case #" << (i+1) << ": " << eval(N, PD, PG) << endl;
	}
	outfile.close();
	cin.get();
	return 0;
}