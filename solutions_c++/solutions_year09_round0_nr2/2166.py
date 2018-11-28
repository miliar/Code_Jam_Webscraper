#include <cstdio>
#include <cstring>
#define W 100
#define H 100
struct node {
	int r, c;
}q[W * H];
int h, w;
int mp[H][W], ans[H][W], idx;
int dr[4] = {-1, 0, 0, 1};
int dc[4] = {0, -1, 1, 0};
void bfs(int r, int c) {
	int head, tail, i, rr, cc;
	head = tail = 0;
	q[head].r = r;
	q[head].c = c;
	while (head <= tail) {
		int mini = -1, mn = 10000;
		for (i = 0; i < 4; ++i) {
			rr = q[head].r + dr[i];
			cc = q[head].c + dc[i];
			if (rr >= 0 && rr < h && cc >= 0 && cc < w && mp[rr][cc] < mp[q[head].r][q[head].c] && mn > mp[rr][cc]) {
				mini = i;
				mn = mp[rr][cc];
			}
		}
		if (mini >= 0) {
			rr = q[head].r + dr[mini];
			cc = q[head].c + dc[mini];
			tail++;
			q[tail].r = rr;
			q[tail].c = cc;
			if (ans[rr][cc] >= 0)
				break;
		}
		head++;
	}
	int mark;
	if (ans[q[tail].r][q[tail].c] >= 0)
		mark = ans[q[tail].r][q[tail].c];
	else
		mark = idx++;
	for (i = 0; i <= tail; ++i)
		ans[q[i].r][q[i].c] = mark;
}
int main ()
{
	int t, i, j, k;
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; ++i) {
		scanf("%d%d", &h, &w);
		for (j = 0; j < h; ++j)
			for (k = 0; k < w; ++k)
				scanf("%d", &mp[j][k]);
		memset(ans, -1, sizeof(ans));
		idx = 0;
		for (j = 0; j < h; ++j)
			for (k = 0; k < w; ++k)
				if (ans[j][k] < 0) {
					bfs(j, k);
				}
		printf("Case #%d:\n", i);
		for (j = 0; j < h; ++ j) {
			for (k = 0; k < w - 1; ++ k)
				printf("%c ", (ans[j][k] + 'a'));
			printf("%c\n", (ans[j][w - 1] + 'a'));
		}
	}
}
