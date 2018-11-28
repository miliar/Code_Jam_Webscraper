#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

struct node
{
	int bg,ed;
}a[200],b[200];

int ua[200],ub[200],an,bn,i,j,k,ax,bx,n,t,T,tim,p;

bool cmp(node n1,node n2)
{
	if (n1.bg==n2.bg) return n1.ed<n2.ed;
	return n1.bg<n2.bg;
}

int main()
{
	scanf("%d",&n);
	for (p=1;p<=n;p++)
	{
		memset(a,0,sizeof(a));	memset(b,0,sizeof(b));
		memset(ua,0,sizeof(ua));memset(ub,0,sizeof(ub));
		scanf("%d",&T);
		scanf("%d%d",&an,&bn);
		for (i=0;i<an;i++)
		{
			scanf("%d:%d",&j,&k);			a[i].bg=j*60+k;
			scanf("%d:%d",&j,&k);			a[i].ed=j*60+k;
		}
		sort(a,a+an,cmp);

		for (i=0;i<bn;i++)
		{
			scanf("%d:%d",&j,&k);			b[i].bg=j*60+k;
			scanf("%d:%d",&j,&k);			b[i].ed=j*60+k;
		}
		sort(b,b+bn,cmp);

		ax=bx=0;
		while (1)
		{
			k=100000;
			for (i=0;i<an;i++)
				if (ua[i]==0 && a[i].bg<k)
			{
				j=i+1;k=a[i].bg;
			}
			for (i=0;i<bn;i++)
				if (ub[i]==0 && b[i].bg<k)
			{
				j=-i-1;k=b[i].bg;
			}
			if (k==100000) break;

			if (j>0)
			{
				ax++;
				ua[j-1]=1;
				tim=a[j-1].ed+T;
			}else
			{
				bx++;
				ub[-j-1]=1;
				tim=b[-j-1].ed+T;
			}
			
			while (1)
			{
				if (j>0)
				{
					t=100000;
					for (i=0;i<bn;i++)
						if (ub[i]==0 && b[i].bg>=tim && b[i].bg<t)
					{
						t=b[i].bg;
						j=-i-1;
					}
					if (t<100000)
					{
						ub[-j-1]=1;
						tim=b[-j-1].ed+T;
					}else break;
				}
				else
				{
					t=100000;
					for (i=0;i<an;i++)
						if (ua[i]==0 && a[i].bg>=tim && a[i].bg<t)
					{
						t=a[i].bg;
						j=i+1;
					}
					if (t<100000)
					{
						ua[j-1]=1;
						tim=a[j-1].ed+T;
					}else break;
				}
			}
		}
		printf("Case #%d: %d %d\n",p,ax,bx);
	}
	return 0;
}
