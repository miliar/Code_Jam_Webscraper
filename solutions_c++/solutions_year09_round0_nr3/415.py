#include <cstdio>
#include <cstring>
#define MAXN 1005
int f[MAXN][20], cnt[20], n, test, len;
char s[MAXN];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	const char t[] = "welcome to code jam";
	scanf("%d", &n); gets(s);
	for (int test = 1; test <= n; test++)
	{
		gets(s); len = strlen(s);
//		memset(f, 0, sizeof(f));
//		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < len; i++)
			for (int j = 0; j < 19; j++)
				f[i][j] = 0;
		for (int i = 0; i < 19; i++) cnt[i] = 0;
		for (int i = 0; i < len; i++)
			for (int j = 0; j < 19; j++)
				if (s[i] == t[j])
				{
					if (j == 0) f[i][j] = 1;
					else f[i][j] = cnt[j - 1];
					cnt[j] = (cnt[j] + f[i][j]) % 10000;
				}
		printf("Case #%d: %0.4d\n", test, cnt[18]);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}