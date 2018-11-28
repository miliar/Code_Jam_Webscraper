#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
struct point
{
	int a,t;
};
point p[1001];
typedef __int64 INT;
int cmp(const void *a,const void *b)
{
	return ((point *)b)->a-((point *)a)->a;
}
int main()
{
	int repeat,i,j,n,m,ri=1;
	int l,t,c;
	INT sum;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		sum=0;
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(i=0;i<c;i++)
		{
			scanf("%d",&p[i].a);
			p[i].t=n/c+(n%c>i);
		}
		for(i=j=0;i<n;i++)
		{
			sum+=p[j].a;
			p[j].t--;
			if( sum*2>t) break;
			j++;
			if( j==c ) j=0;
		}
		p[c].t=1;
		p[c].a=(sum*2-t)/2;
		qsort(p,c+1,sizeof(p[0]),cmp);
		sum=t;
		for(i=0,j=l;i<=c;i++)
		{
			if( j>=p[i].t)
			{
				sum+=p[i].t*p[i].a;
				j-=p[i].t;
			}
			else
			{
				sum+=j*p[i].a+(p[i].t-j)*p[i].a*2;
				j=0;
			}
		}
		printf("Case #%d: %I64d\n",ri++,sum);
	}
	return 0;
}