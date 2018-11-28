//#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment (linker, "/STACK:100000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 2147483647;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

int n, s, q;

int d[100][1000];
string eng[100], que[1000];

int get(int cur, int pos) {
	if (pos == q) return 0;
	if (cur != -1 && d[cur][pos] != -1) return d[cur][pos];

	int mi = INF;
	forn(i, s) {
		if (que[pos] == eng[i]) continue;
		if (i == cur) mi = min(mi, get(cur, pos + 1));else
		mi = min(mi, 1 + get(i, pos + 1));
	}

	if (cur != -1) d[cur][pos] = mi;
	return mi;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	

	cin >> n;
	forn(i, n) {
		memset(d, 255, sizeof(d));
		scanf("%d\n", &s);
		forn(j, s) {
			getline(cin, eng[j]);
		}
		scanf("%d\n", &q);
		forn(j, q) {
			getline(cin, que[j]);
		}
		printf("Case #%d: %d\n", i + 1, max(0, get(-1, 0) - 1));
	}


	return 0;
}

 
