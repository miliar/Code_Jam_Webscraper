#include <stdio.h>

#define maxx 1000010
#define ll long long

ll A, B, P;
int l, sol;
char u[maxx];
int g[maxx], s[maxx];

inline int find(int x)
{
	l = 0;
	int i;
	for (; x!=g[x]; x=g[x]) s[++l] = x;

	for (i=1; i<=l; i++) g[s[i]] = x;

	return x;
}

int main()
{
	freopen("set.in", "r", stdin);
	freopen("set.out", "w", stdout);

	int t, T, x, y;
	ll i, j, last, now;

	scanf("%d ", &T);

	for (i=2; i<=maxx; i++)
		if (u[i] == 0) 
			for (j=2*i; j<maxx; j+=i) u[j] = 1;

	for (t=1; t<=T; t++)
	{
		scanf("%lld %lld %lld ", &A, &B, &P);

		for (i=0; i<=B-A; i++) g[i] = i;

		for (i=P; i<=B-A; i++)
			if (!u[i])
			{
				if (A%i==0) last = A;	
				else last = (A/i+1) * i;

				for (now=last+i; now<=B; now += i)
				{
					x = find(now-A);
					y = find(last-A);
					if (g[x] != g[y]) g[g[x]] = g[y];
					last = now;
				}
			}

		sol = 0;

		for (i=0; i<=B-A; i++)
			if (find(i) == i) sol++;

		printf("Case #%d: %d\n", t, sol);
	}

	return 0;
}
