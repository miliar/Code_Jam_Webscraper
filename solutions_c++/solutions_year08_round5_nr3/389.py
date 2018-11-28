#include <stdio.h>

#define INF 10000000

int dp[12][2048];
int n,j;
int used[1000];

void dfs(int value, int depth,int count)
{
	int tmp;
	if(depth==n)
	{
		if(count > dp[j+1][value])
			dp[j+1][value] = count;
	}
	else
	{
		if(used[depth]==0)
		{
			tmp = value;
			if(depth!=0)
				tmp = (tmp | (1<< (depth-1)) );
			if(depth!=n-1)
				tmp = (tmp | (1<< (depth+1)) );
			tmp = (tmp | (1<< depth) );
			dfs(tmp,depth+1,count+1);

			dfs(value,depth+1,count);
		}
		else
		{
			dfs(value, depth+1,count);
		}
	}
}

int main()
{
	int k,t;
	int total=0;
	int count,count2;
	int i;
	char map[101][101];

	int m;
	int cas,asd,max;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&cas);
	count=0;
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",map[i]);
		}



		for(j=0;j<m;j++)
		{
			for(k=0;k<(1<<n);k++)
				dp[j][k]=-INF;
		}

		total=0;
		for(i=n-1;i>=0;i--)
		{
			if(map[i][0]=='.')
				t=0;
			else
				t=1;
			total = 2*total + t;
		}
		dp[0][total]=0;
		for(j=0;j<m-1;j++)
		{

			total=0;
			for(i=n-1;i>=0;i--)
			{
				if(map[i][j+1]=='.')
					t=0;
				else
					t=1;
				total = 2*total + t;
			}

			for(k=0;k<(1<<n);k++)
			{
				if(dp[j][k]==-INF)
					continue;
				for(t=0;t<n;t++)
				{
					if( ((k>> t)&1) == 0)
						used[t] = 0;
					else
						used[t] = 1;
				}
				dfs(total,0,dp[j][k]);
			}
		}
		max = 0;
		for(k=0;k<(1<<n);k++)
		{
			if(dp[m-1][k]==INF)
				continue;
			total=0;
			for(t=0;t<n;t++)
			{
				if( ( (k>>t) & 1)==0)
					total++;
			}
			if(total + dp[m-1][k] > max)
				max = total + dp[m-1][k];
		}
		printf("Case #%d: %d\n",asd+1,max);
	}
	return 0;
}
