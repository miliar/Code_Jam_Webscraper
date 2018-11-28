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

int n, m;
string a[100];

int getdata () {
	if (scanf("%d %d\n", &n, &m) != 2)
		return 0;
	forn(i, n)
		if (!getline(cin, a[i]))
			return 0;
	return 1;
}

bool solve (int t) {
	printf("Case #%d:\n", t);
	forn(i, n)
		forn(j, m)
			if (a[i][j] == '#') {
				forn(k, 4)
					if (i + 1 == n || j + 1 == m || a[i + (k & 1)][j + (k >> 1)] != '#') {
						puts("Impossible");
						return 1;
					}
				a[i][j] = a[i + 1][j + 1] = '/';
				a[i][j + 1] = a[i + 1][j] = '\\';
			}
	forn(i, n)
		puts(a[i].data());
	return 1;
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d\n", &t);
	forn(i, t)
		cerr << getdata(), solve(i + 1);
	return 0;
}

