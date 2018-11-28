#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <hash_set>
#include <ppl.h>
using namespace std;
using namespace Concurrency;
using namespace stdext;

int a[1000]={0};


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream is("input.txt");
	ofstream os("output.txt");
	int T;
	is >> T;
	for (int  Testnum=1;  Testnum<=T; ++Testnum)
	{
		int n,k,b;
		__int64 t;
		is >> n >> k >> b >> t;
		/*int* x = new int [n];
		int* v = new int [n];
		int* dt = new int [n];
		bool* can = new bool [n];*/
		int x[50];
		int v[50];
		int dt[50];
		bool can[50];
		for (int i = 0; i<n; ++i){
			is >> x[i];
		}
		for (int i = 0; i<n; ++i){
			is >> v[i];
			dt[i] = (b-x[i]);
			can[i] = dt[i] <= t*v[i];
		}
		int got = 0, uncan = 0, swaps = 0;
		for (int i = n-1; i >= 0 && got < k; --i){
			if (can[i]){
				++got;
				swaps += uncan;
			}else{
				++uncan;
			}
		}
		if (got < k)
			os << "Case #" << Testnum << ": " << ("IMPOSSIBLE") << endl;
		else
			os << "Case #" << Testnum << ": " << (swaps) << endl;
		
	}

	return 0;
}

