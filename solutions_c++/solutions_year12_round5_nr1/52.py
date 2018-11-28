#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

struct Level { int p,l,i; };

bool compareLevel (Level i, Level j)
{
  return (i.p * j.l > j.p * i.l);
}

int main()
{
	ifstream fin("a2.txt");
	ofstream fout("a2_sol.txt");

	int t;
	fin >> t;
	for ( int tt = 1; tt <= t; ++tt )
	{
		int n;
		fin >> n;
		vector<Level> l(n);
		for (int i = 0; i < n; ++i ) fin >> l[i].l;
		for (int i = 0; i < n; ++i ) fin >> l[i].p;
		for (int i = 0; i < n; ++i ) l[i].i = i;

		stable_sort(l.begin(), l.end(), compareLevel);

		fout <<"Case #" << tt << ":";
		for (int i = 0; i < n; ++i ) fout << ' ' << l[i].i;
		fout << "\n";
	}

	fin.close();
	fout.close();
}