#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int sum[1005];
long long p[2005];
long long r,k,n;
long long to[1005];
long long cy_cnt=0,cy_val;
bool visit[1005];
long long val[1005];
 
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	int i,j;
	int T,case_cnt=0;
	scanf("%d",&T);
	while(T--)
	{
		memset(visit,0,sizeof(visit));
		cy_cnt=cy_val=0;
		//sum[0]=0;
		scanf("%lld%lld%lld",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%lld",&p[i]);
			//sum[i]=sum[i-1]+p[i];
		}
		long long res=0;
		long long temp=0;
		for(i=0;i<n;i++)
			p[n+i]=p[i];
		for(i=0;i<n;i++)
		{
			temp=0;
			for(j=i;j<i+n;j++)
			{
				temp+=p[j];
				if(temp>k)
				{
					temp-=p[j];
					break;
				}
			}
			to[i]=(j-1)%n;
			val[i]=temp;
		}
		int pos=-1;
		int cnt=0;
		while(cnt<r)
		{
			pos=(pos+1)%n;
			res+=val[pos];
			pos=to[pos];
			cnt++;
		}
		printf("Case #%d: %lld\n",++case_cnt,res);
	}
}