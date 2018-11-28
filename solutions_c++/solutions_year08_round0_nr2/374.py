#include <stdio.h>
#include <algorithm>
using namespace std;

int sa[128];
int ea[128];
int sb[128];
int eb[128];

int main() 
{
	int n,na,nb,t;
	int x,a,b;
	int i,j,k;
	int h,m;

	scanf("%d",&n);
	for(x=1;x<=n;x++)
	{
		scanf("%d%d%d",&t,&na,&nb);
		for(i=0;i<na;i++)
		{
			scanf("%d:%d",&h,&m);
			sa[i]=h*60+m;
			scanf("%d:%d",&h,&m);
			ea[i]=h*60+m+t;
		}
		for(i=0;i<nb;i++)
		{
			scanf("%d:%d",&h,&m);
			sb[i]=h*60+m;
			scanf("%d:%d",&h,&m);
			eb[i]=h*60+m+t;
		}

		sort(sa,sa+na);
		sort(ea,ea+na);
		sort(sb,sb+nb);
		sort(eb,eb+nb);

		a=na;
		b=nb;

		for(i=j=0;i<na;i++)
		{
			for(;j<nb;j++)
			{
				if(ea[i]<=sb[j])
				{
					b--;
					j++;
					break;
				}
			}
		}

		for(i=j=0;i<nb;i++)
		{
			for(;j<na;j++)
			{
				if(eb[i]<=sa[j])
				{
					a--;
					j++;
					break;
				}
			}
		}

		printf("Case #%d: %d %d\n",x,a,b);
	}

	return 0;
}
