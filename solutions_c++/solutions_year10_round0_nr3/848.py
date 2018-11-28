#include <cstdio>
#include <vector>
using namespace std;
typedef vector<int> vint;
typedef long long lint;

int R, K, N;
int G[1 << 10];
vint T;
int Used[1 << 10];

void Solve(int test) {
	T.clear();
	scanf("%d %d %d", &R, &K, &N);
	for(int i = 0; i < N; ++i) {
		scanf("%d", G + i);
		Used[i] = 0;
	}
	int count = 0;
	lint ans = 0;
	int ix = 0;
	for(; R && !Used[ix]; R--) {
		Used[ix] = ++count;
		int s = 0;
		int g = 0;
		while(s + G[ix] <= K && g < N) {
			s += G[ix];
			++ix %= N;
			g++;
		}
		ans += s;
		T.push_back(s);
	}
	for(int i = 1; i < Used[ix]; ++i) {
		T.erase(T.begin());
	}
	lint sum = 0;
	for(int i = 0; i < T.size(); ++i) {
		sum += T[i];
	}
	ans += (lint)R / T.size() * sum;
	R %= T.size();
	for(int i = 0; i < R; ++i) {
		ans += T[i];
	}
	printf("Case #%d: %lld\n", test, ans);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		Solve(i);
	}
	return 0;
}