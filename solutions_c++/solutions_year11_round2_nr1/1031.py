#pragma comment(linker, "/STACK:16777216")

#include <vector>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <set>
using namespace std;

char a[110][110];
int n;
double res;
double owp[110];

void calcOwp(int i)
{
	int tot = 0;
	owp[i] = 0;
	for (int k = 0; k < n; ++k)
	{
		if (a[i][k] != '.')
		{
			++tot;
			int w = 0, l = 0;
			for (int j = 0; j < n; ++j)
			{
				if (j != i)
				{
					w += (int)(a[k][j] == '1');
					l += (int)(a[k][j] == '0');
				}
			}
			double wp = w;
			wp /= w + l;
			owp[i] += wp;
		}
	}
	owp[i] /= tot;
}


int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%s", &a[i]);
		printf("Case #%d:\n", t + 1);

		for (int i = 0; i < n; ++i)
			calcOwp(i);
		for (int i = 0; i < n; ++i)
		{
			res = 0;
			int w = 0, l = 0;
			double oowp = 0.0;
			for (int j = 0; j < n; ++j)
			{
				w += (int)(a[i][j] == '1');
				l += (int)(a[i][j] == '0');
				if (a[i][j] != '.')
					oowp += owp[j];
			}
			res += 0.25 * ((double)(w) / (w + l));
			res += 0.5 * owp[i];
			res += 0.25 * oowp / (w + l);
			printf("%.9lf\n", res);
		}
	}
	
	return 0;
}
