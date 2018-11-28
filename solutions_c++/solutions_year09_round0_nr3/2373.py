#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iomanip>

#define INF (INT_MAX / 2)
#define X first
#define Y second
#define ft first
#define sc second
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp(a, b) make_pair((a), (b))
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forl(i, n) for(int i = 1; i <= int(n); i++)
#define sqr(a) ((a) * (a))
#define PI 3.1415926535897932384626433832795
#define NMAX 600
#define mod 10000

using namespace std;

typedef pair<int, int> pt;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

int z[NMAX][NMAX];
string s, p("welcome to code jam");

int solve(int i1, int i2)
{
	if(i2 >= (int) p.length())
		return 1;
	if(i1 >= (int) s.length())
		return 0;
	if(z[i1][i2] != -1)
		return z[i1][i2];

	int ans = 0;
	for(int i = i1; i < int(s.length()); i++)
		if(s[i] == p[i2])
			ans = (ans + solve(i + 1, i2 + 1)) % mod;

	return z[i1][i2] = ans;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int N;
	cin >> N;

	getline(cin, s);
	forn(test, N)
	{
		memset(z, -1, sizeof(z));
		getline(cin, s);
		printf("Case #%d: %04d\n", test + 1, solve(0, 0) % mod);
	}

    return 0;
}