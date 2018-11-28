#include <stdio.h>
#include <string.h>

int n, m;
int step = 1000;
int a[1000000], ct[1000], remain;

int move(int cur, int t) {
	while (a[cur] >= 0) {
		cur++;
		if (cur == n) cur = 0;
	}
	t %= remain;
	if (t == 0) t = remain;
	if (!t) return cur;
	while (1) {
		if (cur % step == 0) break;
		if (a[cur] < 0) {
			t--;
			if (!t) return cur;
		}
		cur++;
		if (cur == n) cur = 0;
	}
	while(1) {
		if (ct[cur/step] >= t) break;
		t -= ct[cur/step];
		cur += step;
		if (cur >= n) cur = 0;
	}
	while(1) {
		if (a[cur] < 0) {
			t--;
			if (!t) return cur;
		}
		cur++;
	}
}

int main() {
	int i, j;
	int testcases, r, cur;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d", &testcases);
	for (r = 1; r <= testcases; r++) {
		printf("Case #%d:", r);
		scanf("%d%d",&n,&m);
		memset(a, 0xff, sizeof(a));
		cur = 0;
		remain = n;
		i = j = 0;
		while(j < n) {
			if (j + step <= n) ct[i] = step;
			else ct[i] = n - j;
			i++;
			j+=step;
		}
		for (i = 1; i <= n; i++) {
			cur = move(cur, i);
			a[cur] = i;
			ct[cur/step]--;
			remain--;
		}
		for (i = 0; i < m; i++) {
			scanf("%d",&j);
			printf(" %d",a[j-1]);
		}
		printf("\n");
	}
	return 0;
}
