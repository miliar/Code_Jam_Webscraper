#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char N[25];
int length;

void input(void)
{
	int i;
	scanf("%s", N);
	length = strlen(N);
}

void solve(int index)
{
	int i, j, k, flag, tmp;
	k = 0;
	flag = 0;
	for (i = 0; i < length - 1; ++i)
	{
		for (j = i; j < length; ++j)
		{
			if (N[i] < N[j])
			{
				flag = 1;
				k = i;
				break;
			}
		}
	}
	if (flag)
	{
		for (i = length - 1; i > k; --i)
		{
			if (N[i] > N[k])
			{
				tmp = N[k];
				N[k] = N[i];
				N[i] = tmp;
				break;
			}
		}
		for (i = k + 1; i < (k + 1 + length) / 2; ++i)
		{
			tmp = N[i];
			N[i] = N[k + length - i];
			N[k + length - i] = tmp;
		}
	}
	else
	{
		k = length;
		for (i = 0; i < length; ++i)
		{
			if (N[i] == '0')
			{
				k = i;
				break;
			}
		}
		for (i = 0; i < k / 2; ++i)
		{
			tmp = N[i];
			N[i] = N[k - 1 - i];
			N[k - 1 - i] = tmp;
		}
		N[k] = 0;

		for (i = length + 1; i > length + 1 - k; --i)
		{
			N[i] = N [i - (length + 1 - k)];
		}
		for (; i > 0; --i)
		{
			N[i] = '0';
		}
	}
	printf("Case #%d: %s\n", index, N);
}

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int i;
	scanf("%d", &T);
	for (i = 0; i < T; ++i)
	{
		input();
		solve(i + 1);
	}
	return 0;
}
