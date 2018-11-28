# include <cstdio>
# include <cstdlib>
# include <climits>
# include <cstring>
# include <cctype>

# include <iostream>
# include <sstream>
# include <vector>
# include <string>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <algorithm>

using namespace std;

const int N_MAX = 1000;

char table[N_MAX][N_MAX + 10];
int wins[N_MAX];
int lose[N_MAX];
int games[N_MAX];
int n;
double wp[N_MAX];
double owp[N_MAX];
double oowp[N_MAX];
double rpi[N_MAX];

double getOWP(int id)
{
	double res = 0;
	for (int i = 0; i < n; ++i)
		if (table[id][i] != '.')
		{
			double tmp = wins[i];
			if (table[id][i] == '0')
				tmp -= 1.0;
			tmp /= static_cast<double>(games[i] - 1);
			res += tmp;
		}

	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	scanf("%d", &testNum);

	for (int testId = 1; testId <= testNum; ++testId)
	{
		scanf("%d\n", &n);

		for (int i = 0; i < n; ++i)
			gets(table[i]);

		for (int i = 0; i < n; ++i)
		{
			wins[i] = 0;
			lose[i] = 0;
			games[i] = 0;
			for (int j = 0; j < n; ++j)
			{
				if (table[i][j] != '.')
				{
					games[i]++;
					if (table[i][j] == '0')
						lose[i]++;
					else if (table[i][j] == '1')
						wins[i]++;
				}
			}
		}

		for (int i = 0; i < n; ++i)
		{
			wp[i] = static_cast<double>(wins[i]) / static_cast<double>(games[i]);
			owp[i] = getOWP(i) / static_cast<double>(games[i]);
		}

		for (int i = 0; i < n; ++i)
		{
			oowp[i] = 0;
			for (int j = 0; j < n; ++j)
				if (table[i][j] != '.')
				{
					oowp[i] += owp[j];
				}
			oowp[i] /= static_cast<double>(games[i]);
		}

		for (int i = 0; i < n; ++i)
		{
			rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		}

		printf("Case #%d:\n", testId);
		for (int i = 0; i < n; ++i)
		{
			printf("%.7lf\n", rpi[i]);
		}
	}

	return 0;
}