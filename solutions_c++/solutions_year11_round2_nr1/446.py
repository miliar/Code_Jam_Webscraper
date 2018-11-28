#include<stdio.h>
#include<algorithm>
using namespace std;

int n;
char s[111][111];

double wp[111], owp[111], oowp[111];
int t[111], w[111];

void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		t[i] = w[i] = 0;
		scanf("%s", s[i]);
		for (int j = 0; j < n; j++)
		{
			t[i] += s[i][j] != '.';
			w[i] += s[i][j] == '1';
		}
		wp[i] = 1.0 * w[i] / t[i];
	}
	for (int i = 0; i < n; i++)
	{
		owp[i] = 0.0;
		for (int j = 0; j < n; j++)
		{
			if (s[i][j] != '.')
			{
				owp[i] += (w[j] - (s[j][i] == '1')) / (t[j] - 1.0);
			}
		}
		owp[i] /= t[i];
	}
	for (int i = 0; i < n; i++)
	{
		oowp[i] = 0.0;
		for (int j = 0; j < n; j++)
		{
			if (s[i][j] != '.')
			{
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= t[i];
	}
	for (int i = 0; i < n; i++)
	{
		printf("%.10f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		printf("Case #%d:\n", t);
		solve();
	}
	return 0;
}
