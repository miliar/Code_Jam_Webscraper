#include <stdio.h>
#include <string.h>

char pattern[20] = "welcome to code jam";
char src[501];
int cnt[19][501];
int length;

void solve(int index)
{
	int i, j, k, res;
	gets(src);
	length = strlen(src);

	for (i = 0; i < 19; ++i)
	{
		for (j = 0; j < length; ++j)
		{
			cnt[i][j] = 0;
		}
	}

	for (i = 0; i < length - 18; ++i)
	{
		if (src[i] == pattern[0])
		{
			cnt[0][i] = 1;
		}
	}
	for (k = 1; k < 19; ++k)
	{
		for (i = k; i < length - 18 + k; ++i)
		{
			if (src[i] == pattern[k])
			{
				for (j = 0; j < i; ++j)
				{
					cnt[k][i] += cnt[k - 1][j];
				}
				if (cnt[k][j] > 10000)
				{
					cnt[k][j] %= 10000;
				}
			}
		}
	}

	res = 0;
	for (i = 18; i <length; ++i)
	{
		res += cnt[18][i];
	}
	res %= 10000;
	printf("Case #%d: %d%d%d%d\n", index, res / 1000, (res % 1000) / 100, (res % 100) / 10, (res % 10));

}

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N, i;
	scanf("%d", &N);
	gets(src);
	for (i = 0; i < N; ++i)
	{
		solve(i + 1);
	}
	return 0;
}
