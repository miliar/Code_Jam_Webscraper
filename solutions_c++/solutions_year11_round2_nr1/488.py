#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, N, count = 0;
	vector <long double> OWP, OOWP;
	vector <int> sum, win;
	char s[111][111];
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d:\n", ++count);
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%s", s[i]);
		}
		sum.resize(N);
		win.resize(N);
		OWP.resize(N);
		OOWP.resize(N);
		for (int i = 0; i < N; ++i)
		{
			sum[i] = win[i] = 0;
			for (int j = 0; j < N; ++j)
			{
				win[i] += s[i][j] == '1';
				sum[i] += s[i][j] != '.';
			}
		}
		for (int i = 0; i < N; ++i)
		{
			long double all = .0;
			int temp = 0;
			for (int j = 0; j < N; ++j)
			{
				if (s[i][j] != '.')
				{
					++temp;
					all += (long double)(win[j] - (s[j][i] == '1')) / (sum[j] - 1);
				}
			}
			OWP[i] = all / temp;
		}
		for (int i = 0; i < N; ++i)
		{
			OOWP[i] = 0;
			int temp = 0;
			for (int j = 0; j < N; ++j)
			{
				OOWP[i] += s[i][j] != '.' ? OWP[j] : .0;
				temp += s[i][j] != '.';
			}
			OOWP[i] /= temp;
		}
		for (int i = 0; i < N; ++i)
		{
			printf("%.10lf\n", (long double)0.25 * win[i] / sum[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}
