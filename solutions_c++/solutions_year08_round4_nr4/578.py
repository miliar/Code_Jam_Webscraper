#include <cstdio>
#include <cstring>

#define MAXLEN 50011
#define INF 999999999

int K, len, res, seen[8], st[8];
char str[MAXLEN], tmp[MAXLEN];

void swap(char &a, char &b)
{
	int tmp;

	tmp = a, a = b, b = tmp;
}

int getCost(char *str)
{
	int res = 1;	

	for (int i = 0; i + 1 < len; i++)
		res += str[i] != str[i + 1];

	return res;
}

void update()
{
	for (int i = 0; i + K - 1 < len; i += K)
	{
		for (int j = 0; j < K; j++)
			tmp[i + j] = str[i + st[j]];
	}

	int ccost = getCost(tmp);
	if (ccost < res)
		res = ccost;
}

void back(int k)
{
	if (k == K)
		update();
	else
		for (int i = 0; i < K; i++)
			if (!seen[i])
			{
				seen[i] = 1;
				st[k] = i;
				back(k + 1);
				seen[i] = 0;
			}
}

int solve()
{
	res = INF;
	memset(seen, 0, sizeof(seen));
	back(0);
	return res;
}

void readAndSolve()
{
	int N;

	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		scanf("%d %s", &K, str);
		len = strlen(str);

		printf("Case #%d: %d\n", i, solve());
	}
}

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);	

	readAndSolve();

	return 0;
}