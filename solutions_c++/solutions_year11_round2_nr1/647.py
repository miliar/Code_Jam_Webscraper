#include <cstdio>
#include <cstring>

namespace Solve
{
	const int NTEAM_MAX = 105;
	int mat[NTEAM_MAX][NTEAM_MAX], nteam;
	int win_cnt[NTEAM_MAX], tot_cnt[NTEAM_MAX];
	double owp[NTEAM_MAX], rpi[NTEAM_MAX];

	void work();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		fscanf(fin, "%d", &nteam);
		for (int i = 0; i < nteam; i ++)
		{
			static char str[NTEAM_MAX + 5];
			fscanf(fin, "%s", str);
			for (int j = 0; j < nteam; j ++)
				mat[i][j] = str[j] == '.' ? 0 : (str[j] == '1' ? 1 : -1);
		}
		work();
		fprintf(fout, "Case #%d:\n", casenu);
		for (int i = 0; i < nteam; i ++)
			fprintf(fout, "%.9lf\n", rpi[i]);
	}
}

void Solve::work()
{
	for (int i = 0; i < nteam; i ++)
	{
		int w = 0, t = 0;
		for (int j = 0; j < nteam; j ++)
			if (mat[i][j])
			{
				t ++;
				if (mat[i][j] == 1)
					w ++;
			}
		win_cnt[i] = w;
		tot_cnt[i] = t;
		rpi[i] = 0.25 * w / t;
	}

	for (int i = 0; i < nteam; i ++)
	{
		double sum = 0;
		int nopt = 0;
		for (int j = 0; j < nteam; j ++)
			if (mat[j][i])
			{
				nopt ++;
				int w = win_cnt[j], t = tot_cnt[j];
				t --;
				if (mat[j][i] == 1)
					w --;
				sum += double(w) / t;
			}
		sum /= nopt;
		owp[i] = sum;
		rpi[i] += 0.5 * sum;
	}

	for (int i = 0; i < nteam; i ++)
	{
		double sum = 0;
		int nopt = 0;
		for (int j = 0; j < nteam; j ++)
			if (mat[j][i])
			{
				nopt ++;
				sum += owp[j];
			}
		sum /= nopt;
		rpi[i] += 0.25 * sum;
	}
}

int main()
{
	Solve::solve(stdin, stdout);
}

