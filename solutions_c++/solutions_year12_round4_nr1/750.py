#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
#define maxn 10010
long long d[maxn], l[maxn], f[maxn];
long long D;
int T, n;
int main() {
	freopen("r", "r", stdin);
	int cas;
	cin >> cas;
	for (int cc = 1; cc <= cas; cc++) {
		memset(f, 0, sizeof(f));
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lld %lld", &d[i], &l[i]);
		scanf("%lld", &D);
		f[0] = d[0];
		for (int i = 0; i < n; ++i) {
			long long tmp = d[i] + f[i];
			for (int j = i + 1; j < n && tmp >= d[j]; j++) {
				f[j] = max(f[j], min(d[j] - d[i], l[j]));
			}
		}
		bool flag = false;
		for (int i = n - 1; i >= 0; --i) {
			if (d[i] + f[i] >= D) {
				flag = true;
				break;
			}
		}
		if (flag)
			printf("Case #%d: YES\n", cc);
		else
			printf("Case #%d: NO\n", cc);
	}
	return 0;
}

