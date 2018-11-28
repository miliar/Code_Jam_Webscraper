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

int eval(string list, string word, vector<string> &dictionary) {
	int ret = 0;
	int possible[101];
	for(int i = 0; i < dictionary.size(); i++) possible[i] = (dictionary[i].size() == word.size());
	for(int i = 0; i < 26; i++) {
		bool shouldGuess = false;
		for(int j = 0; j < dictionary.size(); j++) {
			if(!possible[j]) continue;
			if(dictionary[j].find(list[i]) == -1) continue;
			shouldGuess = true;
		}
		if(!shouldGuess) continue;
		if(word.find(list[i]) == -1) ret++;
		for(int j = 0; j < dictionary.size(); j++) {
			if(!possible[j]) continue;
			for(int k = 0; k < word.size(); k++) {
				if((dictionary[j][k] == list[i]) != (word[k] == list[i])) possible[j] = 0;
			}
		}
	}
	return ret;
}

string doit(vector<string> &dictionary, vector<string> &lists) {
	string ret = "";
	for(int i = 0; i < lists.size(); i++) {
		int best = -1;
		string bestStr = "";
		for(int j = 0; j < dictionary.size(); j++) {
			int cur = eval(lists[i], dictionary[j], dictionary);
			if(cur > best) {
				best = cur;
				bestStr = dictionary[j];
			}
		}
		if(ret.size()) ret = ret + " ";
		ret = ret + bestStr;
	}
	return ret;
}

int main()
{
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile("output.txt");
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
		int n, m;
		ss >> n >> m;
		vector<string> dictionary, lists;
		for(int j = 0; j < n; j++) {
			string s;
			ss >> s;
			dictionary.push_back(s);
		}
		for(int j = 0; j < m; j++) {
			string s;
			ss >> s;
			lists.push_back(s);
		}
		outfile << "Case #" << (i+1) << ": " << doit(dictionary, lists) << endl;
	}
	outfile.close();
	cin.get();
	return 0;
}