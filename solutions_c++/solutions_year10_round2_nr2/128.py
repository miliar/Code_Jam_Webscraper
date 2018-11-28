#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
#include <queue>
#include <set>
#include <map>
#include <string>
using namespace std;
typedef vector<int> vint;
typedef long long lint;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()

int N, K, B, T;

vint X;
vint V;

void Solve(int test) {
	scanf("%d %d %d %d", &N, &K, &B, &T);
	X.clear();
	V.clear();
	for(int i = 0; i < N; ++i) {
		int x;
		scanf("%d", &x);
		X.pb(x);
	}
	for(int i = 0; i < N; ++i) {
		int v;
		scanf("%d", &v);
		V.pb(v);
	}
	int run = 0;
	int lose = 0;
	int ans = 0;
	for(int i = N - 1; run < K && i >= 0; --i) {
		int dist = B - X[i];
		if((lint)T * V[i] >= dist) {
			run++;
			ans += lose;
		}
		else {
			lose++;
		}
	}
	if(run < K) {
		printf("Case #%d: IMPOSSIBLE\n", test);
	}
	else {
		printf("Case #%d: %d\n", test, ans);
	}

}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		Solve(i);
	}
	return 0;
}