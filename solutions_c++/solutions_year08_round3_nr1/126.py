#include <iostream>
#include <cstdio>
#include <algorithm>
#include <functional>
#include <vector>
using namespace std;

int a[1024];

int main()
{
	int N, K, P, L;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d", &N);
	for (int cas = 1; cas <= N; ++cas) {
		scanf("%d %d %d", &P, &K, &L);
		for (int i = 0; i < L; ++i)
			scanf("%d", &a[i]);
		sort(a,a+L);
		long long ans = 0, ind = 0, t = 1;
		for (int i = L-1; i >= 0; --i) {
			ans += a[i]*t;
			ind++;
			if (ind == K) {
				ind = 0;
				t++;
			}
		}
		printf("Case #%d: %lld\n", cas, ans);
	}
	return 0;
}

