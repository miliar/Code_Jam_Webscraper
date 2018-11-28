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
	ifstream fin("a2.txt");
	ofstream fout("a2_sol.txt");

	int t;
	fin >> t;
	for ( int tt = 1; tt <= t; ++tt )
	{
		int n,g;
		fin >> n;
		vector<int> d(n);
		vector<int> l(n);
		for (int i = 0; i < n; ++i)
			fin >> d[i] >> l[i];
		fin >> g;

		vector<int> maxswing(n,-1);
		maxswing[0] = d[0];
		int j = 1;
		for (int i = 0; i < n; ++i)
		{
			while (j < n && d[i] + maxswing[i] >= d[j])
			{
				maxswing[j] = (l[j] < d[j] - d[i] ? l[j] : d[j] - d[i]);
				++j;
			}
		}

		bool res = false;
		for (int i = 0; i < n; ++i)
		{
			if ((maxswing[i] != -1) && (d[i] + maxswing[i] >= g)) res = true;
		}
		
		fout <<"Case #" << tt << ": " << (res ? "YES" : "NO") << "\n";
	}

	fin.close();
	fout.close();
}