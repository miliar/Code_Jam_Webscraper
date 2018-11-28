#include <iostream>
#include <fstream>

using namespace std;

#define MaxiN 105

int TestCase, N, C, C1, C2, Ans;
int S1[MaxiN], S2[MaxiN], S[MaxiN];

void Go(int &x, int y)
{
	if (x < y)
		++ x;
	else
		if (x > y)
			-- x;
}

int main()
{
	#ifdef _PRJ
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	#endif
	#ifdef _CP
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	#endif
	#ifdef _UOI
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	#endif
	#ifdef _CXT
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	#endif
	int TestCase;
	cin >> TestCase;
	for (int i = 1; i <= TestCase; ++ i)
	{
		cin >> N;
		Ans = 0;
		C = C1 = C2 = 0;
		for (int j = 1; j <= N; ++ j)
		{
			char Ch;
			int Cmd;
			while (!isalpha(Ch = getchar()));
			cin >> Cmd;
			if (Ch == 'O')
			{
				S[++ C] = Cmd;
				S1[++ C1] = Cmd;
			}
			else
			{
				S[++ C] = - Cmd;
				S2[++ C2] = Cmd;
			}
		}
		for (int j = 1, k = 1, g = 1, t1 = 1, t2 = 1; g <= C; ++ g)
		{
			if (S[g] > 0)
			{
				while (j != S[g])
					Go(j, S[g]), Go(k, S2[t2]), ++ Ans;
				Go(k, S2[t2]), ++ Ans;
				++ t1;
			}
			else
			{
				while (k != - S[g])
					Go(k, - S[g]), Go(j, S1[t1]), ++ Ans;
				Go(j, S1[t1]), ++ Ans;
				++ t2;
			}
		}
		printf("Case #%d: %d\n", i, Ans);
	}
}
