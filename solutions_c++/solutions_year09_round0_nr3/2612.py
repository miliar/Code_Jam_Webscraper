#include <cstdio>
#include <cstring>

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	char *q = "welcome to code jam", s[505];
	int i, j, T, W = strlen(q), N, cn[505][20];
scanf("%d", &T);
getchar();
for (int t = 0; t < T; ++t)
{
	gets(s);
	N = strlen(s);
	memset(cn, 0, sizeof cn);
	cn[0][0] = s[0] == q[0];
	for (i = 1; i < N; ++i)
	{
		cn[i][0] = (cn[i-1][0] + (s[i] == q[0])) % 10000;
		for (j = 1; j < W; ++j) cn[i][j] = (cn[i-1][j] + (s[i] == q[j]) * cn[i-1][j-1]) % 10000;
	}
#define RET cn[N-1][W-1]
	printf("Case #%d: %d%d%d%d\n", t+1, RET / 1000, RET / 100 % 10, RET / 10 % 10, RET % 10);	
}
	return 0;
}
