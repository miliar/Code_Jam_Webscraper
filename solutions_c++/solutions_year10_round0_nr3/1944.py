#include <cstdio>
#include <cstring>

int a[1002];
int next[1002], sum[1002];

int R, K, n;
int T;

void solve (int caz)
{
	int i, j;
       long long s = 0;
	for (i = 1; i <= n; ++i)
		s += (long long)a[i];

	if (K >= s)
	{
		printf ("Case #%d: %lld\n", caz, (long long)R * s);
		return;
	}

	int ok = 0;
	for (i = 1; i <= n; ++i)
		if (a[i] <= K)
			ok = 1;

	if (!ok)
	{
		printf ("Case #%d: 0\n", caz);
		return ;

	}


	for (i = 1; i <= n; ++i)
	{
		s = 0;

		for (j = i; s + a[j] <= K; )
		{
			s += a[j];

			++j;
			if (j == n + 1)
				j = 1;
		}
		next[i] = j;
		sum[i] = s;

	}

	i = 1;
	s = 0;
	for (int r = 1; r <= R; ++r)
	{
		s += sum[i];
		i = next[i];
	}

	printf ("Case #%d: %lld\n", caz,s);
}

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);	
	scanf ("%d\n", &T);

	int i;
	
	for (int caz = 1; caz <= T; ++caz)
	{
		scanf ("%d %d %d\n", &R, &K, &n);
		for (i = 1; i <= n; ++i)
			scanf ("%d ", &a[i]);
		solve (caz);
	}

	return 0;
}

