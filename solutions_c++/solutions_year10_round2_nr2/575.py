#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int text,i,j;
	int n,b,k,t;
	int p,q;
	int pointx[200];
	int speed[200];
	bool isvalid[200];
	int swapp[200];
	scanf("%d",&text);
	for (i=1;i<=text;i++)
	{
		int haha=0;
		memset(swapp,0xff,sizeof(swapp));
		memset(isvalid,false,sizeof(isvalid));
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for (j=1;j<=n;j++)
		{
			scanf("%d",&pointx[j]);
		}
		for (j=1;j<=n;j++)
		{
			scanf("%d",&speed[j]);
		}
		for (p=n;p>=1;p--)
		{
			if (pointx[p]+t*speed[p]>=b)
			{
				isvalid[p]=true;
			}
		}
		int flag=0;
		for (p=1;p<=n;p++)
		{
			if (isvalid[p])
			{
				swapp[p]=0;
				flag++;
				for (q=p+1;q<=n;q++)
				{
					if (!isvalid[q])
					{
						swapp[p]++;
					}
				}
			}
		}
		if (flag<k)
		{
			printf("Case #%d: IMPOSSIBLE\n",i);
		}
		else 
		{
			sort(swapp+1,swapp+n+1);
			int ans=0,num=0;
			for (p=1;p<=n;p++)
			{
				if (swapp[p]!=-1)
				{
					num++;
					ans+=swapp[p];
					if (num>=k)
					{
						break;
					}
				}
			}
			printf("Case #%d: %d\n",i,ans);
		}
		
	
	}
	return 0;
}