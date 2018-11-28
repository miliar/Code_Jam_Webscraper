// GCJ 2011 Qual 3.cpp : main project file.

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

int main()
{
	ifstream infile;
	infile.open("C-large.in");
	ofstream outfile("C-large.out");
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
	for(int i = 0; i < cases; i++) {
		int N;
		ss >> N;
		vector<int> a;
		for(int j = 0; j < N; j++) {
			int val;
			ss >> val;
			a.push_back(val);
		}
		sort(a.begin(), a.end());
		int xor = 0, sum = 0;
		for(int j = 0; j < a.size(); j++) {
			xor = xor ^ a[j];
			sum = sum + a[j];
		}
		outfile << "Case #" << (i+1) << ": ";
		if(xor != 0) outfile << "NO" << endl;
		else outfile << (sum - a[0]) << endl;
	}
	outfile.close();
	return 0;
}