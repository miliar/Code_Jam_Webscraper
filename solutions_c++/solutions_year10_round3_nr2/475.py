// CalcA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int T;
map<int, int, greater<int>> dict;

ifstream in;
ofstream out;

#define cin in
#define cout out

int _tmain(int argc, _TCHAR* argv[])
{
	in.open("B-large.in");
	out.open("res.txt");
	cin >> T;
	int t = T;
	
	while(t-- > 0) {
		if(t == 541) {
			int a = 0;
		}
		unsigned long long L, P, C;
		unsigned long long X = 0;
		cin >> L >> P >> C;
		unsigned long long k = 0;
		while(L * C < P) {
			L *= C;
			k++;
		}
		while(k > 1) {
			k = k / 2;
			X++;
		}
		if(k == 1) ++X;
		cout << "Case #" << T - t << ": " << X << endl;
	}
	return 0;
}

