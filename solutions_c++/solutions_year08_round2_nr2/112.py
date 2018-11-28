#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a)

vi factor(int n) {
	vi res;
	for (int i =2; i*i <= n; ++i) {
		if (n%i == 0) {
			res.push_back(i);
			while (n%i==0) n/=i;
		}
	}
	if (n > 1) res.push_back(n);
	return res;
}

int common(vi &a, vi &b)
{
	vi res(min(a.size(),b.size()),0);
	vi::iterator it = set_intersection(a.begin(), a.end(), b.begin(), b.end(), res.begin());
	if (it-res.begin() > 0) return *(it-1);
	return -1;
}

int main()
{
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	//ifstream fin("B-large.in");
	//ofstream fout("B-large.out");

	int c, a, b ,p;

	fin >> c;

	for (int tc = 1; tc <= c; ++tc)
	{

		fin >> a >> b >> p;
		vi g(b+1);
		vector <vi> f(b+1);

		FOR(i,a,b+1) {
			g[i] = i;
			f[i] = factor(i);
		}

		bool joined = true;
		while (joined)
		{
			joined = false;
			FOR(i,a,b+1) FOR(j,i+1,b+1) if (g[i] != g[j]) {
				if (common(f[i], f[j]) >= p) {
					int z = min(g[i], g[j]), q = max(g[i], g[j]);
					FOR(k,a,b+1) if (g[k] == q) g[k] = z;
					joined = true;
				}
			}
		}

		set <int> s;
		FOR(k,a,b+1) s.insert(g[k]);

		fout << "Case #" << tc << ": " << s.size() << endl;

	}



	fin.close();
	fout.close();

	return 0;
}

