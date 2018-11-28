#include<cstdio>
#include<algorithm>
using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"
#define NMAX 2048
int B[NMAX], E[NMAX], W[NMAX], I[NMAX];

bool cmp(int i, int j)
{
	return W[i] < W[j];
}

void solve()
{
	int k = 0, x, s, r, t, n, b, e, w;

	B[k] = E[k] = W[k] = 0;
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	while(n--)
	{
		scanf("%d%d%d", &b, &e, &w);
		++k;
		B[k] = E[k - 1];
		E[k] = b;
		W[k] = 0;
		++k;
		B[k] = b;
		E[k] = e;
		W[k] = w;
	}

	++k;
	B[k] = E[k - 1];
	E[k] = x;
	W[k] = 0;

	int i;
	double ans = 0, time;

	for(i = 0; i <= k; ++i)
		I[i] = i;
	sort(I, I + k + 1, cmp);

	for(i = 0; i <= k; ++i)
	{
		int j = I[i];
		time = (double)(E[j] - B[j]) / (r + W[j]);
		if(ans + time <= t)
			ans += time;
		else
		{
			ans = t + ((E[j] - B[j]) - ((t - ans) * (r + W[j]))) / (s + W[j]);
			break;
		}
	}

	for(++i; i <= k; ++i)
	{
		int j = I[i];
		ans += (double)(E[j] - B[j]) / (s + W[j]);
	}

	printf("%.8lf\n", ans);
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);
	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
