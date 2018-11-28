#include <stdio.h>

int main()
{
	int numCases;
	int xs[100000],ys[100000],n, i,j,k, count;
	long long a,b,c,d,x,y,m;
	
	scanf("%d\n", &numCases);
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		scanf("%d %lld %lld %lld %lld %lld %lld %lld\n", &n,&a,&b,&c,&d,&x,&y,&m);
		xs[0] = x;
		ys[0] = y;
		for (i = 1; i < n; i++)
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			xs[i] = x;
			ys[i] = y;
		}
		count = 0;
		for (i = 0; i < n; i++)
			for (j = i+1; j < n; j++)
				for (k = j+1; k < n; k++)
				{
					if ((xs[i] + xs[j] + xs[k]) % 3 == 0 && (ys[i] + ys[j] + ys[k]) % 3 == 0)
					{
						count++;
					}
				}
		printf("Case #%d: %d\n", curCase, count);
	}
	return 0;
}
