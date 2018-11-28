#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 3000;

int casei, cases, n;
int hh[maxn];
int ans[maxn];

int t1, t2, h1, h2;
double d;

bool process(int l, int r) {
	//printf("process: %d %d\n", l, r);
	//ans[l] = height;
	while (l < r) {
		if (hh[l] > r) {
			//printf("FALSE! %d hh=%d\n", l, hh[l]);
			return false;
		}
		//if (hh[l] != r) ans[hh[l]] = height;
		if (hh[l] > l + 1) 
			if (!process(l + 1, hh[l])) {
				//printf("");
				return false;
			}
		l = hh[l];
	}
	return true;
}

void calc(int now) {
	if (ans[hh[now]] == -1) calc(hh[now]);
	h1 = ans[hh[now]];
	h2 = ans[hh[hh[now]]];
	t1 = hh[now] - now;
	t2 = hh[hh[now]] - hh[now];
	d = h1 - (t1 + 0.0)/t2*(h2 - h1);
	ans[now] = ((int)d) - 1;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d", &n);
		for (int i = 1; i < n; ++i) scanf("%d", hh + i);
		
		
		if (!process(1, n)) printf("Case #%d: Impossible\n", casei);
		else {
			memset(ans, 255, sizeof ans);
			ans[n] = 999999999;
			hh[n] = n + 1;
			ans[n + 1] = ans[n];
			for (int i = 1; i < n; ++i) if (ans[i] == -1) calc(i);
			printf("Case #%d:", casei);
			for (int i = 1; i <= n; ++i) printf(" %d", ans[i]);
			printf("\n");
		}
	}

	return 0;
}
