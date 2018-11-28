// Dancing With the Googlers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int t=0,n=0,s=0,p=0;
	int m[2];
	int v;
	ifstream f("c:\\B-large.in");
	ofstream o("c:\\result.txt");
	f>>t;
	for(int i=1;i<=t;i++){
		f>>n>>s>>p;
		int sc = 0;
		int cc = 0;
		for(int k=0;k<n;k++) {
			f>>v;
			if (v==0) {
				m[0]=0;
				m[1]=0;
			} else if (v%3==0) {
				m[0]=v/3;
				m[1]=v/3+1;
			} else if (v%3==1){
				m[0]=v/3+1;
				m[1]=v/3+1;
			} else {
				m[0]=v/3+1;
				m[1]=v/3+2;
			}
			if (m[0]>=p) {
				cc++;
			} else if (m[1]>=p&&sc<s){
				sc++;
			}
		}
		o << "Case #"<<i<<": " << cc+sc <<endl;
	}
	return 0;
}

