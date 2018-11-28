#include "stdio.h"
char map[100][100];
int dp[2050],mid[2050],x[100],ok[2050],ll,m,n,t[2050];
int calc(int a,int b)
{
	int c,pre,i;
	c=(a|b);
	pre=0;
	while(c>0)
	{
		i=c%2;
		if(i==1&&pre==1)
			return 0;
		c/=2;
		pre=i;
	}
	return 1;
}
void search(int now,int ste,int step,int s)
{
	if(step==n)
	{
		t[now]=s;
		ok[ll++]=now;
		return;
	}
	if(ste==0)
		search(now*2+1,1,step+1,s+1);
	search(now*2,0,step+1,s);
}
int main()
{
	int tot,kase,i,k,j,num,res;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		ll=0;
		scanf("%d%d",&m,&n);
		search(0,0,0,0);
		for(i=1;i<=m;i++)
		{
			x[i]=0;
			for(k=1;k<=n;k++)
			{
				map[i][k]=getchar();
				if(map[i][k]!='.'&&map[i][k]!='x')
				{
					k--;
					continue;
				}
				x[i]*=2;
				if(map[i][k]=='x')
					x[i]+=1;
			}
		}
		res=0;
		num=(1<<n);
		for(i=0;i<ll;i++)
		{
			if((x[1]|ok[i])==x[1]+ok[i])
				dp[ok[i]]=t[ok[i]];
			else
				dp[ok[i]]=0;
			if(dp[ok[i]]>res)
				res=dp[ok[i]];
			mid[ok[i]]=0;
		}
		for(i=2;i<=m;i++)
		{
			for(k=0;k<ll;k++)
				mid[ok[i]]=0;
			for(k=0;k<ll;k++)
			{
				if((x[i]|ok[k])!=x[i]+ok[k])
					continue;
				for(j=0;j<ll;j++)
				{
					if(calc(ok[j],ok[k])==1&&dp[ok[j]]+t[ok[k]]>mid[ok[k]])
						mid[ok[k]]=t[ok[k]]+dp[ok[j]];
				}
			}
			for(k=0;k<ll;k++)
			{
				dp[ok[k]]=mid[ok[k]];
				if(i==m&&dp[ok[k]]>res)
					res=dp[ok[k]];
			}
		}
		printf("Case #%d: %d\n",kase,res);
	}
	return 0;
}
