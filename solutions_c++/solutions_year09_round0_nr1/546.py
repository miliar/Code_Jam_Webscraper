#include <cstdio>
#include <cstring>
#include <cctype>

const int LMAX = 20;
const int DMAX = 5000;

char word[DMAX][LMAX];
char pattern[LMAX*30];
bool ok[LMAX][26];
int len, d, n;

int Solve()
{
	memset(ok, 0, sizeof(ok));

	int k = 0;
	int balance = 0;

	for (int i = 0; pattern[i]; i++)
		if (isalpha(pattern[i]))
		{
			ok[k][pattern[i] - 'a'] = true;
			if (balance == 0)
				k++;
		}
		else if (pattern[i] == '(')
			balance++;
		else
		{
			balance--;
			k++;
		}

	int res = 0;
	bool flag;

	for (int i = 0; i < d; i++)
	{
		flag = true;
		for (int j = 0; word[i][j]; j++)
			if (!ok[j][word[i][j] - 'a'])
			{
				flag = false;
				break;
			}
		if (flag)
			res++;
	}

	return res;
}

int main()
{
	freopen("aliens.in", "r", stdin);
	freopen("aliens.out", "w", stdout);

	scanf("%d%d%d\n", &len, &d, &n);
	for (int i = 0; i < d; i++)
		gets(word[i]);

	for (int tnum = 1; tnum <= n; tnum++)
	{
		gets(pattern);
		printf("Case #%d: %d\n", tnum, Solve());
	}

	return 0;
}
