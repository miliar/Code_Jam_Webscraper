#include <iostream>
#include <string>
#include <cstring>

using namespace std;

const int MaxL = 20;
const int MaxN = 505;

int TCase, N, F[MaxL][MaxN];
char G[19] = {'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};
char S[MaxN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &TCase);
	for (int Case = 1; Case <= TCase; Case++)
	{
		gets(S);
		N = strlen(S);
		memset(F, 0, sizeof(F));
		for (int i = 0; i < N; i++)
			if (S[i] == G[18]) F[18][i] = 1;
		for (int i = 17; i >= 0; i--)
		{
			int Sum = 0;
			for (int j = N - 1; j >= 0; j--)
			{
				if (S[j] == G[i]) F[i][j] = Sum;
				else F[i][j] = 0;
				Sum += F[i + 1][j];
				if (Sum >= 10000) Sum -= 10000;
			}
		}
		int Ans = 0;
		for (int i = 0; i < N; i++)
		{
			Ans += F[0][i];
			if (Ans >= 10000) Ans -= 10000;
		}
		printf("Case #%d: ", Case);
		if (Ans < 1000) printf("0");
		if (Ans < 100) printf("0");
		if (Ans < 10) printf("0");
		printf("%d\n", Ans);
	}
	return 0;
}
