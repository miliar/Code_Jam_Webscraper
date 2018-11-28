// GCJ 2011 Qual 2.cpp : main project file.

// Test.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

string solve(vector<string> a, vector<string> b, string c) {
	string ret = "";
	for(int i = 0; i < c.size(); i++) {
		char combine = ' ';
		if(ret.size() > 0) {
			string lasttwo = ret[(int)ret.size()-1] + string(1, c[i]);
			for(int j = 0; j < a.size(); j++) {
				if(a[j][0] == lasttwo[0] && a[j][1] == lasttwo[1]) combine = a[j][2];
				if(a[j][0] == lasttwo[1] && a[j][1] == lasttwo[0]) combine = a[j][2];
			}
		}
		if(combine != ' ')
			ret[(int)ret.size()-1] = combine;
		else {
			bool found = false;
			for(int j = 0; j < b.size(); j++) {
				if(ret.find(b[j][1]) != -1 && b[j][0] == c[i]) found = true;
				if(ret.find(b[j][0]) != -1 && b[j][1] == c[i]) found = true;
			}
			if(found) ret = "";
			else ret = ret + c[i];
		}
	}
	string formatted = "";
	for(int i = 0; i < ret.size(); i++) {
		if(i > 0) formatted = formatted + ", ";
		formatted = formatted + ret[i];
	}
	return "[" + formatted + "]";
}

int main()
{
	ifstream infile;
	infile.open("B-large.in");
	ofstream outfile("B-large.out");
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
		int C, D, N;
		ss >> C;
		vector<string> a, b;
		for(int j = 0; j < C; j++) {
			string s;
			ss >> s;
			a.push_back(s);
		}
		ss >> D;
		for(int j = 0; j < D; j++) {
			string s;
			ss >> s;
			b.push_back(s);
		}
		ss >> N;
		string c;
		ss >> c;
		string ret = solve(a, b, c);
		outfile << "Case #" << (i+1) << ": " << ret << endl;
	}
	outfile.close();
	return 0;
}