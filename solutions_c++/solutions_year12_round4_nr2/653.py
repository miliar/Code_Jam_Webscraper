#include <stdio.h>
#include <algorithm>

using namespace std;

struct s
{
	int x,y;
};

s ans[13];
int r[13],arr1[13];

bool cmp(int a,int b)
{
	return r[a]>r[b];
}

int main()
{
	freopen("b.txt","r",stdin);
	freopen("b.out","w",stdout);
	int test,cas,n,L,W,i,j,prev,now,l,p,k,reqx,reqy;
	bool d;
	bool sw;
	scanf("%d",&test);
	for (cas=1;cas<=test;cas++)
	{
		scanf("%d%d%d",&n,&L,&W);
		sw=0;
		if (L<W)
		{
			L^=W^=L^=W;
			sw=1;
		}
		for (i=0;i<n;i++) scanf("%d",&r[i]);
		for (i=0;i<n;i++) arr1[i]=i;
		sort(arr1,arr1+n,cmp);
		prev=0;
		j=0;
		for (i=0;j<n;i++)
		{
			now=0;
			d=0;
			for (;j<n;j++)
			{
				k=arr1[j];
				if (now==0) reqx=0;
				else reqx=r[k];
				if (i==0) reqy=0;
				else reqy=r[k];
				if (now+reqx>L||prev+reqy>W) break;
				ans[k].x=now+reqx;
				ans[k].y=prev+reqy;
				now+=reqx+r[k];
				if (!d)
				{
					p=reqy;
					l=k;
					d=1;
				}
			}
			prev+=p+r[l];
			now=0;
		}
		printf("Case #%d:",cas);
		for (i=0;i<n;i++)
		{
			if (!sw) printf(" %d %d",ans[i].x,ans[i].y);
			else printf(" %d %d",ans[i].y,ans[i].x);
		}
		printf("\n");
	}
	return 0;
}
