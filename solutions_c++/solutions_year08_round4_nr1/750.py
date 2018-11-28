#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

int can(int node, int val, vector <int> & value, vector <int> & gate, vector <int> & status, vector <int> & best1, vector <int> & best0)
{
	if (value[node] != -1)
	{
		if (val == value[node]) return 0;
		return 1000000000;
	}

	if (val == 0)
	{
		if (best0[node] != -1) return best0[node];
		int best = 1000000000;

		if (gate[node] == 1)
		{
			best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0));
			best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0));
			best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0));
			if (status[node] == 1) best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0) + 1);
			return best0[node] = best;
		}

		best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0));
		if (status[node] == 1)
		{
			best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0) + 1);
			best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0) + 1);
			best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0) + 1);
		}
		return best0[node] = best;
	}

	if (best1[node] != -1) return best1[node];
	int best = 1000000000;

	if (gate[node] == 0)
	{
		best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0));
		best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0));
		best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0));
		if (status[node] == 1) best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0) + 1);
		return best1[node] = best;
	}

	best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0));
	if (status[node] == 1)
	{
		best = min(best, can(node * 2, 0, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0) + 1);
		best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 0, value, gate, status, best1, best0) + 1);
		best = min(best, can(node * 2, 1, value, gate, status, best1, best0) + can(node * 2 + 1, 1, value, gate, status, best1, best0) + 1);
	}
	return best1[node] = best;
}

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	int T, N;

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		int m, v, i;
	
		fout << "Case #" << T << ": ";
		fin >> m >> v;
		vector <int> value(m + 1, -1);
		vector <int> gate(m + 1, -1);
		vector <int> status(m + 1, -1);
		vector <int> best0(m + 1, -1);
		vector <int> best1(m + 1, -1);

		for(i = 1; i <= (m - 1) / 2; ++i)
			fin >> gate[i] >> status[i];
		for(; i <= m; ++i)
			fin >> value[i];

		int res = can(1, v, value, gate, status, best1, best0);

		if (res < 1000000000) fout << res << endl; else fout << "IMPOSSIBLE" << endl;
	}
	return 0;
}