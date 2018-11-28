#include <cstdio>
#include <cmath>

namespace Solve
{
	const int NRC_MAX = 505;
	const double EPS = 1e-8;
	typedef long long int Bignum_t;
	int nrow, ncol, mass[NRC_MAX][NRC_MAX];
	Bignum_t mass_sum[NRC_MAX][NRC_MAX];
	double md[2][NRC_MAX][NRC_MAX], md_sum[2][NRC_MAX][NRC_MAX];

	bool test(int r0, int c0, int size);
	void init();

	int work();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		int d;
		fscanf(fin, "%d%d%d", &nrow, &ncol, &d);
		static char str[NRC_MAX];
		for (int i = 1; i <= nrow; i ++)
		{
			fscanf(fin, "%s", str);
			for (int j = 1; j <= ncol; j ++)
				mass[i][j] = str[j - 1] - '0' + d;
		}
		int ans = work();
		fprintf(fout, "Case #%d: ", casenu);
		if (ans == -1)
			fprintf(fout, "IMPOSSIBLE\n");
		else
			fprintf(fout, "%d\n", ans);
	}
}

int Solve::work()
{
	init();
	int ans = 2;
	for (int i = 0; i < nrow; i ++)
		for (int j = 0; j < ncol; j ++)
			for (int k = ans + 1; i + k <= nrow && j + k <= ncol; k ++)
				if (test(i, j, k) && k > ans)
					ans = k;
	if (ans == 2)
		ans = -1;
	return ans;
}

void Solve::init()
{
	for (int i = 1; i <= nrow; i ++)
		for (int j = 1; j <= ncol; j ++)
		{
			md[0][i][j] = mass[i][j] * (i - 0.5);
			md[1][i][j] = mass[i][j] * (j - 0.5);
			mass_sum[i][j] = mass_sum[i - 1][j] + mass_sum[i][j - 1] - 
				mass_sum[i - 1][j - 1] + mass[i][j];
			for (int k = 0; k < 2; k ++)
			{
				md_sum[k][i][j] = md_sum[k][i - 1][j] + md_sum[k][i][j - 1] -
					md_sum[k][i - 1][j - 1] + md[k][i][j];
			}
		}
}

bool Solve::test(int r0, int c0, int size)
{
	int r1 = r0 + size, c1 = c0 + size;
	double s0[2] = {mass_sum[r1][c1] + mass_sum[r0][c0] -
		mass_sum[r0][c1] - mass_sum[r1][c0] -
		mass[r0 + 1][c0 + 1] - mass[r0 + 1][c1] - mass[r1][c0 + 1] - mass[r1][c1]};
	s0[1] = s0[0];
	s0[0] *= r0 + size * 0.5;
	s0[1] *= c0 + size * 0.5;
	for (int i = 0; i < 2; i ++)
	{
		double tmp = md_sum[i][r1][c1] + md_sum[i][r0][c0] -
			md_sum[i][r0][c1] - md_sum[i][r1][c0] -
			md[i][r0 + 1][c0 + 1] - md[i][r0 + 1][c1] - md[i][r1][c0 + 1] - md[i][r1][c1];
		if (fabs(tmp - s0[i]) >= EPS)
			return false;
	}
	return true;
}

int main()
{
	Solve::solve(stdin, stdout);
}

