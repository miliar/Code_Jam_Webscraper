#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

ifstream fin("B-large (1).in");
ofstream fout("1c_blarge.out");

//#define fout cout

long long  d[2000000];
long long a[2000];
vector<long long> list;

int main()
{
	int T;
	fin >> T;
	for (int cases =0; cases<T; cases++)
	{
		long long L, N, C;
		long long t;
		fin >> L >> t >> N >> C;
		fout << "Case #" << cases+1 << ": ";
		for (int i=0; i<C; i++) fin >> a[i];
		d[0] = 0;
		for (int i=1; i<=N; i++) d[i] = d[i-1] + a[(i-1)%C]*2;
		int k = -1;
		for (int i=0; i<=N; i++)
			if (d[i] >= t)
			{
				k = i;
				break;
			}
		if (k == -1)
		{
			fout << d[N] << '\n';
			continue;
		}

		list.clear();
		for (int i=k; i<N; i++)
		{
			list.push_back(d[i+1]-d[i]);
		}
		if (k > 0)
		{
			list.push_back(d[k]-t);
		}
		sort(list.begin(), list.end());
		long long ans = 0;
		for (int i=max(0, (int)(list.size()-L)); i<list.size(); i++)
			ans += list[i];
		cerr << cases << endl;
		fout << d[N] - ans/2 << '\n';
	}
	return 0;
}