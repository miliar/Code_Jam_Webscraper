#include <stdio.h>
#include <string>

#define maxx 100000010

int n, m, A;
short c[maxx];

int det(int x1, int y1, int x2, int y2)
{
	return x1*y2 - x2*y1;
}

int main()
{
	freopen("tri.in", "r", stdin);	
	freopen("tri.out", "w", stdout);

	int i, j, T, A, t, found, x, y;

	scanf("%d ", &T);

	for (t=1; t<=T; t++)
	{
		found = 0;
		scanf("%d %d %d ", &n, &m, &A);

		printf("Case #%d: ", t);

		for (i=0; i<=n; i++)
			for (j=i; j<=m; j++) c[i*j] = 1;

		for (i=0; i<=n && !found; i++)
			for (j=i; j<=m && i*j+A<=n*m && !found; j++) 
				if (c[i*j])
				{
					for (x=0; x<=n && !found; x++)
						for (y=0; y<=m && !found; y++) 
							if (x*y==i*j+A) 
							{
								printf("%d %d %d %d %d %d\n", 0, 0, x, j, i, y);
							    found = 1;
							}
				}

		for (i=0; i<=n; i++)
			for (j=i; j<=m; j++) c[i*j] = 0;

		if (!found) printf("IMPOSSIBLE\n");
	}

	return 0;
}
