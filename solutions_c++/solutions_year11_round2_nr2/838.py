#include <fstream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int a[2000000];
int n;
ifstream fin("B-small-attempt0.in");
ofstream fout("1b_b.out");
//#define fout cout 

int main()
{
	int T;
	fin >> T;
	for (int cases =0; cases < T; cases++)
	{
		fout << "Case #" << cases+1 << ": ";
		int C, D;
		fin >> D >> C;
		n =0;
		for (int i=0; i<D; i++)
		{
			int P, V;
			fin >> P >> V;
			for (int j=0; j<V; j++)
				a[n++] = P*2;
		}
		sort(a, a+n);
		C*=2;

		int l = 0;
		int r = 200000000;
		while (l <= r)
		{
			int m = (l+r)/2;
			int lastpos = -400000000;
			bool success=true;
			for (int i=0; i<n; i++)
				if (a[i] - m >= lastpos+C)
				{
					lastpos = a[i]-m;
				} else {
					if (abs(lastpos+C-a[i]) > m) {success=false; break;}
					lastpos = lastpos+C;
				}
			if (success)
			{
				r = m-1;
			}
			else l=m+1;
		}

		fout << l *0.5 << '\n';
	}
	return 0;
}