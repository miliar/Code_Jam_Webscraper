#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

typedef long double ld;
typedef long long ll;
const double pi = M_PI;

const int NMAX = 45;

string a[NMAX];

void solve(int tc)
{
	printf("Case #%d: ", tc);
	int n; scanf("%d\n", &n);
	forn(i, n) getline(cin, a[i]);
	vector<int> v(n, n-1);
	forn(i, n)
	{
		while (v[i] >= 0 && a[i][v[i]] == '0') v[i]--;
	}

	int ans = 0;
	forn(i, n)
	{
		int j = i; 
		while (v[j] > i) j++;
		while (j > i)
		{
			ans++;
			swap(v[j], v[j-1]);
			j--;
		}
	}
	printf("%d\n", ans);
}	

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; cin >> tc;
	forn(it, tc) solve(it+1);

	return 0;
}