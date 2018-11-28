#include <stdio.h>
#include <string.h>

inline int ABS(int x) {
	return x<0?-x:x;
}

int main(void) {
	int T, cs, i, n;
	scanf("%d", &T);
	for(cs=1;cs<=T;cs++){
		scanf("%d", &n);
		int last[2] = {1, 1};
		int lasttime[2] = {0, 0};
		int prev = -1;
		int prevtime = 0;
		for(i=0;i<n;i++) {
			char x[10];
			int y;
			scanf("%s%d", x, &y);
			int u;
			if(x[0]=='O') u = 0;
			else u = 1;
			lasttime[u] += ABS(last[u] - y) + 1;
			last[u] = y;
			if (prev == u) {
				prevtime = lasttime[u];
			} else {
				if (prevtime >= lasttime[u])
					lasttime[u] = prevtime + 1;
				prev = u;
				prevtime = lasttime[u];
			}
		}
		printf("Case #%d: %d\n", cs, prevtime);
		fprintf(stderr, "Case #%d: %d\n", cs, prevtime);
	}
	return 0;
}
