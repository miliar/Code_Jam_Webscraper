#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

const int h = 10101;

int T, n, x;
int a[h];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d", &n);
		for (int i = 0; i < h; i++)
			a[i] = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &x);
			a[x] ++;
		}
		int ans = h;
		for (int i = 0; i < h; i++) {
			if (a[i]) {
				int j;
				for (j = i; j+1 < h && a[j] <= a[j+1]; j++);
				for (int k = i; k <= j; k++)
					a[k] --;
				ans = min(ans, j - i + 1);
				i--;
			}
		}
		if (ans == h)
			ans = 0;
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}