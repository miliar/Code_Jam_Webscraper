#include <stdio.h>
#include <string>

#define maxn 1010
#define maxl 10

int n, m;
int sol, rez, best, nr;
char a[maxn], b[maxn];
int u[maxl], p[maxl];

void back(int k)
{
	if (k == m)
	{
		rez = 1;
		nr++;

		int i, j;

		for (i=0; i<n; i+=m)
			for (j=0; j<m; j++) b[i+j] = a[i+p[j]];

		for (i=1; i<n; i++) 
			if (b[i] != b[i-1]) rez++;

		if (rez < sol) 
		{
			sol = rez;
			best = nr;
		}
	}
	else {
			 int i;
			 for (i=0; i<m; i++)
				 if (!u[i])
				 {
					 p[k] = i;
					 u[i] = 1;
					 back(k+1);
					 u[i] = 0;
				 }
		 }
}

int main()
{
	freopen("perm.in", "r", stdin);
	freopen("perm.out", "w", stdout);

	int t, T;

	scanf("%d ", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d " , &m);
		scanf("%s ", a);

		n = strlen(a);
		sol = n+1;		

		back(0);

		printf("Case #%d: %d\n", t, sol);
	}

	return 0;
}
