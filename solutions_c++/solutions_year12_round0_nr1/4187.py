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

char trans[26];

void init () {
	memset(trans, -1, sizeof trans);
	int n;
	freopen("info.txt", "rt", stdin);
	scanf("%d\n", &n);
	trace(n);
	forn(i, n) {
		string s1, s2;
		getline(cin, s1);
		getline(cin, s2);
		forn(i, s1.size())
			if (s1[i] >= 'a' && s1[i] <= 'z')
				trans[s1[i] - 'a'] = s2[i];
	}
	trans['z' - 'a'] = 'q';
	trans['q' - 'a'] = 'z';
	forn(i, 26)
		trace(trans[i]);
}

const string filename("");

int solve (int t) {
	string s;
	if (!getline(cin, s))
		return 1;
	forn(i, s.size())
		if (s[i] >= 'a' && s[i] <= 'z')
			s[i] = trans[s[i] - 'a'];
	printf("Case #%d: %s\n", t, s.data());
	return 0;
}

int main ()
{
	init();
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int i = 0;
	scanf("%d\n", &i);
	i = 0;
	while (!solve(++i));
	return 0;
}

