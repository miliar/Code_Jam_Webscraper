#include<stdio.h>
#include<string.h>
#define N 100+10
#define M 100
int a[N][N];
int v[N][N];
int flag=1;
int h,w;
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int label[M];
int dfs(int x,int y)
{
	int i,dx,dy,min,mx,my;
	min=a[x][y];
	for(i=0;i<4;++i)
	{
		dx=x+dir[i][0];
		dy=y+dir[i][1];
		if(dx<0||dx>=h||dy<0||dy>=w)
			continue;
		if(a[dx][dy]<min)
		{
			min=a[dx][dy];
			mx=dx;
			my=dy;
		}
	}
	if(min==a[x][y])
	{
		if(v[x][y])
			return v[x][y];
		else v[x][y]=flag++;
        return v[x][y];
	}
	v[x][y]=dfs(mx,my);
}
int main()
{
	int t,i,j,k;
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		flag=1;
		memset(v,0,sizeof(v));
		memset(label,-1,sizeof(label));
		scanf("%d%d",&h,&w);
		for(j=0;j<h;++j)
			for(k=0;k<w;++k)
				scanf("%d",&a[j][k]);
			for(j=0;j<h;++j)
				for(k=0;k<w;++k)
					if(!v[j][k])
						dfs(j,k);
			printf("Case #%d:\n",i);
			flag=0;
			for(j=0;j<h;++j)
				for(k=0;k<w;++k)
				{
					if(label[v[j][k]]==-1)
						label[v[j][k]]=flag++;
					v[j][k]=label[v[j][k]];
				}
				for(j=0;j<h;++j)
				{
					printf("%c",v[j][0]+'a');
					for(k=1;k<w;++k)
						printf(" %c",v[j][k]+'a');
					printf("\n");
				}
			
	}
	return 0;
}
