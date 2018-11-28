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

#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define REP(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
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
#define maxN 2000002

const int x[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };
vi adj[maxN];

int getLength(int n) {
	if (n == 0) return 1;
	int res = 0;
	while (n) res++, n /= 10;
	return res;
}

void preCal() {
	int len, back, front, tmp;
	for (int i = 10; i < maxN; i++) {
		set<int> mySet;
		len = getLength(i);
		for (int j = 1; j < len; j++) {
			back = i % x[j];
			front = i / x[j];
			tmp = back * x[len - j] + front;
			if (tmp > i && getLength(tmp) == len)
				mySet.insert(tmp);
		}
		foreach(it, mySet) adj[i].pb(*it);
	}
}

int main() {
	#ifndef ONLINE_JUDGE
	//freopen("C-large.in", "r", stdin);
	//freopen("test.out", "w", stdout);
	#endif
	preCal();
	int caseNo, cases = 0, a, b;
	for (scanf("%d", &caseNo); caseNo--; ) {
		int res = 0;
		scanf("%d %d", &a, &b);
		for (int i = a; i <= b; i++) {
			int lo = 0, hi = adj[i].size() - 1, pos = -1;
			while (lo <= hi) {
				int mid = (lo + hi) >> 1;
				if (adj[i][mid] <= b) {
					pos = mid;
					lo = mid + 1;
				}
				else hi = mid - 1;
			}
			res += pos + 1;
		}
		printf("Case #%d: %d\n", ++cases, res);
	}
	return 0;
}

// Copyright (C) 2012, LamPhanViet