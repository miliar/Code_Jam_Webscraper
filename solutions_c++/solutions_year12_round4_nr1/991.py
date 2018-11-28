#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <sstream>
#include <queue>
using namespace std;
#define mp make_pair
#define pb push_back
typedef vector<int> vi;
typedef pair<int, int> pii;
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
typedef long long lint;

struct seg {
	lint a, b;
	seg(lint a, lint b) : a(a), b(b) {
	}
};
inline bool operator<(seg x, seg y) {
	return x.a > y.a;
}

priority_queue<seg> S;
int d[10 * 1000 + 5];
int l[10 * 1000 + 5];

void solve(int test) {
	printf("Case #%d: ", test);
	int N;
	scanf("%d", &N);
	for(int i = 0; i < N; i++) {
		scanf("%d %d", d + i, l + i);
	}
	int D;
	scanf("%d", &D);
	while(!S.empty()) S.pop();
	S.push(seg(0, d[0]));
	for(int i = 0; i < N; i++) {
		while(sz(S) && S.top().b < d[i]) {
			S.pop();
		}
		if(!S.empty()) {
			int a = S.top().a;
			if((lint)d[i] + min(l[i], d[i] - a) >= D) {
				puts("YES");
				return;
			}
			S.push(seg(d[i], (lint)d[i] + (min(l[i], d[i] - a))));
		}
	}
	puts("NO");
}

int main() {
#ifdef __LOCAL
	
#else
#endif
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		solve(i + 1);
	}
	return 0;
}
