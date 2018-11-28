//============================================================================
// Author       : LAM PHAN VIET - lamphanviet@gmail.com
// Problem Name : 
// Time Limit   : .000s
// Description  : 
//============================================================================
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a) | (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 555

int n, a[maxN], m;
map<int, int> idx;
vector< vi > v;

int getIndex(int sum) {
	int id = idx[sum];
	if (id == 0) {
		id = idx[sum] = ++m;
		v.pb(vi());
	}
	return id;
}

void printSet(int x) {
	bool space = false;
	rep(i, n)
		if (x & BIT(i)) {
			if (space) putchar(' '); space = true;
			printf("%d", a[i]);
		}
	puts("");
}

bool solve() {
	int x, y;
	fr(i, 1, v.size() - 1) {
		rep(j, v[i].size()) {
			x = v[i][j];
			fr(k, j + 1, v[i].size() - 1) {
				y = v[i][k];
				if ((x & y) == 0) {
					printSet(x);
					printSet(y);
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	#ifndef ONLINE_JUDGE
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		idx.clear();
		v.resize(1); m = 0;
		scanf("%d", &n);
		rep(i, n) scanf("%d", &a[i]);
		fr(i, 1, BIT(n) - 1) {
			int sum = 0;
			rep(j, n) if (i & BIT(j))
				sum += a[j];
			int id = getIndex(sum);
			v[id].pb(i);
		}
		printf("Case #%d:\n", ++caseNo);
		if (!solve()) puts("Impossible");
	}
	return 0;
}

// Copyright (C) 2012, LamPhanViet