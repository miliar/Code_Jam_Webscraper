#include <stdio.h>
#include <stdlib.h>

struct Line
{
	int l,r;
	int ll,rr;
};

int cmpl(const void *a , const void *b)
{
	return ((Line *)a)->l - ((Line *)b)->l;
}

int cmpr(const void *a , const void *b)
{
	return ((Line *)a)->r - ((Line *)b)->r;
}

Line l[1200];
int T,n;
int main()
{	
	freopen("C:\A-small-attempt0.in","r",stdin);
	freopen("C:\out.out","w",stdout);
	int i , j;
	scanf("%d",&T);

	for(int tt = 0 ; tt < T ; tt++)
	{
		scanf("%d",&n);
		for(i = 0 ; i < n ; i++)
		{
			scanf("%d%d",&l[i].l,&l[i].r);
		}
		qsort(l,n,sizeof(Line),cmpl);
		for(i = 0 ; i < n ; i++)
		{
			l[i].ll = i;
		}
		qsort(l,n,sizeof(Line),cmpr);
		int sum = 0;
		for(i = 0 ; i < n ; i++)
		{
			l[i].rr = i;
			int t = l[i].ll - l[i].rr ;
			sum += (t > 0?t:-t);
		}

		sum/=2;

		printf("Case #%d: %d\n",tt+1,sum);

	}
}