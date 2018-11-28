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

using namespace std;

int mx(int x, int y) {
	if(x>y) return x;
	return y;
}

int main()
{
	ifstream infile;
	infile.open("B-small-attempt0.in");
	ofstream outfile("B-small-attempt0.out");
	string str, input;
	int cases;
	if (infile.is_open()) {
		infile>>cases;
	}
	else {
		return 0;
	}
	for(int i=0;i<cases;i++) {
		int N,S,p;
		infile>>N>>S>>p;
		int mem[105][105];
		memset(mem,-1,sizeof(mem));
		mem[0][0]=0;
		vector<int> v;
		for(int j=0;j<N;j++) {
			int score;
			infile>>score;
			int surprise=-1,nonsurprise=-1;
			for(int s1=0;s1<=10;s1++)
				for(int s2=s1;s2<=10&&s2<=s1+2;s2++) 
					for(int s3=s2;s3<=10&&s3<=s1+2;s3++) {
						if(s1+s2+s3!=score) continue;
						if(s3==s1+2) surprise=mx(surprise,(p<=s3));
						else nonsurprise=mx(nonsurprise,(p<=s3));
					}
			if(surprise>=0) {
				for(int k=0;k<=100;k++) {
					if(mem[j][k]==-1) continue;
					mem[j+1][k+1]=mx(mem[j+1][k+1],(mem[j][k]+surprise));
				}
			}
			if(nonsurprise>=0) {
				for(int k=0;k<=100;k++) {
					if(mem[j][k]==-1) continue;
					mem[j+1][k]=mx(mem[j+1][k],(mem[j][k]+nonsurprise));
				}
			}
		}
		outfile << "Case #" << (i+1) << ": " << mem[N][S] << endl; 
	}
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}