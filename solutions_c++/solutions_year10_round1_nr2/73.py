#include<cstdio>
#include<cstring>

int f[100][256];
int a[100];
int D,I,M,n;

int abs(int x)
{
	if (x < 0) return -x; else return x;
}

int MIN(int x, int y)
{
	if (x < y) return x; else return y;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d%d%d", &D,&I,&M,&n);
		for (int i = 0; i < n; ++i) scanf("%d" , a + i);
		for (int i = 0; i < 256; ++i)
			f[0][i] = abs(a[0] - i);
		for (int i = 1; i < n; ++i)
			for (int j = 0; j < 256; ++j)
			{
				f[i][j] = i * D + abs(a[i] - j);
				f[i][j] = MIN(f[i][j], f[i - 1][j] + D);
				for (int k = 0; k < 256; ++k)
					if (abs(k - j) <= M)
						f[i][j] = MIN(f[i][j], f[i - 1][k] + abs(a[i] - j));
					else
					{
						if (M == 0) continue;
						int no = abs(j - k) / M;
						if (abs(j - k) % M == 0) --no;
						f[i][j] = MIN(f[i][j], f[i - 1][k] + abs(a[i] - j) +  I * no);
					}
			}
		int ans = 0x7fffffff;
		for (int i = 0; i < 256; ++i)
			ans = MIN(ans, f[n - 1][i]);
		printf("Case #%d: %d\n", ca, ans);
	}
	fclose(stdin);
	fclose(stdout);

}
