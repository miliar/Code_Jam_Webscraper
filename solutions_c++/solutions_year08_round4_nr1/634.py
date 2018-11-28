#include <stdio.h>

int origin[10001];
int change[10001];
int min_change[10001][2];

int min(int x,int y)
{
	return (x>y)?y:x;
}

int main()
{
	int g,c;
	int i,n,v;
	int asd,cas;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d",&n,&v);
		for(i=1;i<=n;i++)
		{
			min_change[i][0] = min_change[i][1] = 1000000;
			if( i <= (n-1)/2 )
			{
				scanf("%d %d",&g,&c);
				change[i] = c;	
			}
			else
				scanf("%d",&g);
			origin[i] = g;
			
		}
		for(i=n;i>=1;i--)
		{
			if(i<=(n-1)/2)
			{
				if(origin[i]==0)
				{
					min_change[i][0] = min(min_change[i][0],min_change[2*i][0] + min_change[2*i+1][0]);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][0] + min_change[2*i+1][1]);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][1] + min_change[2*i+1][0]);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][1] + min_change[2*i+1][1]);
				}
				else
				{
					min_change[i][1] = min(min_change[i][1],min_change[2*i][1] + min_change[2*i+1][1]);
					min_change[i][0] = min(min_change[i][0],min_change[2*i][0] + min_change[2*i+1][1]);
					min_change[i][0] = min(min_change[i][0],min_change[2*i][1] + min_change[2*i+1][0]);
					min_change[i][0] = min(min_change[i][0],min_change[2*i][0] + min_change[2*i+1][0]);
				}
				if(change[i]==1)
				{

					min_change[i][0] = min(min_change[i][0],min_change[2*i][0] + min_change[2*i+1][0]+1);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][0] + min_change[2*i+1][1]+1);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][1] + min_change[2*i+1][0]+1);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][1] + min_change[2*i+1][1]+1);
					min_change[i][1] = min(min_change[i][1],min_change[2*i][1] + min_change[2*i+1][1]+1);
					min_change[i][0] = min(min_change[i][0],min_change[2*i][0] + min_change[2*i+1][1]+1);
					min_change[i][0] = min(min_change[i][0],min_change[2*i][1] + min_change[2*i+1][0]+1);
					min_change[i][0] = min(min_change[i][0],min_change[2*i][0] + min_change[2*i+1][0]+1);
				}
			}
			else
				min_change[i][origin[i]] = 0;
		}
		printf("Case #%d: ",asd+1);
		if(min_change[1][v]==1000000)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",min_change[1][v]);
	}
	return 0;
}