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
#define ONLINE_JUDGE

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

int a[26][26];
bool d[26][26];
int s[310];
int n;

bool getdata () {
	int k;
	if (scanf("\n%d ", &k) != 1)
		return 0;
	char x, y, z;
	memset(a, -1, sizeof a);
	memset(d, 0, sizeof d);
	forn(i, k) {
		if (scanf("%c%c%c ", &x, &y, &z) != 3)
			return 0;
		trace(x - 'A');
		trace(y - 'A');
		trace(z - 'A');
		a[x - 'A'][y - 'A'] = a[y - 'A'][x - 'A'] = z - 'A';
	}
	if (scanf("%d ", &k) != 1)
		return 0;
	forn(i, k) {
		if (scanf("%c%c ", &x, &y) != 2)
			return 0;
		d[x - 'A'][y - 'A'] = d[y - 'A'][x - 'A'] = 1;
	}
	if (scanf("%d ", &n) != 1)
		return 0;
	forn(i, n) {
		if (scanf("%c", &x) != 1)
			return 0;
		s[i] = x - 'A';
	}
	return 1;
}

bool solve (const int &t) {
	trace(a);
	vector <int> cmb;
	forn(i, n) {
		trace(cmb);
		if (!cmb.empty() && a[s[i]][cmb.back()] >= 0)
			cmb.back() = a[s[i]][cmb.back()];
		else
			cmb.pb(s[i]);
		forn(i, cmb.size() - 1)
			if (d[cmb[i]][cmb.back()]) {
				cmb.clear();
				break;
			}
	}
	trace(cmb);
	printf("Case #%d: [", t);
	forn(i, cmb.size() - 1)
		printf("%c, ", cmb[i] + 'A');
	if (!cmb.empty())
		printf("%c]\n", cmb.back() + 'A');
	else
		puts("]");
	trace("-------------------");
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

