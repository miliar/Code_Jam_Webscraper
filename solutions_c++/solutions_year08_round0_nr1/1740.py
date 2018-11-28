//#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <sstream>



using namespace std;
using std::string;


ifstream fin("A-small-attempt0.in");
ofstream fout("A-small.out");

#define FOR(a,b,c) for(int a=(b);a<(c);a++)


char line[100];

#define MAX_S 10
#define MAX_Q 100

int solve()
{
	string s;
	string ss[MAX_S];
	string qq[MAX_Q];
	
	int S, Q;
	int i, j;
	
	int qn[MAX_Q];
	
	fin >> S;	
	getline(fin,s);
	
	for(int i = 0; i < S; i++) {
		getline(fin, ss[i]);
		//fout<< ss[i] << endl;
	}
	
	fin >> Q;	
	getline(fin,s);
	
	for(i = 0; i < Q; i++) {
		getline(fin, qq[i]);
		//fout<< qq[i] << endl;
		for(j = 0; j < S; j++) {
			if (qq[i] == ss[j])
				qn[i] = j;
		}
	}
	/*
	for(i = 0; i < Q; i++) {
		fout << qn[i] << endl;
	}
	*/
	int cnt = 0;
	int cnt1;
	int point;
	int det[MAX_Q];
	
	for(i = 0; i < S; i++) {
		det[i] = 0;
	}
	
	for(i = 0; i < Q; i++) {
		
		if (det[qn[i]] == 0) {
			if (i >= S-1) {	// check
				cnt1 = 0;
				for (j = 0; j < S; j++) {
					if (det[j] > 0)
						cnt1++;
				}
				
				if (cnt1 == S-1) {
					cnt++;
					//point = i+1;
					for (j = 0; j < S; j++) {	// clear all
						det[j] = 0;
					}
				}
			}
		}
		det[qn[i]]++;
	}
	
	return cnt;
}

int main()
{
	int i;
	int N;
	int cnt;
	
	fin >> N;
	
	for(int i = 0; i < N; i++) {
		cnt = solve();
		fout << "Case #" << i+1 << ": " << cnt << endl;
	}
	
	return 0;
}
