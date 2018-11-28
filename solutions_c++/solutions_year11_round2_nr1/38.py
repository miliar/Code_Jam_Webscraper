#include <stdio.h>
#include <string.h>

int tc, ntc;
int n;
char mm[120][120];

double wp[120];
double owp[120];
double oowp[120];

void calc_wp()
{
	int i, j;
	for (i=0; i<n; i++)
	{
		int num = 0;
		double tot = 0;
		for (j=0; j<n; j++) if (mm[i][j] != '.')
		{
			num++;
			if (mm[i][j] == '1') tot++;
		}
		wp[i] = tot / num;
	}
}

void calc_owp()
{
	int i, j, k;
	for (i=0; i<n; i++)
	{
		int num = 0;
		double tot = 0;

		for (j=0; j<n; j++) if (mm[i][j] != '.')
		{
			num++;

			int num2 = 0;
			double tot2 = 0;
			for (k=0; k<n; k++) if (mm[j][k] != '.' && k != i)
			{
				num2++;
				if (mm[j][k] == '1') tot2++;
			}

			tot += tot2 / num2;
		}
		owp[i] = tot / num;
	}
}

void calc_oowp()
{
	int i, j;
	for (i=0; i<n; i++)
	{
		int num = 0;
		double tot = 0;
		for (j=0; j<n; j++) if (mm[i][j] != '.')
		{
			num++;
			tot += owp[j];
		}
		oowp[i] = tot / num;
	}
}

int main()
{
	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int i, j;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%d", &n);
		for (i=0; i<n; i++) fscanf(fi, "%s", mm[i]);

		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		calc_wp();
		calc_owp();
		calc_oowp();
		
		printf("Case #%d:\n", tc);
		fprintf(fo, "Case #%d:\n", tc);
		for (i=0; i<n; i++)
		{
			double f = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.10lf\n", f);
			fprintf(fo, "%.10lf\n", f);
		}
	}

	fclose(fi); fclose(fo);

	return 0;
}