/*
 * $File: d.cpp
 * $Date: Sat May 07 13:06:46 2011 +0800
 */

#include <cstdio>
#include <cstring>

namespace Solve
{
	const int SEQLEN_MAX = 1005;
	double f[SEQLEN_MAX];
	bool used[SEQLEN_MAX];

	int seq[SEQLEN_MAX], seqlen;

	void init_f(int n);
	double work();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		fscanf(fin, "%d", &seqlen);
		for (int i = 0; i < seqlen; i ++)
		{
			int x;
			fscanf(fin, "%d", &x);
			seq[i] = x - 1;
		}
		fprintf(fout, "Case #%d: %.8lf\n", casenu, work());
	}
}

double Solve::work()
{
	init_f(seqlen);
	memset(used, 0, sizeof(used));
	double ans = 0;
	for (int i = 0; i < seqlen; i ++)
		if (!used[i])
		{
			int len = 0;
			do
			{
				len ++;
				used[i] = true;
				i = seq[i];
			} while (!used[i]);
			ans += f[len];
		}
	return ans;
}

void Solve::init_f(int n)
{
	f[1] = 0;
	f[2] = 2;
	for (int i = 3; i <= n; i ++)
	{
		double ans = 0;
		for (int j = 1; j < i; j ++)
			ans += f[j] + f[i - j] - 1;
		ans ++;
		f[i] = (ans / i + 1) / (1 - 1.0 / i);
	}
}

int main()
{
	Solve::solve(stdin, stdout);
}

