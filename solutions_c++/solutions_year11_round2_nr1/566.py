// Google Code Jame 2011 - Round 1B
// by vdave, Hungary, 2011

#include <cstdio>


int N;
int GC[128];
double WP[128];
double OWP[128];
double OOWP[128];
char matches[128][128];

void solve_1(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; ++tc)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%s", &(matches[i][0]));
		}

		for (int tm = 0; tm < N; ++tm)
		{
			GC[tm] = 0;
			WP[tm] = 0.0;

			for (int tm2 = 0; tm2 < N; ++tm2)
			{
				if (matches[tm][tm2] == '0')
				{
					GC[tm]++;
				}
				else if (matches[tm][tm2] == '1')
				{
					GC[tm]++;
					WP[tm] += 1.0;
				}
			}
		}

		// Calculate WP[tm]
		for (int tm = 0; tm < N; ++tm)
		{
			WP[tm] /= (double) GC[tm];
		}

		// Calculate OWP[tm]
		for (int tm = 0; tm < N; ++tm)
		{
			int opCnt = 0;
			double totalOWP = 0.0;
			for (int tm2 = 0; tm2 < N; ++tm2)
			{
				if (matches[tm][tm2] != '.')
				{
					opCnt++;
					totalOWP += ((WP[tm2] * GC[tm2]) - (1 - (matches[tm][tm2] - '0'))) / ((double) (GC[tm2] - 1));
				}
			}
			OWP[tm] = totalOWP / (double) opCnt;
		}

		// Calculate OOWP[tm]
		for (int tm = 0; tm < N; ++tm)
		{
			int opCnt = 0;
			double totalOOWP = 0.0;
			for (int tm2 = 0; tm2 < N; ++tm2)
			{
				if (matches[tm][tm2] != '.')
				{
					opCnt++;
					totalOOWP += OWP[tm2];
				}
			}
			OOWP[tm] = totalOOWP / (double) opCnt;
		}

		printf("Case #%d:\n", tc);
		for (int i = 0; i < N; ++i)
		{
			printf("%.12lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	fflush(stdout);
}






void solve_2(int argc, char *argv[])
{

}






void solve_3(int argc, char *argv[])
{

}






int main(int argc, char *argv[])
{
	solve_1(argc, argv);
	return 0;
}