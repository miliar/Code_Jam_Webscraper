#include <stdio.h>
#include <string.h>

#define inf 1000000000
int icost,dcost;

int a[110];
int diff,n;

int dp[260][110];

inline int min(int a,int b)
{
	return a<b?a:b;
}

inline int myabs(int a)
{
	return a<0?-a:a;
}

int table[260][260];

int getcost(int a,int b)
{
	if(diff==0)
	{
        if(a==b)
			return 0;
		else
			return inf;
	}
	else
		return icost * (table[a][b]-1);
}

int solve(int last,int ith)
{
	int i;
	if(ith==n)
		return 0;
	if(last==-1)
	{
		int ret = solve(last,ith+1) + dcost;
		for(i=0;i<=255;i++)
            ret = min(ret, myabs(a[ith] - i) + solve(i,ith+1));
		return ret;
	}
	else 
	{
		if(dp[last][ith]>=0)
			return dp[last][ith];
		dp[last][ith] = solve(last,ith+1) + dcost;
		for(i=0;i<=255;i++)
            dp[last][ith] = min(dp[last][ith], getcost(i,last) + myabs(a[ith] - i) + solve(i,ith+1));
	}
	return dp[last][ith];
}

void init()
{
	int i,j,k;
	for(i=0;i<=255;i++)
		for(j=0;j<=255;j++)
			if(myabs(i-j)<=diff)
				table[i][j] = 1;
			else
				table[i][j] = inf; 
			
			for(k=0;k<=255;k++)
				for(i=0;i<=255;i++)
					for(j=0;j<=255;j++)
							table[i][j] = min(table[i][j],table[i][k]+table[k][j]);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ct;scanf("%d",&ct);
	int caset = 1;
	while(ct--)
	{
		int i;
        scanf("%d%d%d%d",&dcost,&icost,&diff,&n);
		init();
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
	
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: ",caset++);
		printf("%d\n",solve(-1,0));
	}
	return 0;
}