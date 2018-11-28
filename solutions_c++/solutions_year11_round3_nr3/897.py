#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <fstream>
using namespace std;

int gcd(int a, int b)
{
	return (a==0) ? b : gcd(b%a, a); 
}

int main()
{
	int t, tt;

	ifstream fin("c.in");
	ofstream fout("c.out");

	fin >> tt;
	for( t = 1; t <= tt; ++ t )
	{
		int N, L, H;
		fin >> N >> L >> H;
		long long *f = new long long[N];
		for (int i=0; i<N; i++)
			fin >> f[i];
		
		bool okest = false;
		for (int i=L; i<=H; i++)
		{
			bool ok = true;
			for (int j=0; j<N; j++)
				if (i%f[j]!=0 && f[j]%i!=0)
				{
					ok = false;
					break;
				}
			if (ok)
			{
				fout << "Case #" << t << ": " << i << endl;
				okest = true;
				break;
			}
		}
		if (!okest)
			fout << "Case #" << t << ": NO" << endl;
	}

	return 0;
}
