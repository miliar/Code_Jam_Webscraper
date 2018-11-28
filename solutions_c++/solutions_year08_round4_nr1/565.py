#include <stdio.h>
#include <string.h>

#define M 10000

short t[M][2];
bool g[M],c[M];

int main() 
{
	int n,m,v;
	int i,j,k;
	int x,y;
	
	scanf("%d",&n);
	for(k=1;k<=n;k++)
	{
		memset(t,-1,sizeof(t));
		scanf("%d%d",&m,&v);
		
		j=(m-1)/2;
		for(i=0;i<j;i++)
		{
			scanf("%d%d",&x,&y);
			g[i]=(x==1);
			c[i]=(y==1);
		}
		for(;i<m;i++)
		{
			scanf("%d",&x);
			t[i][x]=0;
		}
		
		for(i=j-1;i>=0;i--)
		{
			x=(i<<1)+1;
			y=x+1;
			if(g[i]==1)
			{
				//and
				if(t[x][1]!=-1 && t[y][1]!=-1)
				{
					j=t[x][1]+t[y][1];
					if(j<t[i][1] || t[i][1]==-1) t[i][1]=j;
				}
				if(t[x][0]!=-1)
				{
					j=t[x][0];
					if(j<t[i][0] || t[i][0]==-1) t[i][0]=j;
				}
				if(t[y][0]!=-1)
				{
					j=t[y][0];
					if(j<t[i][0] || t[i][0]==-1) t[i][0]=j;
				}
				
				if(c[i])
				{
					if(t[x][0]!=-1 && t[y][0]!=-1)
					{
						j=t[x][0]+t[y][0]+1;
						if(j<t[i][0] || t[i][0]==-1) t[i][0]=j;
					}
					if(t[x][1]!=-1)
					{
						j=t[x][1]+1;
						if(j<t[i][1] || t[i][1]==-1) t[i][1]=j;
					}
					if(t[y][1]!=-1)
					{
						j=t[y][1]+1;
						if(j<t[i][1] || t[i][1]==-1) t[i][1]=j;
					}
				}
			}
			else
			{
				//or
				if(t[x][0]!=-1 && t[y][0]!=-1)
				{
					j=t[x][0]+t[y][0];
					if(j<t[i][0] || t[i][0]==-1) t[i][0]=j;
				}
				if(t[x][1]!=-1)
				{
					j=t[x][1];
					if(j<t[i][1] || t[i][1]==-1) t[i][1]=j;
				}
				if(t[y][1]!=-1)
				{
					j=t[y][1];
					if(j<t[i][1] || t[i][1]==-1) t[i][1]=j;
				}

				if(c[i])
				{
					if(t[x][1]!=-1 && t[y][1]!=-1)
					{
						j=t[x][1]+t[y][1]+1;
						if(j<t[i][1] || t[i][1]==-1) t[i][1]=j;
					}
					if(t[x][0]!=-1)
					{
						j=t[x][0]+1;
						if(j<t[i][0] || t[i][0]==-1) t[i][0]=j;
					}
					if(t[y][0]!=-1)
					{
						j=t[y][0]+1;
						if(j<t[i][0] || t[i][0]==-1) t[i][0]=j;
					}
				}
			}
		}
		
		printf("Case #%d: ",k);
		if(t[0][v]==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",t[0][v]);
	}
	
	return 0;
}
