#include <cstdio>
#include <cstring>

const int MaxL = 15 + 1;
const int MaxD = 5000 + 10;

int L, D, N;
char Str[MaxD][MaxD];
char Buf[300000];

int Tmp[MaxL][26];

int Check()
{
	scanf("%s", &Buf);
	memset(Tmp, 0, sizeof(Tmp));
	int Ptr = 0;
	for (int i = 0; i < L; i ++)
	{
		if (Buf[Ptr] == '(')
		{
			while (Buf[++ Ptr] != ')')
				Tmp[i][Buf[Ptr] - 'a'] = 1;
			Ptr ++;
		}
		else
		{
			Tmp[i][Buf[Ptr] - 'a'] = 1;
			Ptr ++;
		}
	}
	int Ans = 0;
	for (int i = 0; i < D; i ++)
	{
		int OK = 1;
		for (int j = 0; j < L; j ++)
			if (! Tmp[j][Str[i][j] - 'a'])
			{
				OK = 0;
				break;
			}
		Ans += OK;
	}
	return Ans;
}

int main()
{
	freopen("large_A.in", "r", stdin);
	freopen("large_A.out", "w", stdout);
	
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i ++)
		scanf("%s", &Str[i]);
	
	for (int Case = 1; Case <= N; Case ++)
		printf("Case #%d: %d\n", Case, Check());
	
	return 0;
}
