#include<stdio.h>
/*int x[1005][4];
int xx[1005][4];
int set[1005];
int find(int a)
{
	if(set[a]==a) return a;
	return (set[a]=find(set[a]));
}
void un(int a,int b)
{
	int sa=find(a);
	int sb=find(b);
	if(xx[sa][0]>xx[sb][0]) xx[sa][0]=xx[sb][0];
	if(xx[sa][1]>xx[sb][1]) xx[sa][1]=xx[sb][1];
	if(xx[sa][2]<xx[sb][2]) xx[sa][2]=xx[sb][2];
	if(xx[sa][3]<xx[sb][3]) xx[sa][3]=xx[sb][3];
	set[sb]=find(sa);
	return;
}*/


char map[1001][1001];
int main()
{
	freopen("c-small.in","r",stdin);
	freopen("c-small.out","w",stdout);
	int tt,t;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		printf("Case #%d: ",t);
		int n;
		scanf("%d",&n);
		
		int x1,y1,x2,y2;
		for(int i=0;i<=100;i++)
		{
			for(int j=0;j<=100;j++)
			{
				map[i][j]='0';
			}
		}
		for(int i=0;i<n;i++)
		{
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(int x=x1;x<=x2;x++)
				for(int y=y1;y<=y2;y++)
					map[x][y]='1';
		}
		
		int cnt=0;
		while(1)
		{
			bool g=0;
			for(int i=100;i>0;i--)
			{
				for(int j=100;j>0;j--)
				{
					if(map[i][j]=='1') g=1;
					if(map[i][j]=='0' && map[i-1][j]=='1' && map[i][j-1]=='1') map[i][j]='1';
					if(map[i][j]=='1' && map[i-1][j]=='0' && map[i][j-1]=='0') map[i][j]='0';
				}
			}
			if(g==0) break;
			cnt++;
		}
		
		printf("%d\n",cnt);
		
/*		for(int i=0;i<n;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&x[i][j]);
				xx[i][j]=x[i][j];
			}
			set[i]=i;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if(!(x[i][0]>x[j][2] || x[i][2]<x[j][0] || x[i][1]>x[j][3] || x[i][3]<x[j][1]))
				{
					un(i,j);
				}
			}
		}
		int ans=0;
		for(int i=0;i<n;i++)
		{
			int cc=(xx[i][2]-xx[i][0])+(xx[i][3]-xx[i][0])-1
			if()
		}
		printf("%d\n",ans);*/
	}
	return 0;
}
