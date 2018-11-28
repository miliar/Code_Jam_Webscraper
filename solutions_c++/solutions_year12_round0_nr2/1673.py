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
#define maxN 111

int n, sur, p;
int score[maxN], dp[maxN][maxN];

int getSur(int m) {
	if (m < 2 || m >= 29) return -1;
	if (m % 3 == 0) return (m / 3) + 1;
	if (m % 3 == 1) return (m / 3) + 1;
	return (m / 3) + 2;
}

int getNor(int m) {
	if (m < 2) return m;
	if (m % 3 == 0) return m / 3;
	if (m % 3 == 1) return (m / 3) + 1;
	return (m / 3) + 1;
}

int main() {
	#ifndef ONLINE_JUDGE
	//freopen("B-large.in", "r", stdin);
	//freopen("test.out", "w", stdout);
	#endif
	int caseNo, cases = 0;
	for (scanf("%d", &caseNo); caseNo--; ) {
		scanf("%d %d %d", &n, &sur, &p);
		for (int i = 1; i <= n; i++)
			scanf("%d", &score[i]);
		for (int i = 0; i <= n; i++)
			for (int j = 0; j <= sur; j++)
				dp[i][j] = 0;
		int tmpPoint, add;
		for (int i = 1; i <= n; i++) {
			tmpPoint = getSur(score[i]);
			add = (tmpPoint >= p) ? 1 : 0;
			if (tmpPoint != -1) {
				for (int j = 1; j <= sur; j++)
					dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + add);
			}
			tmpPoint = getNor(score[i]);
			add = (tmpPoint >= p) ? 1 : 0;
			for (int j = 0; j <= sur; j++)
				dp[i][j] = max(dp[i][j], dp[i - 1][j] + add);
		}
		printf("Case #%d: %d\n", ++cases, dp[n][sur]);
	}
	return 0;
}

// Copyright (C) 2012, LamPhanViet