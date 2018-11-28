#include <stdio.h>

#define nmax 1005

int r, k, n, v [nmax];


void scan ()
{
	int i;
	scanf ("%d%d%d", &r, &k, &n);
	for (i=1; i <= n; ++i)
		scanf ("%d", &v [i]);
}

long long rez ()
{
	int i, j, l=1, w;
	long long s=0;
	for (i=1; i <= r; ++i)
	{
		w=0;
		for (j=l; j <= n && w+v [j] <= k; ++j)
			w+=v [j];
		if (j > n)
			for (j=1; j < l && w+v [j] <= k; ++j)
				w+=v [j];
		l=j;
		if (l > n) l=1;
		s+=w;
	}
	return s;
}

int main ()
{
	freopen ("park.in", "r", stdin);
	freopen ("park.out", "w", stdout);
	int i, t;
	scanf ("%d", &t);
	for (i=1; i <= t; ++i)
	{
		scan ();
		printf ("Case #%d: %lld\n", i, rez ());
	}
	return 0;
}

