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
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 105

string a[NMAX];
double wp[NMAX], owp[NMAX], oowp[NMAX];
int n;

double calc_wp(int i, int f = -1)
{
	double ret = 0;	
	int cnt = 0;
	forn(j, n)
	{
		if (j == f) continue;
		if (a[i][j] == '1') ret++;
		if (a[i][j] != '.') cnt++;
	}

	ret /= cnt;

	return ret;
}

void solve(int tc)
{
	printf("Case #%d:\n", tc);
	cin >> n;
	forn(i, n)
	{
		cin >> a[i];

		wp[i] = calc_wp(i);
	}

	forn(i, n)
	{
		owp[i] = 0.0;
		int cnt = 0;

		forn(j, n)
		{
			if (a[i][j] == '.') continue;
			owp[i] += calc_wp(j, i);
			cnt++;
		}
		
		owp[i] /= cnt;
	}

	forn(i, n)
	{
		oowp[i] = 0.0;
		int cnt = 0;

		forn(j, n)
		{
			if (a[i][j] == '.') continue;
			oowp[i] += owp[j];
			cnt++;
		}
		
		oowp[i] /= cnt;
	}

	forn(i, n)
	{
		printf("%.10lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
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
            
