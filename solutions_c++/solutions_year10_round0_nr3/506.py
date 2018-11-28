#include <string.h>
#include <iostream>
using namespace std;
int main()
{
	int t,i,j,l;
	int r,k,n,g[1005];
	int h[1005];
	int hh[1005];
	bool isused[1005];
	__int64 haha=0;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		memset(isused,false,sizeof(isused));
		scanf("%d%d%d",&r,&k,&n);
		haha=0;
		for (j=0;j<n;j++)
		{
			scanf("%d",&g[j]);
			haha+=g[j];
		}
		if(haha<=k)
		{
			__int64 dd=haha*r;
			printf("Case #%d: %I64d\n",i,dd);
		}
		else
		{
			int tmp=0;
			for (j=0;j<n;j++)
			{
				tmp=0;
				for (l=j;;l=(l+1)%n)
				{
					if (tmp+g[l]>k)
					{
						break;
					}
					tmp+=g[l];
				}
				h[j]=tmp;
				hh[j]=l;
			}
			__int64 ans=0;
			int tt=0;
			int jj=0;
			for (j=1;j<=r;j++)
			{				
				if (isused[tt])
				{
					break;
				}
				jj++;
				ans=ans+h[tt];
				isused[tt]=true;
				tt=hh[tt];				
			}
			__int64 anss=ans;
			int tmpp=1;
			int ttt=tt;
			__int64 tmpans=h[tt];
			while (hh[ttt]!=tt)
			{
				ttt=hh[ttt];
				tmpans+=h[ttt];
				tmpp++;				
			}
			int sz=(r-jj+tmpp)/tmpp;
			int tz=(r-jj+tmpp)%tmpp;
			anss+=tmpans*sz;
			for (j=1;j<=tz;j++)
			{
				anss=anss+h[tt];
				tt=hh[tt];
			}
			printf("Case #%d: %I64d\n",i,anss-tmpans);
		}
	}
	return 0;	
}