#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	ifstream fin("b2.txt");
	ofstream fout("b2_sol.txt");

	int t;
	fin >> t;
	for ( int tt = 1; tt <= t; ++tt )
	{
		int n,w,l;
		fin >> n >> w >> l;
		vector< pair<int,int> > r(n);
		for (int i = 0; i < n; ++i)
		{
			fin >> r[i].first;
			r[i].second = i;
		}
		sort(r.begin(), r.end());
		bool mirrored = false;
		if (w < l)
		{
			mirrored = true;
			int tmp = w;
			w = l;
			l = tmp;
		}

		vector<int> x(n);
		vector<int> y(n);
		int i = 0;
		int cy = 0;
		while (i < n)
		{
			int j = i + 1;
			int s = 0;
			while (j < n && s + r[j-1].first + r[j].first <= w)
			{
				s += r[j-1].first + r[j].first;
				++j;
			}
			int ny = cy + (i > 0 ? (r[i-1].first + r[j-1].first) : 0);
			s = 0;
			for (int k = i; k < j; ++k)
			{
				if (k > i) s += r[k-1].first + r[k].first;
				x[k] = s;
				y[k] = ny;
			}
			i = j;
			cy = ny;
		}

		vector<int> rx(n), ry(n);
		for (int i = 0; i < n; ++i)
		{
			if (mirrored)
			{
				rx[r[i].second] = y[i];
				ry[r[i].second] = x[i];
			}
			else
			{
				rx[r[i].second] = x[i];
				ry[r[i].second] = y[i];
			}
		}
				
		fout <<"Case #" << tt << ":";
		for (int i = 0; i < n; ++i) fout << " " << rx[i] << " " << ry[i];
		fout << "\n";
	}

	fin.close();
	fout.close();
}