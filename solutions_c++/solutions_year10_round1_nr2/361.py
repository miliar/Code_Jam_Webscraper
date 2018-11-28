#include <iostream>
#include <fstream>
#include <memory.h>
#include <cmath>

using namespace std;

#define MAXN 120
#define MAXM 257
#define EMP 256
#define oo 1000000000

ifstream in("input.txt");
ofstream out("output.txt");

int dp[MAXN][MAXM];
int tmp[MAXM];
int num[MAXN];

int main()
{
	int T;
	int D, I, M, N;
	int res;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		for (int i = 0; i < MAXN; i++)
			for (int j = 0; j < MAXM; j++)
				dp[i][j] = oo;
		out << "Case #" << t << ": ";
		in >> D >> I >> M >> N;
		for (int i = 1; i <= N; i++)
			in >> num[i];
		dp[1][EMP] = D;
		for (int i = 0; i <= 255; i++)
		{
			dp[1][i] = min(M ? I * int(ceil(double(abs((int)num[1] - i))/double(M))) : oo, abs((int)num[1] - i));
		}
		for (int i = 2; i <= N; i++)
		{
			dp[i][EMP] = dp[i - 1][EMP] + D;
			for (int j = 0; j <= 255; j++)
			{
				dp[i][j] = dp[i - 1][j] + D;
				for (int k = 0; k < MAXM; k++)
				{
					if (abs((int)j - k) <= M)
						dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs((int)j - num[i]));
				}
			}
			if (M == 0)
				continue;
			for (int j = 0; j < MAXM; j++)
				tmp[j] = dp[i][j];
			for (int j = 0; j <= 255; j++)
			{
				for (int k = 0; k < j; k++)
					tmp[j] = min(tmp[j], dp[i][k] + I * int(ceil(double(j - k)/double(M))));
			}
			for (int j = MAXM - 1; j >= 0; j--)
			{
				for (int k = j + 1; k <= 255; k++)
					tmp[j] = min(tmp[j], dp[i][k] + I * int(ceil(double(k - j)/double(M))));
			}
			for (int j = 0; j < MAXM; j++)
				dp[i][j] = min(dp[i][j], tmp[j]);
		}
		res = oo;
		for (int i = 0; i < MAXM; i++)
			res = min(res, dp[N][i]);
		out << res << endl;
	}
	return 0;
}