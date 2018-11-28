#include <cstdio>
#include <cstring>

const char STR[] = "welcome to code jam";
const int STRLEN = 19;
const int MaxL = 1000;
const int Modulo = 10000;

int N;
char Buf[MaxL];
int DP[MaxL][STRLEN];

void Add(int &i, int Delta)
{
	i += Delta;
	if (i >= Modulo)
		i -= Modulo;
}

int Work()
{
	fgets(Buf, MaxL, stdin);
	N = strlen(Buf) - 1;
	memset(DP, 0, sizeof(DP));
	for (int i = 0; i < N; i ++)
	{
		if (Buf[i] == STR[0])
			Add(DP[i][0], 1);
		if (i == 0)
			continue;
		for (int j = 0; j < STRLEN; j ++)
		{
			if (j >= 1 && Buf[i] == STR[j])
				Add(DP[i][j], DP[i - 1][j - 1]);
			Add(DP[i][j], DP[i - 1][j]);
		}
	}
	int Ans = DP[N - 1][STRLEN - 1];
	return Ans;
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	int Cases;
	scanf("%d", &Cases);
	fgets(Buf, MaxL, stdin);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %04d\n", Case, Work());
	
	return 0;
}
