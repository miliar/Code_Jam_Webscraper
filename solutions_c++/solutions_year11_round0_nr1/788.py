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
int a[1010];

bool getdata () {
	if (scanf("\n%d", &n) != 1)
		return 0;
	forn(i, n) {
		char c;
		if (scanf(" %c %d", &c, a + i) != 2)
			return 0;
		if (c == 'B')
			a[i] = -a[i];
	}
	return 1;
}

bool solve (const int &t) {
	a[n] = 0;
	trace(n);
	trace(a);
	int o, b, ot, bt, op, bp; //a[o] > 0, a[b] < 0
	o = b = -1;
	while (a[++o] < 0);
	while (a[++b] > 0);
	ot = bt = 0;
	op = bp = 1;
	while (o < n || b < n) {
		if (o < b) {
			ot += abs(op - a[o]);
			ot = max(ot, bt) + 1;
			op = a[o];
			while (a[++o] < 0);
		} else {
			bt += abs(bp + a[b]);
			bt = max(ot, bt) + 1;
			bp = -a[b];
			while (a[++b] > 0);
		}
	}
	printf("Case #%d: %d\n", t, max(ot, bt));
	return 1;
}

int main ()
{
	int t = 0;
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	scanf("%d", &t);
	forn(i, t) {
		getdata();
		solve(i + 1);
	}
	return 0;
}

