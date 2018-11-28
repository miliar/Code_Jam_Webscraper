#pragma warning(disable:4786)

#include <stdio.h>
#include <vector>
#include <string.h>

using namespace std;


int add(int a, int b)
{
	int c, i;
	if(a>b) {c=a;a=b;b=c;}

	i=1; c=0;
	while(i<=b)
	{
		if((a&i) + (b&i) == i)
			c += i;
		i = i<<1;
	}
	
	return c;
}

int c[1005];


int main()
{
	freopen("1.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t, n, i, j, k, m, x, a, b, ma, maxa;
	
	scanf("%d", &t);
	for(i=1; i<=t; i++)
	{
		scanf("%d", &n);
		memset(c, 0, sizeof(c));
		for(j=0; j<n; j++)
			scanf("%d", &c[j]);

		m=2<<(n-1);
		maxa=-1;
		for(k=1; k<m-1; k++)
		{
			a=0; b=0, ma=0;
			for(x=0; x<n; x++)
			{
				if((k&(1<<x))==(1<<x))
				{
					a = add(a, c[n-1-x]);
					ma += c[n-1-x];
				}
				else
				{
					b = add(b, c[n-1-x]);
				}
			}
			if(a==b && ma>maxa)
				maxa = ma;
		}

		printf("Case #%d: ", i);
		if(maxa==-1)
			printf("NO\n");
		else
			printf("%d\n", maxa);
	}
	
	return 0;
}