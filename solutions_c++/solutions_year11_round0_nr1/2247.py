#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int cas = 1; cas <= cases; cas++) {
		int n, i;
		scanf("%d", &n);
		char buf[10];
		int pos[200], num[200];
		for (i = 0; i < n; i++) {
			scanf("%s%d", buf, &pos[i]);
			if (buf[0] == 'B') num[i] = 0;
			else num[i] = 1;
		}
		int t[2], p[2];
		t[0] = t[1] = 0;
		p[0] = p[1] = 1;
		for (i = 0; i < n; i++) {
			t[num[i]] += 1 + abs(p[num[i]] - pos[i]);
			if (t[num[i]] <= t[1 - num[i]]) t[num[i]] = t[1 - num[i]] + 1;
			p[num[i]] = pos[i];
		}
		int tot = t[0];
		if (t[1] > tot) tot = t[1];
		printf("Case #%d: %d\n", cas, tot);
	}
	return 0;
}
