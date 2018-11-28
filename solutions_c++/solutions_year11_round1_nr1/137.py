#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

long long gcd(long long a, long long b)
{
	if(b == 0) return a;
	return gcd(b, a%b);
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fout << "Case #" << i+1 << ": ";
		
		long long N, PD, PG;
		fin >> N >> PD >> PG;
		
		if(PD == 0 && PG == 0) fout << "Possible\n";
		else if(PD == 100 && PG == 100) fout << "Possible\n";
		else if(PG == 100 || PG == 0) fout << "Broken\n";
		else
		{		
			long long g = gcd(PD, 100);
			long long D = 100/g;
			if(D <= N) fout << "Possible\n";
			else fout << "Broken\n";
		}
	}
	return 0;
}