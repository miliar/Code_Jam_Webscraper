#include <cstdio>
#include <cstring>
const int N = 256;
char c[N][N], d[N][N], cmd[N];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testi = 0; testi < test; ++testi)
	{
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		int n;
		scanf("%d", &n);
		while (n--)
		{
			scanf("%s", cmd);
			c[cmd[0]][cmd[1]] = cmd[2];
			c[cmd[1]][cmd[0]] = cmd[2];
		}
		scanf("%d", &n);
		while (n--)
		{
			scanf("%s", cmd);
			d[cmd[0]][cmd[1]] = 1;
			d[cmd[1]][cmd[0]] = 1;
		}
		scanf("%d%s", &n, cmd);
		int j = 0;
		for (int i = 0; cmd[i]; ++i)
		{
			cmd[j++] = cmd[i];
			for (;;)
			{
				if (j == 1)
				{
					break;
				}
				char tmp = c[cmd[j - 2]][cmd[j - 1]];
				if (tmp)
				{
					--j;
					cmd[j - 1] = tmp;
				}
				else
				{
					break;
				}
			}
			for (int k = 0; k + 1 < j; ++k)
			{
				if (d[cmd[k]][cmd[j - 1]])
				{
					j = 0;
					break;
				}
			}
		}
		printf("Case #%d: [", testi + 1);
		for (int i = 0; i + 1 < j; ++i)
		{
			printf("%c, ", cmd[i]);
		}
		if (j)
		{
			printf("%c", cmd[j - 1]);
		}
		puts("]");
	}
	return 0;
}