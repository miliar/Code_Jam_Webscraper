#include<stdio.h>
#define N 1000+10

int group[N];              //每组的人数
int to[N];                 //记录若以i位置为队首，可以玩到的组号
_int64 cntto[N];              //这次玩的人数

int main()
{
	_int64 ans;
	int t,r,k,n,start,i,j,g;       //start为队首组号 
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		ans=0;
		start=0;
		scanf("%d%d%d",&r,&k,&n);
		for(j=0;j<n;++j)
			scanf("%d",&group[j]);
		for(j=0;j<n;++j)
		{
			_int64 cnt=0;
			for(g=j;g<n+j;++g)
				if(cnt+group[g%n]<=k)
					cnt+=group[g%n];
				else break;
			if(cnt<=k)
			{
				to[j]=(g-1)%n;
				cntto[j]=cnt;
			}
			else
			{
				to[j]=-1;                      //位置不够队首组的人使用
				cntto[j]=0;
			}
		}	
		for(j=0;j<r;++j)
		{
			if(to[start]!=-1)
			{
				ans+=cntto[start];
				start=(to[start]+1)%n;
			}
			else break;
		}
		printf("Case #%d: %I64d\n",i,ans);
	}
	return 0;
}