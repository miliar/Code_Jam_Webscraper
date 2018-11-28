#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct {	int a , b;	}	P;
P a[2];
int sgn(int a)
{
	return (a > 0)-(a<0);
}
int main()
{
	int i ,j  , n, t , cas = 1;
	freopen("A-small-attempt0.in", "r",stdin);
	freopen("a.out" , "w" , stdout);
	scanf("%d" , &t);
	while ( t-- )	{
		scanf("%d" , &n);
		
		for (i = 0;i < n;i ++)	{
			scanf("%d%d" , &a[i].a, &a[i].b);
		}
		
		printf("Case #%d: " , cas ++);
		if (n==1)	{
			printf("0\n");
		}	else	{
			if (sgn(a[0].a-a[1].a)*sgn(a[0].b-a[1].b)>0)
				printf("0\n");
			else printf("1\n");
		}
	}
}