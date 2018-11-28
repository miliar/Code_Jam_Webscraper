#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <hash_set>
#include <ppl.h>
using namespace std;
using namespace Concurrency;
using namespace stdext;
#define MN 500
int a[1000]={0};

int cs[MN+1][MN+1]={0};
__int64 c[MN+1][MN+1]={0};

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream is("input.txt");
	ofstream os("output.txt");
	int T;
	is >> T;

	for (int i = 0; i <= MN; ++i){
		c[i][0] = 1;
		for (int j = 1; j < i; ++j){
			c[i][j] = (c[i-1][j]+c[i-1][j-1])%100003;
		}
		c[i][i] = 1;
	}
	for (int i = 1; i <= MN; ++i){
		cs[i][1] = cs[i][0] = 1;
		for (int j = 2; j < i; ++j){
			for (int k = 1; k < j; ++k){
				cs[i][j] = (cs[i][j] + cs[j][j-k]*c[i-j-1][k-1])%100003;
			}
			cs[i][0] = (cs[i][0] + cs[i][j])%100003;
		}
	}
	for (int  Testnum=1;  Testnum<=T; ++Testnum)
	{
		int n;
		is >> n;
		
		os << "Case #" << Testnum << ": " << cs[n][0] << endl;
		
	}

	return 0;
}

