#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct Rope {
	int a, b;
};

bool comp(Rope& x, Rope& y)
{
	return x.a < y.a;
}

Rope r[1000];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, N;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d", &N);
		for (int j = 0; j < N; ++j) {
			scanf("%d%d", &(r[j].a), &(r[j].b));
		}
		int ans = 0;
		sort(r, r + N, comp);
		for (int j = 0; j < N - 1; ++j) {
			for (int k = j + 1; k < N; ++k) {
				if (r[j].b > r[k].b) ++ans;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}