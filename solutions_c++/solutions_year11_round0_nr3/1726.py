#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <map>
#include <vector>

using namespace std;

#define TEST 
#ifdef TEST
ifstream fin("C-large.in");
ofstream fout("c.out");
//#define fout cout
#else
#define fin cin
#endif

int main()
{
	int T;
	fin >> T;

	for (int cases =0; cases < T; cases++)
	{
		int N;
		fout << "Case #" << cases+1 << ": ";
		fin >> N;
		int a=0;
		int mmm = 1000000000;
		int sum = 0;
		for (int i=0; i<N; i++)
		{
			int x;
			fin >> x;
			a ^= x;
			sum += x;
			if (x < mmm) mmm = x;
		}
		if (a == 0)
		{
			fout << sum-mmm << endl;
		}
		else fout << "NO" << endl;
	}
	return 0;
}