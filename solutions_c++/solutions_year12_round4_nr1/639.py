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

int N, D;
int l[10000];
int d[10000];
int s[10000];

void solve()
{
	for (int i=0; i<N; ++i)
		s[i]=0;
		
	s[0] = d[0];
	
	for (int i=0; i<N; ++i)
	{
		int x = s[i];
		
		for (int j=i+1; j<N && d[j]<=d[i]+x; ++j)
		{
			int y = min(d[j] - d[i], l[j]);
			s[j] = max(s[j], y);
		}
		
		if (d[i] + s[i] >= D)
		{
			fout << "YES" << endl;
			return;
		}
	}
	
	fout << "NO" << endl;
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
		
		for (int k=0;k<N;++k) fin >> d[k] >> l[k];
		
		fin >> D;
		
		fout << "Case #" << tcase+1 << ": ";
		solve();
	}
	return 0;
}