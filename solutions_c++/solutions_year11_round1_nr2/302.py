#include <cstdio>
#include <cstring>

int N, M;
char S[10000 + 10][15];
int Cnt[10000 + 10][26], Len[10000 + 10];
char Dict[30];
int Possible[10000 + 10];

int Choose(int x)
{
	int Score = 0, Remain = Len[x];
	int nPossible = 0;
	for (int i = 0; i < N; i ++)
		if (Len[i] == Len[x])
			Possible[nPossible ++] = i;
	for (int tt = 0; tt < 26; tt ++)
	{
		int t = Dict[tt] - 'a';
		int OK = 0;
		for (int i = 0; i < nPossible; i ++)
			if (Cnt[Possible[i]][t])
			{
				OK = 1;
				break;
			}
		if (! OK)
			continue;
		if (! Cnt[x][t])
		{
			Score ++;
			int mPossible = 0;
			for (int i = 0; i < nPossible; i ++)
				if (Cnt[Possible[i]][t] == 0)
					Possible[mPossible ++] = Possible[i];
			nPossible = mPossible;
			continue;
		}
		int mPossible = 0;
		if (Remain == 0)
			break;
		for (int i = 0; i < nPossible; i ++)
		{
			int P = 1;
			for (int k = 0; k < Len[x]; k ++)
				if ((S[Possible[i]][k] - 'a' == t) ^ (S[x][k] - 'a' == t))
				{
					P = 0;
					break;
				}
			if (P)
				Possible[mPossible ++] = Possible[i];
		}
		nPossible = mPossible;
	}
	return Score;
}

void Work()
{
	scanf("%d%d", &N, &M);
	memset(Cnt, 0, sizeof(Cnt));
	for (int i = 0; i < N; i ++)
	{
		scanf("%s", &S[i]);
		Len[i] = strlen(S[i]);
		for (int j = 0; j < Len[i]; j ++)
			Cnt[i][S[i][j] - 'a'] ++;
	}
	while (M --)
	{
		scanf("%s", &Dict);
		int Ans = -1, Ansi = -1;
		for (int i = 0; i < N; i ++)
		{
			int t = Choose(i);
			//printf("[%d] %d\n", i, t);
			if (t > Ans)
			{
				Ans = t;
				Ansi = i;
			}
		}
		printf(" %s", S[Ansi]);
	}
	printf("\n");
}

int main()
{
	//freopen("B.txt", "r", stdin);
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d:", Case);
		Work();
	}
	return 0;
}