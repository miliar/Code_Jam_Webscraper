#include <malloc.h>

#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <deque>
#include <list>
#include <string>
#include <cstdlib>
#include <queue>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <assert.h>
#include <stack>
#include <bitset>

//#define debug
//#define ONLINE_JUDGE

#ifndef LOCAL_MACHINE
#define trace(a) void()
#define tracearr(a, b) void()
#else
#include "/home/victor/Dropbox/Public/trace.cpp"
#endif
using namespace std;
#define elif else if
#define sqr(a) ((a)*(a))
#define forn(i,j) for(int i=0;i<int(j);i++)
#define ford(i,j) for(int i=int(j)-1;i>=0;i--)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define all(a) a.begin(),a.end()
#define forin(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define fill_zero(a) memset(a,0,sizeof(a))
#define count botva
#define y1 botven

typedef long long ll;
typedef long double ld;

const string filename("");

int solve (int t) {
	int n, p, s;
	if (scanf("%d%d%d", &n, &s, &p) != 3)
		return 1;
	int a[200];
	forn(i, n)
		if (scanf("%d", a + i) != 1)
			return 0;
	sort(a, a + n);
	reverse(a, a + n);
	int ans = 0;
	forn(i, n) {
		if (a[i] > (p - 1) * 3)
			++ans;
		else if (s && (a[i] >= (p - 2) * 3 + 2 && a[i] >= 2)) {
			++ans;
			--s;
		}
	}
	printf("Case #%d: %d\n", t, ans);
	return 0;
}

int main ()
{
#ifdef LOCAL_MACHINE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int i = 0;
	scanf("%d", &i);
	i = 0;
	while (!solve(++i));
#endif
	return 0;
}

