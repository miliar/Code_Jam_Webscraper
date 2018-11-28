#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

#define QMAX 1002
#define NMAX 102
#define INF 1000000

int d[QMAX][NMAX];
string name[NMAX];
map<string, int> num;

void solve(int tc)
{
	int q, s;
	string t;
	num.clear();
	getline(cin, t);
	s = atoi(t.c_str());
	forn(i, s)
	{
		getline(cin, name[i]);		
	}
	getline(cin, t);
	q = atoi(t.c_str());
	forn(i, q + 1) forn(j, s) d[i][j] = INF;
	forn(i, s) d[0][i] = 0;
	forn(i, q)
	{
		getline(cin, t);
		forn(j, s)
		{
			if (d[i][j] == INF) continue;
			forn(k, s)
			{
				if (name[k] == t) continue;
				d[i + 1][k] = min(d[i + 1][k], d[i][j] + int(j != k));
			}
		}
	}	
	int ans = INF;
	forn(i, s) ans = min(ans, d[q][i]);
	printf("Case #%d: %d\n", tc, ans);
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc;
	scanf("%d\n", &tc);
	forn(it, tc) solve(it + 1);
	return 0;
}
         	
