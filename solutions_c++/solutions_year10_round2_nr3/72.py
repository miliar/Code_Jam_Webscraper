#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <cassert>
#include <cmath>
#include <deque>
#include <sstream>
using namespace std;
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define only(v) v.erase(unique(all(v)), v.end())
typedef  vector<int> VI;
typedef  pair<int, int> pii;
typedef vector<string> VS;
#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
const int NMAX = 505;
const long long MOD = 100003;
long long c[NMAX][NMAX], a[NMAX][NMAX];

void precalc() 
{
	forn(i, NMAX)
	{
		c[0][i] = c[i][i] = 1;
		for(int j = 1; j < i; j++)
		{
			c[j][i] = (c[j-1][i-1] + c[j][i-1]) % MOD;
		}
	}
	for1(i, NMAX-2) a[1][i+1] = 1;
	for(int k = 2; k < NMAX; k++)
	{
		for(int n = k + 1; n < NMAX; n++)
		{
			a[k][n] = 0;
			for(int i = 0; i < min(k-1, n-k); i++)
			{
				a[k][n] += (c[i][n-k-1] * a[k - i - 1][k]) % MOD;
			}
		}
	}
}

void solve(int tc)
{
	int n; cin >> n;
	long long ans = 0;
	for1(k, n-1)
	{
		ans += a[k][n];
	}
	ans %= MOD;
	cout << "Case #" << tc << ": " << ans << endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
#endif
	precalc();
	int tc; cin >> tc;
	forn(i, tc) solve(i+1);

	return 0;
}
