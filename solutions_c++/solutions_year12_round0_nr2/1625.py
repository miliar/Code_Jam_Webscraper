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
const int maxn = 110;
int a[maxn] = {};
int getval(int x, int p) {
	int m1 = x/3;
	if (x%3) m1++;
	
	int res = 0;
	if (m1 >= p) res |= 1;
	if (x>=2&&x<=28) {
		int m2 = x/3+1;
		if (x%3 == 2) m2++;
		if (m2 >= p) res |= 2;
	}
	return res;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; scanf("%d", &T);
	for (int ttt = 0; ttt < T; ++ttt) {
		int n, s, p; scanf("%d%d%d", &n, &s, &p);
		int cnt[5] = {};
		for (int i = 0; i < n; ++i) scanf("%d", &a[i]), cnt[getval(a[i],p)]++;
		int best = 0;
		for (int i = 0; i <= s; ++i) {
			if (cnt[2] < i) continue;
			if (n-cnt[2] < s-i) continue;
			int curans = i+cnt[3];
			int rem = n-cnt[2]-(s-i);
			rem = min(rem,cnt[1]);
			curans += rem;
			if (curans > best) best = curans;
		}
		printf("Case #%d: %d\n", ttt+1, best);
	}
	return 0;
}