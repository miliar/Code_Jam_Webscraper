// GCJ 2011 Qual 1.cpp : main project file.

// Test.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

int solve(vector<string> a, vector<int> b) {
	int pos1 = 1, pos2 = 1, t = 0, t1 = 0, t2 = 0;
	if(a.size() == 0) return 0;
	for(int i = 0; i < a.size(); i++) {
		if(a[i] == "O") {
			int dist = abs(b[i] - pos1);
			t = max(t1 + dist, t2) + 1;
			t1 = t;
			pos1 = b[i];
		} else {
			int dist = abs(b[i] - pos2);
			t = max(t2 + dist, t1) + 1;
			t2 = t;
			pos2 = b[i];
		}
	}
	return t;
}

int main()
{
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile("A-large.out");
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
		vector<string> a;
		vector<int> b;
		string robot;
		int pos;
		int commands;
		ss >> commands;
		for(int j = 0; j < commands; j++) {
			ss >> robot >> pos;
			a.push_back(robot);
			b.push_back(pos);
		}
		int t = solve(a, b);
		outfile << "Case #" << (i+1) << ": " << t << endl; 
	}
	outfile.close();
	return 0;
}