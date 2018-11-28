#include <cstdio>

using namespace std;

const int SZ = 110;
char game[SZ][SZ];
double wp[SZ];
double owp[SZ];
double oowp[SZ];
double result[SZ];
int N;

void cal_wp()
{
	int i, j;
	for (i = 0; i < N; i++)
	{
		int win = 0;
		int sum = 0;
		for (j = 0; j < N; j++)
		{
			if (game[i][j] == '1') win += 1;
			if (game[i][j] != '.') sum += 1;
		}
		wp[i] = (double)win / (double)sum;
	}
}

void cal_owp()
{
	int i, j, k;
	for (i = 0; i < N; i++)
	{
		double sum = 0.0;
		int num = 0;
		for (j = 0; j < N; j++)
		{
			if (game[i][j] != '.')
			{
				int s = 0;
				int w = 0;
				double cur_wp;
				for (k = 0; k < N; k++)
				{
					if (k != i)
					{
						if (game[j][k] == '1') w += 1;
						if (game[j][k] != '.') s += 1;
					}
				}
				cur_wp = (double)w / double(s);
				sum += cur_wp;
				num++;
			}
		}
		owp[i] = sum / (double)(num);
	}
}

void cal_oowp()
{
	int i, j;
	for (i = 0; i < N; i++)
	{
		double sum = 0.0;
		int num = 0;
		for (j = 0; j < N; j++)
		{
			if (game[i][j] != '.')
			{
				sum += owp[j];
				num++;
			}
		}
		oowp[i] = sum / (double)(num);
	}
}

void cal_result()
{
	int i;
	for (i = 0; i < N; i++)
		result[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
}




int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w",stdout);
	int T;
	scanf("%d", &T);
	int t;
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		scanf("%d", &N);
		int n;
		for (n = 0; n < N; n++)
			scanf("%s", game[n]);
		cal_wp();
		cal_owp();
		cal_oowp();
		cal_result();
		int i;
		for (i = 0; i < N; i++)
			printf("%.12lf\n", result[i]);
	}
	return 0;
}

		