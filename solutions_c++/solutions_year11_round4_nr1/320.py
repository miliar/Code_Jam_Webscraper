#include "stdio.h"
#include "string.h"
#include <algorithm>
using namespace std;
#define M 1100000

struct pp
{
	int beg,end;
	int v;
}all[M];

int n,s,x,r,lt,u;

int cmp(pp a,pp b)
{
	return a.beg<b.beg;
}

int cmp1(pp a,pp b)
{
	return a.v<b.v;
}

int main()
{
	int i,j,k,t,tc=1;
	double ans,leftt,ls;
	freopen("gcj/2011.6.4/A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		u=0;
		scanf("%d%d%d%d%d",&x,&s,&r,&lt,&n);
		k=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&all[i].beg,&all[i].end,&all[i].v);
			k+=all[i].end-all[i].beg;
		}
		/*u=n;
		sort(all,all+n,cmp);
		k=0;
		for(i=0;i<n;i++)
		{
			if(all[i].beg>k)
			{
				all[u].beg=k;
				all[u].end=all[i].beg;
				all[u].v=0;
				k=all[u].end;
				u++;
			}
			else
				k=all[i].end;
		}
		if(k<x)
		{
			all[u].beg=k;
			all[u].end=x;
			all[u].v=0;
			u++;
		}*/
		if(k<x)
		{
			all[n].beg=0;
			all[n].end=x-k;
			all[n].v=0;
			n++;
		}
		sort(all,all+n,cmp1);
		ans=0;leftt=lt;
		for(i=0;i<n;i++)
		{
			if(leftt>0)
			{
				if((all[i].end-all[i].beg)/(r+all[i].v*1.0)<leftt)
				{
					ans+=(all[i].end-all[i].beg)/(r+all[i].v*1.0);
					leftt-=(all[i].end-all[i].beg)/(r+all[i].v*1.0);
				}
				else
				{
					ans+=leftt;
					ls=(all[i].end-all[i].beg)-(r+all[i].v*1.0)*leftt;
					ans+=ls/(s+all[i].v);
					leftt=0;
				}
			}
			else
			{
				ans+=(all[i].end-all[i].beg)/(s+all[i].v*1.0);
			}
		}
		printf("Case #%d: ",tc++);
		printf("%.7lf\n",ans);
	}
	return 0;
}

/*
3
10 1 4 1 2
4 6 1
6 9 2
12 1 2 4 1
6 12 1
20 1 3 20 5
0 4 5
4 8 4
8 12 3
12 16 2
16 20 1
*/

