// GCJ 2011 Qual 1.cpp : main project file.

// Test.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <map>
#include <set>

using namespace std;

int doit(int low, int high) {
	int digits=0;
	int t=low;
	while(t) {
		t/=10;
		digits++;
	}
	int pow10[10];
	pow10[0]=1;
	for(int i=1;i<10;i++) pow10[i]=pow10[i-1]*10;
	int ret=0;
	for(int i=low;i<=high;i++) {
		set<int> found;
		for(int j=1;j<digits;j++) {
			int k=i/pow10[j]+i%pow10[j]*pow10[digits-j];
			if(i<k&&k<=high) {
				if(found.count(k)) continue;
				found.insert(k);
				ret++;
			}
		}
	}
	return ret;
}

int main()
{
	ifstream infile;
	infile.open("C-small-attempt0.in");
	ofstream outfile("C-small-attempt0.out");
	int cases;
	if (infile.is_open()) {
		infile>>cases;
	}
	else {
		return 0;
	}
	for(int i=0;i<cases;i++) {
		int low,high;
		infile>>low>>high;
		outfile << "Case #" << (i+1) << ": " << doit(low,high) << endl; 
	}
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}