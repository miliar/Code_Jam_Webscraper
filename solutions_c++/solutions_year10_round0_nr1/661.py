#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <ppl.h>
using namespace std;
using namespace Concurrency;
int a[10]={0};


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream is("input.txt");
	ofstream os("output.txt");
	int T;
	is >> T;
	for (int i=1; i<=T; ++i)
	{
		int K, N;
		is >> N >> K;
		os << "Case #" << i << ": " << (((K+1)&((1<<N)-1))==0?"ON":"OFF") << endl;
	}
	
	/*parallel_for(0, T, [&](int i){
		a[i]=;
	});*/
	return 0;
}

