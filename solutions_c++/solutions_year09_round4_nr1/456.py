#include <cstdio>
#include <cstring>

int T,N;
char g[64][64];
int r[64];

void init()
{
	int i,j;
	
	scanf("%d",&N);
	memset(r,0,sizeof(r));
	for (i=1;i<=N;i++)
	{
		for (j=1;j<=N;j++)
		{
			scanf("%1s",&g[i][j]);
			if (g[i][j]=='1')
				r[i]=j;
		}
	}
	
}

int work()
{
	int i,j,k,num;
	int tot=0;
	
	for (i=N;i>=1;i--)
	{
		num=0;
		for (j=i;j>=1;j--)
		{
			for (k=1;k<=i;k++)
			{
				if (r[k]==j)
					num++;
			}
			if (i-j+1==num)
				break;
		}
		
		for (k=i;k>=1;k--)
		{
			if (r[k]>=j)
				break;
		}
		
		tot+=i-k;
		for (j=k;j<i;j++)
		{
			r[j]=r[j+1];
		}
	}
	
	return tot;
}

int main()
{
	int i;
	
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	scanf("%d",&T);
	for (i=1;i<=T;i++)
	{
		init();
		printf("Case #%d: %d\n",i,work());
	}
	
	return 0;
}
