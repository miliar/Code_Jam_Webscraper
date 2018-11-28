#include <cstdio>


int tt, T, n;
int v[105][2];
int A[105], B[105];

void work()
{
	int ans = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		char ch;
		do {
			scanf("%c", &ch);
		} while (ch != 'O' && ch != 'B');
		v[i][0] = (ch == 'B');
		scanf("%d", &v[i][1]);
	}
	A[0] = B[0] = 0;
	for (int i = 1; i <= n; ++i)
		if (v[i][0] == 0)
			A[++A[0]] = i;
		else
			B[++B[0]] = i;
	int p = 1, q = 1;
	int c = 1, d = 1, finished = 0;
	while (p <= A[0] || q <= B[0]) {
		int tfinished = finished;
		if (p <= A[0]) {
			int goal = v[A[p]][1];
			if (c == goal && tfinished == A[p] - 1) {
				//printf("A press\n");
				finished = A[p];
				++p;
			} else if (c != goal) {
				//printf("A move\n");
				if (c > goal) --c; else ++c;
			}
		}
		if (q <= B[0]) {
			int goal = v[B[q]][1];
			if (d == goal && tfinished == B[q] - 1) {
				//printf("B press\n");
				finished = B[q];
				++q;
			} else if (d != goal) {
				//printf("B move\n");
				if (d > goal) --d; else ++d;
			}
		}
		//printf("\n");
		++ans;
	}
	printf("Case #%d: %d\n", tt, ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; ++tt) work();
}