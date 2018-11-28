#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn=10;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int r,k,n,i,sum,ans,nCase,case_Id=0,now,total;
	int g[maxn+1];
	scanf("%d",&nCase);
	while(nCase--)
	{
		scanf("%d%d%d",&r,&k,&n);
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&g[i]);
			sum+=g[i];
		}
		if(sum<=k)
			ans=r*sum;
		else
		{
			now=ans=0;
			while(r)
			{
				total=0;
				for(i=now;;i++)
				{
					if(total+g[i%n]>k)
						break;
					total+=g[i%n];
				}
				now=i;
				ans+=total;
				r--;
			}
		}
		printf("Case #%d: %d\n",++case_Id,ans);
	}
	return 0;
}