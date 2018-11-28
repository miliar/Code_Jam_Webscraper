#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>

#define pb push_back
#define mp make_pair
#define PI 3.14159265358979
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int maxn = 10000010;
int has[maxn] = {};
int tt = 1;
int solve(int a, int b) {
	int ans = 0;
	for (int i = a; i <= b; ++i) {
		int x = i;
		int len = 0;
		int st = 1;
		do {
			x/=10;
			len++;
			st *= 10;
		} while (x);
		st/=10;
		x = i;
		tt++;
		for (int j = 1; j < len; ++j) {
			int cur = x%10;
			x = x/10+st*(cur);
			if (cur != 0 && x >= a && x < i && has[x]!=tt) ans++;
			has[x] = tt;
		}
	}
	return ans;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		int a, b; scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", i+1, solve(a,b));
	}
	return 0;
}