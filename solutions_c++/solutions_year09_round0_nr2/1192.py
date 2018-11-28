#include<stdio.h>

int n,m;
int map[101][101];
char ans[101][101],label[10001];

void process()
{
	int i,j,k,x,y,nx,ny,way[4][2]={{-1,0},{0,-1},{0,1},{1,0}},min,p;
	char bas='a';
	for(i=0;i<10000;i++) label[i]=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			x=i; y=j;
			while(1)
			{
				min=2100000000; p=-1;
				for(k=0;k<4;k++)
				{
					nx=x+way[k][0]; ny=y+way[k][1];
					if(nx<0 || nx>=n || ny<0 || ny>=m) continue;
					if(map[nx][ny]<min){ min=map[nx][ny]; p=k; }
				}
				if(p>-1 && min<map[x][y])
				{
					x+=way[p][0]; y+=way[p][1];
				}
				else break;
			}
			if(label[x*m+y]==0)
			{
				label[x*m+y]=bas;
				ans[i][j]=bas++;
			}
			else
			{
				ans[i][j]=label[x*m+y];
			}
		}
	}
}

int main()
{
	int i,j,k,t;
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&m);
		for(j=0;j<n;j++)
		{
			for(k=0;k<m;k++)
			{
				scanf("%d",&map[j][k]);
			}
		}
		process();
		printf("Case #%d:\n",i);
		for(j=0;j<n;j++)
		{
			for(k=0;k<m;k++)
			{
				printf("%c ",ans[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}