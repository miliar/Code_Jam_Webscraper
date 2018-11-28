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

struct position
{
	int r, c;
	bool operator< (position p) const
	{
		if (r == p.r) return c < p.c;
		return r < p.r;
	}
};

int recur(position pos, map <position, int> & table, set <position> forbid)
{
	map <position, int>::iterator m;
	m = table.find(pos);
	if (m != table.end()) return m -> second;

	position p;
	int r = pos.r;
	int c = pos.c;
	int res1 = 0, res2 = 0;

	if (r - 2 >= 0 && c - 1 >= 0)
	{
		p.r = r - 2;
		p.c = c - 1;
		if (forbid.find(p) == forbid.end()) res1 = recur(p, table, forbid);
	}

	if (r - 1 >= 0 && c - 2 >= 0)
	{
		p.r = r - 1;
		p.c = c - 2;
		if (forbid.find(p) == forbid.end()) res2 = recur(p, table, forbid);
	}

	return table[pos] = (res1 + res2) % 10007;
}

int main()
{
	ifstream fin("d.in");
	ofstream fout("d.out");

	int T, N;

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		int h, w, r, i;
		fin >> h >> w >> r;

		fout << "Case #" << T << ": ";

		map <position, int> table;
		position first, p;
		first.r = 0;
		first.c = 0;
		table[first] = 1;
		
		set <position> forbid;

		for(i = 0; i < r; ++i)
		{
			fin >> p.r >> p.c;
			--p.r;
			--p.c;
			forbid.insert(p);
		}

		p.r = h - 1;
		p.c = w - 1;
		fout << recur(p, table, forbid) << endl;
	}
	return 0;
}