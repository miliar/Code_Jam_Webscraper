#include <cstdio>

int W, H, r;

int solve()
{
	int i, j;
	int d[101][101] = {0, };
	int a[101][101] = {0, };
	for(i = 0; i < r; ++i)
	{
		int r, c;
        scanf("%d %d", &r, &c);
		a[r][c] = -1;
	}
    if(a[1][1] != -1) d[1][1] = 1;
	for(i = 1; i <= H; ++i)
		for(j = 1; j <= W; ++j)
		{
			if(i == 1 && j == 1) continue;
			if(a[i][j] == -1) continue;
			int r, c;
            r = i - 2; c = j - 1;
			if(r >= 1 && c >= 1) d[i][j] = (d[i][j] + d[r][c]) % 10007;
			r = i - 1;
			c = j - 2;
			if(r >= 1 && c >= 1) d[i][j] = (d[i][j] + d[r][c]) % 10007;
		}
	return d[H][W];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cs;
	int n;
	scanf("%d", &n);
	for(cs = 1; cs <= n; ++cs)
	{
		scanf("%d %d %d", &H, &W, &r);
		printf("Case #%d: %d\n", cs, solve());
	}
	
	return 0;
}