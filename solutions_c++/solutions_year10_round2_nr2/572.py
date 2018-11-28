#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

struct node
{
	int x,y;
	bool set;
};
node num[100];

bool cmp(node a,node b)
{
	if(a.x<b.x)
	{
		return true;
	}
	else if(a.x==b.x)
	{
		if(a.y>b.y)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	else
	{
		return false;
	}
}

int main(void)
{
	int t;
	int yy=0;
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n,k,b,ti;
		yy++;
		scanf("%d%d%d%d",&n,&k,&b,&ti);
		int i,j;
		for(i=0;i<n;i++)
		{
			scanf("%d",&num[i].x);
			num[i].x=b-num[i].x;
		}
		for(i=0;i<n;i++)
		{
			scanf("%d",&num[i].y);
			num[i].set=false;
		}
		sort(num,num+n,cmp);
		int ans=0;
		int kk=0;
		for(i=0;i<n;i++)
		{
			if(ti*num[i].y>=num[i].x)
			{
				for(j=i-1;j>=0;j--)
				{
					if(num[j].set==false)
					{
						ans++;
					}
				}
				num[i].set=true;
				kk++;
			}
			if(kk==k)
			{
				break;
			}
		}
		if(kk==k)
		{
			printf("Case #%d: %d\n",yy,ans);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",yy);
		}
	}
	return 0;
}
