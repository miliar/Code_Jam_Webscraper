#include <iostream>
using namespace std;

const int MOD = 100003;
const int L = 501;

int F[L][L], C[L][L];

void calc()
{
	for (int i = 0; i < L; i ++)
		for (int j = 0; j <= i; j ++)
		{
			if (!i && !j) C[i][j] = 1; else C[i][j] = 0;
			if (i) C[i][j] += C[i - 1][j];
			if (i && j) C[i][j] += C[i - 1][j - 1];
			C[i][j] %= MOD;
		}

	long long tmp;
	for (int i = 2; i < L; i ++)
	{
		F[i][1] = 1;
		for (int j = 2; j < i; j ++)
		{
			tmp = 0;
			for (int k = 1; k < j; k ++)
				tmp += F[j][k] * 1LL * C[i - j - 1][j - k - 1];
			tmp %= MOD;
			F[i][j] = tmp;
		}
	}
}

int main()
{
	calc();
	int T;
	cin >> T;
	for (int _T = 1; _T <= T; _T ++)
	{
		int N;
		cin >> N;
		int ans = 0;
		for (int i = 1; i < N; i ++)
		{
			ans += F[N][i];
			ans %= MOD;
		}
		printf("Case #%d: %d\n", _T, ans);
	}
}
