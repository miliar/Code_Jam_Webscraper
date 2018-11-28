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

int n, m, A;

bool good(int A, int& p, int& q)
{
	for (p = n; p > 0; p--)
	{
		if (A % p) continue;
		q = A / p;
		if (q <= m)
		{
			return true;
		}
	}
	return false;
}

void solve(int tc)
{
	cerr << tc << endl;	
	printf("Case #%d: ", tc);
	cin >> n >> m >> A;
	if (A > n * m)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	int a, b;
	for (int c = 0; c <= n; c++)
	{
		for (int d = 0; d <= m; d++)
		{
			if (good(A + c * d, a, b))
			{
				printf("0 0 %d %d %d %d\n", a, d, c, b);
				return;
			}
		}
	}
	cerr << "Boroda" << endl;
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc;
	cin >> tc;
	forn(it, tc) solve(it + 1);
	return 0;
}
         	
