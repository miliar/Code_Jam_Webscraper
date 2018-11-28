#include <stdio.h>
#include <memory.h>
#include <string.h>

char buf[1005];
char buf2[1005];
int per[5];
int mark[5];
int n, times, len;

int cal(int depth)
{
	int i, j;

	if (depth == n) {
		for (i = 0; i < times; i++) {
			char *ptr = buf + i * n;
			char *ptr2 = buf2 + i * n;
			for (j = 0; j < n; j++) {
				ptr2[j] = ptr[per[j]];
			}
		}
		int rlt = 1;
		char last = buf2[0];
		for (i = 1; i < len; i++) {
			if (buf2[i] != last) {
				last = buf2[i];
				rlt++;
			}
		}
		return rlt;
	}

	int rlt = -1;
	for (i = 0; i < n; i++) {
		if (mark[i] == 0) {
			mark[i] = 1;
			per[depth] = i;
			int t = cal(depth + 1);
			if (rlt == -1 || t < rlt) {
				rlt = t;
			}
			mark[i] = 0;
		}
	}
	return rlt;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int cs, k;
	scanf("%d", &cs);
	for (k = 1; k <= cs; k++) {
		scanf("%d", &n);
		gets(buf);
		gets(buf);
		len = strlen(buf);
		times = len / n;
		memset(mark, 0, sizeof (mark));
		printf("Case #%d: %d\n", k, cal(0));
	}

	return 0;
}