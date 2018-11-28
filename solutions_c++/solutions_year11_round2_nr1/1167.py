#include<cstdio>
using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"
#define NMAX 101

void solve()
{
	int n;
	char S[NMAX][NMAX];
	double WP[NMAX], OWP[NMAX], OOWP[NMAX], W[NMAX], L[NMAX];

	scanf("%d", &n);
	for(int i = 0; i < n; ++i)
	{
		scanf("%s", S[i]);
		W[i] = L[i] = 0;
		for(int j = 0; j < n; ++j)
		{
			if(S[i][j] == '1')
				++W[i];
			if(S[i][j] == '0')
				++L[i];
		}
		WP[i] = (double) W[i] / (W[i] + L[i]);
	}

	for(int i = 0; i < n; ++i)
	{
		OWP[i] = 0;
		for(int j = 0; j < n; ++j)
		{
			if(S[i][j] == '.')
				continue;
			int w = W[j], l = L[j];
			if(S[j][i] == '1')
				--w;
			if(S[j][i] == '0')
				--l;
			OWP[i] += (double)w / (w + l);
		}
		OWP[i] /= W[i] + L[i];
	}

	for(int i = 0; i < n; ++i)
	{
		OOWP[i] = 0;
		for(int j = 0; j < n; ++j)
			if(S[i][j] != '.')
				OOWP[i] += OWP[j];
		OOWP[i] /= W[i] + L[i];
		printf("%lf\n", WP[i] / 4 + OWP[i] / 2 + OOWP[i] / 4);
	}
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);
	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d:\n", t);
		solve();
	}

	return 0;
}
