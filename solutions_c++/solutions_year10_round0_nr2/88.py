#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <ctime>
using namespace std;

int R, k;
int g[1000], N;
long long rans[1100000];
int mk[1000];

int next(int i) {
	i++;
	return i == N ? 0 : i;
}

void solve() {
	scanf("%d %d %d", &R, &k, &N);
	long long tmp = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &g[i]);
		tmp += g[i];
	}

	if (tmp <= (long long)k) {
		printf("%lld\n", (long long)R * tmp);
		return;
	}
	memset(mk, -1, sizeof mk);

	long long ans = 0;
	long long rep = 0;
	long long sum = 0;
	int pot = -1;
	int t = 0;

	mk[0] = 0;
	for (int i = 0; ;i = next(i)) {
		sum += g[i];
		if (sum > k) {
			rep += sum - g[i];
			sum = g[i];
			rans[++t] = rep;

			if (mk[i] != -1) {
				pot = mk[i];
				rep -= rans[pot];
				break;
			}
			mk[i] = t;
		}
	}
	if (R <= pot) {
		ans = rans[pot];
	} else {
		R -= pot;
		int mod = t - pot;
		ans += (long long)((int)(R / mod)) * rep + rans[R % mod + pot];
	}
	printf("%lld\n", ans);
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}t