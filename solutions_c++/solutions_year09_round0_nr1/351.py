#include<stdio.h>
#include<string.h>

char st[5050][20];
char tmp[5000];
bool f[20][30];

int L, D, N;

bool find(int a)
{
	for (int i = 0; i < L; i++)
	{
		if (!f[i][st[a][i] - 'a'])
			return 0;
	}
	return 1;
}
	

int solve()
{
	char c;
	memset(f, 0, sizeof(f));
	getchar();
	for (int i = 0; i < L; i++)
	{
		c = getchar();
		if (c != '(')
		{
			f[i][c - 'a'] = 1;
			continue;
		}
		while (1)
		{
			c = getchar();
			if (c == ')')
				break;
			f[i][c - 'a'] = 1;
		}
	}
	int ans = 0;
	for (int i = 0; i < D; i++)
	{
		ans += find(i);
	}
	return ans;
}

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i< D; i++)
	{
		scanf("%s", st[i]);
	}
	
	for (int i = 1; i <= N; i++)
	{
		printf("Case #%d: %d\n", i, solve());
	}
//	while (1);
	return 0;
}
