#include <stdio.h>
#include <stdlib.h>

#define MAXN 128

struct TIME
{
	int s, e;
}data[2][MAXN];

int sort_function(const void *a, const void *b) {
	if(((TIME *)a)->s > ((TIME *)b)->s)return 1;
	if(((TIME *)a)->s < ((TIME *)b)->s)return -1;
	if(((TIME *)a)->e > ((TIME *)b)->e)return 1;
	if(((TIME *)a)->e < ((TIME *)b)->e)return -1;
	return 0;
}

int readtime() {
	int h, m;

	scanf("%d:%d", &h, &m);

	return h * 60 + m;
}

void find_ans(int Case) {
	int i, j, c[2], next;
	int t, n[2];
	int ans[2], min[MAXN][2];

	scanf("%d", &t);
	scanf("%d %d", &n[0], &n[1]);
	for(i = 0; i < 2; i++)
		for(j = 0; j < n[i]; j++) {
			data[i][j].s = readtime();
			data[i][j].e = readtime();
		}
	qsort((void *)data[0], n[0], sizeof(data[0][0]), sort_function);
	qsort((void *)data[1], n[1], sizeof(data[1][0]), sort_function);

	ans[0] = 0;
	ans[1] = 0;
	for(c[0] = 0, c[1] = 0; c[0] < n[0] || c[1] < n[1]; ) {
		if((c[0] < n[0] && data[0][c[0]].s < data[1][c[1]].s) || c[1] == n[1]) {
			next = 0;
		} else {
			next = 1;
		}
		for(i = 0; i < ans[0] + ans[1]; i++) {
			if(min[i][1] == next)
				if(min[i][0] + t <= data[next][c[next]].s) {
					min[i][0] = data[next][c[next]].e;
					min[i][1] = next ^ 1;
					break;
				}
		}
		if(i == ans[0] + ans[1]) {
			min[ans[0] + ans[1]][0] = data[next][c[next]].e;
			min[ans[0] + ans[1]][1] = next ^ 1;
			ans[next]++;
		}
		c[next]++;
	}

	printf("Case #%d: %d %d\n", Case, ans[0], ans[1]);
}

int main(int argc, char *argv[])
{
	int c, n;

	scanf("%d", &n);
	for(c = 1; c <= n; c++) {
		find_ans(c);
	}

	return 0;
}
