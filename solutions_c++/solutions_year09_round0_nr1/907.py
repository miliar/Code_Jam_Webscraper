#include <iostream>
#include <memory.h>

using namespace std;

const int MaxL = 20;
const int MaxD = 5005;

int L, D, N, S[MaxD][MaxL];
bool P[MaxL][26];
char Ch;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d%d%d\n", &L, &D, &N);
	for (int i = 0; i < D; i++)
	{
		for (int j = 0; j < L; j++) S[i][j] = getchar() - 97;
		scanf("\n");
	}
	for (int i = 1; i <= N; i++)
	{
		memset(P, 0, sizeof(P));
		for (int j = 0; j < L; j++)
		{
			Ch = getchar();
			if (Ch == '(')
				while (1)
				{
					Ch = getchar();
					if (Ch == ')') break;
					P[j][Ch - 97] = 1;
				}
			else P[j][Ch - 97] = 1;
		}
		int Ans = 0;
		for (int j = 0; j < D; j++)
		{
			bool Same = 1;
			for (int k = 0; k < L; k++)
				if (!P[k][S[j][k]])
				{
					Same = 0;
					break;
				}
			if (Same) Ans ++;
		}
		printf("Case #%d: %d\n", i, Ans);
		scanf("\n");
	}
	return 0;
}
