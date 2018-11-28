// CodeJamTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

string next(string num) {
	string s = num;
	string f = s;
	next_permutation(s.begin(), s.end());
	sort(f.begin(), f.end());
	if(f == s) {
	 string r;
	 int z = 1, i;
	 for(i = 0; i < f.size(); i++)
		 if(f[i] == '0') z++;
		 else {
			 r.push_back(f[i]);
			 for(; z > 0; --z)
				 r.push_back('0');
		 }
	 return r;
	}
	return s;
/*
	string s = num;
	sort(s.begin(), s.end());
	reverse(s.begin(), s.end());
	string res;
	if(s == num) {
		string temp = num.substr(0, num.size() - 1) + '0' + num[num.size() - 1];
		reverse(temp.begin(),temp.end());
		int i =0;
		while(temp[i]=='0')
			i++;
		for(;i<temp.size();i++)
			res.push_back(temp[i]);
		if (temp[0]=='0') {
			while(num.size()>=res.size()) {
				res.push_back('0');
			}
		}
	}
	else {
		next_permutation(num.begin(), num.end());
		res = num;
	}
	return res;*/
}

int main() {
	ifstream fin("C:\\input.txt");
	ofstream fout("C:\\output.txt");

  int n;
  fin >> n;
  for(int i=0;i<n;i++) {
	  string number;
	  fin >> number;
	  fout << "Case #" << (i+1) << ": " << next(number) << endl;
  }
  return 0;
}