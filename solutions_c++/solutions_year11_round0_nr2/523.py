#include<cstdio>
#include<cstring>

int C, D, N;
char c[50][5], d[50][50], s[111];
char stk[111];
int top;

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &C);
		for (int i = 0; i < C; ++i)
			scanf("%s", c[i]);
		scanf("%d", &D);
		for (int i = 0; i < D; ++i)
			scanf("%s", d[i]);
		scanf("%d", &N);
		scanf("%s", s);
		printf("Case #%d: ", tt);
		top = 0;
		stk[0] = '*';
		for (int i = 0; i < N; ++i) {
			stk[++top] = s[i];
			for (int j = 0; j < C; ++j)
				if (stk[top] == c[j][0] && stk[top - 1] == c[j][1] 
				|| stk[top] == c[j][1] && stk[top - 1] ==c[j][0]) {
					stk[--top] = c[j][2]; break;
				}
			for (int j = 0; j < D && top; ++j)  
				for (int k = 1; k < top; ++k)
					if (stk[k] == d[j][0] && stk[top] == d[j][1] ||
					stk[top] == d[j][0] && stk[k] == d[j][1]) {
					top = 0; break;
				}
		}
		printf("[");
		if (top > 0) printf("%c", stk[1]);
		for (int i = 2; i <= top; ++i) 
			printf(", %c", stk[i]);
		printf("]\n");
	}
	return 0;
}

