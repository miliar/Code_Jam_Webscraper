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

#ifdef ONLINE_JUDGE
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

int n;
int a[10000];

bool getdata () {
	if (scanf("%d", &n) != 1)
		return 0;
	forn(i, n)
		if (scanf("%d", a + i) != 1)
			return 0;
	return 1;
}

bool solve (const int &t) {
	int ans = 0;
	forn(i, n)
		ans += a[i] != i + 1;
	printf("Case #%d.00: %d\n", t, ans);
	return 1;
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	forn(i, t) {
		getdata();
		solve(i + 1);
	}
	return 0;
}

