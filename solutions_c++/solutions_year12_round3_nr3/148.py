#include <stdio.h>
#include <stdlib.h>

#define MAX 128
#define MAXN 10240000

struct NODE {
	long long ans, a, b;
	int next;
}node[MAXN];

int n, m;
long long ln[MAX][2], lm[MAX][2], global_ans;
int mic[MAX][MAX], c;

long long _min(long long a, long long b) {
	if(a < b)return a;
	return b;
}

void fill(int ia, int ib, long long la, long long lb, long long ans) {
	if(ln[ia][1] == lm[ib][1]) {
		long long _m = _min(la, lb);
		node[c].ans = _m + ans;
		node[c].a = la - _m;
		node[c].b = lb - _m;
	} else {
		node[c].ans = ans;
		node[c].a = la;
		node[c].b = lb;
	}

	int s = mic[ia][ib];
	while(s != -1) {
		if(node[c].ans <= node[s].ans && node[c].a <= node[s].a && node[c].b <= node[s].b)return;
		s = node[s].next;
	}

	node[c].next = mic[ia][ib];
	if(node[c].ans > global_ans)
		global_ans = node[c].ans;
	mic[ia][ib] = c;

	//printf("ia:%d ib:%d la:%lld lb:%lld ans:%lld: ans:%lld a:%lld b:%lld\n", ia, ib, la, lb, ans, node[c].ans, node[c].a, node[c].b);

	if(c == MAXN) {
		printf("overflow\n");
	}
	c++;
}

void action() {
	scanf("%d %d", &n, &m);
	for(int i = 1; i <= n; i++)
		scanf("%lld %lld", &ln[i][0], &ln[i][1]);
	for(int i = 1; i <= m; i++)
		scanf("%lld %lld", &lm[i][0], &lm[i][1]);

	for(int i = 0; i <= n; i++)
		for(int j = 0; j <= m; j++)
			mic[i][j] = -1;

	c = 0;
	global_ans = 0;
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= m; j++) {
			//printf("a:%d b:%d\n", i, j);
			int s = mic[i][j - 1];
			while(s != -1) {
				long long a = node[s].a, b = lm[j][0];
				if(lm[j][1] == lm[j - 1][1])
					b += node[s].b;
				fill(i, j, a, b, node[s].ans);
				s = node[s].next;
			}

			s = mic[i - 1][j];
			while(s != -1) {
				long long a = ln[i][0], b = node[s].b;
				if(ln[i][1] == ln[i - 1][1])
					a += node[s].a;
				fill(i, j, a, b, node[s].ans);
				s = node[s].next;
			}

			fill(i, j, ln[i][0], lm[j][0], 0);

			//printf("\n\n");
		}
	}
	printf("%lld", global_ans);
	//printf(" (%d)", c);
	printf("\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		action();
	}
return 0;
}
