#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <cmath>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int N;
int x[2000];
int d[2000];

const int Inf = 999888777;

void run(int s, int i)
{
	for (int j=s+1; j<i; ++j)
	{
		if (x[j] == i)
		{
			int deg = 1;
			for (int k=i+1; k<N; ++k)
			{
				if (d[k] > d[i])
				{
					double f = (i-j)*(d[k]-d[i])/(k-i);
					deg = max(deg, (int)(ceil(f)+1e-3) + 1);
				}
			}
			
			cout << "s: " << s << " i: " << i << " deg: " << deg << " j: " << j << endl;
			d[j] = d[i] - deg;
			run(s, j);
		}
	}
}

void solve()
{
	for (int i=0;i<N; ++i)
	{
		d[i] = -Inf;
	}

	d[0] = 0;
	
	for (int i=0;i<N-1; i=x[i])
	{
		d[x[i]] = 0;
		run(i, x[i]);
	}
	
	for (int i=0;i<N;++i)
	{
		if (d[i] == -Inf)
		{
			fout << " Impossible" << endl;
			return;
		}
		for (int j=i+1; j<x[i]; ++j)
		{
			if ((j-i)*(d[x[i]]-d[i]) <= (x[i]-i)*(d[j]-d[i]))
			{
				fout << " Impossible" << endl;
				return;
			}
		}
	}
	
	int m = d[0];
	for (int i=0;i<N;++i) m = min(m, d[i]);
	for (int i=0;i<N;++i) fout << " " << d[i] - m;
	fout << endl;
}

int main()
{
	int T;
	fin >> T;
	fout.precision(8);
	fout.setf(ios::fixed, ios::floatfield);	
	for (int tcase=0;tcase<T;++tcase)
	{
		fin >> N;
		
		for (int k=0;k<N-1;++k)
		{
			fin >> x[k];
			--x[k];
		}
		
		fout << "Case #" << tcase+1 << ":";
		solve();
	}
	return 0;
}