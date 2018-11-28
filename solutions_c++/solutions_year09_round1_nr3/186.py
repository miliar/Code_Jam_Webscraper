#include <iostream>

using namespace std;

const int MaxN = 45;

int N, C, TCase;
long long CC[MaxN][MaxN];
double A[MaxN], B[MaxN], Ans;
bool Used[MaxN];

void Dp(int Cur)
{
	Used[Cur] = 1;
	double a, b = 0.0, c = 0.0;
	if (Cur >= N) a = 1.0 - (double)CC[Cur][N] / CC[C][N];
	else a = 1.0;
	for (int i = 1; i <= C - Cur; i++)
	{
		if (N - i > Cur) continue;
		if (i > N) break;
		if (!Used[Cur + i]) Dp(Cur + i);
		b = (double)b + (double)A[Cur + i] * CC[Cur][N - i] * CC[C - Cur][i];
		c = (double)c + (double)B[Cur + i] * CC[Cur][N - i] * CC[C - Cur][i];
	}
	b = b / (double)CC[C][N], c = c / (double)CC[C][N] - 1;
	A[Cur] = b / a, B[Cur] = c / a;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int i = 0; i <= 40; i++)
	{
		CC[i][0] = CC[i][i] = 1;
		for (int j = 1; j < i; j++)
			CC[i][j] = CC[i - 1][j - 1] + CC[i - 1][j];
	}
	for (int Case = 1; Case <= TCase; Case++)
	{
		scanf("%d%d", &C, &N);
		memset(Used, 0, sizeof(Used));
		A[C] = 1.0, B[C] = 0.0, Used[C] = 1;
		Dp(0);
		Ans = - (double)B[0] / A[0];
		printf("Case #%d: %.7lf\n", Case, Ans);
	}
	return 0;
}
