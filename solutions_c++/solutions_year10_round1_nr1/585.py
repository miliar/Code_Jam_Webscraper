#include<stdio.h>
char map[101][101];
int cnt[101][101];
int ry[4]={1,0,-1,1};
int rx[4]={0,1,1,1};
int main()
{
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int tt,t;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++) scanf("%s",map[i]);
		
		for(int i=0;i<n;i++)
		{
			int cc=0;
			for(int j=n-1;j>=0;j--)
			{
				if(map[i][j]=='.') cc++;
				else map[i][j+cc]=map[i][j];
			}
			while(cc>0)
			{
				cc--;
				map[i][cc]='.';
			}
		}
		
		
		int R=0,B=0;
		
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cnt[i][j]=0;
		for(int j=0;j<n;j++)
		{
			for(int i=0;i<n;i++)
			{
				if(map[i][j]=='.') continue;
				int y=i;
				int x=j;
				int cc=0;
				while(y>=0 && y<n && x>=0 && x<n && cnt[y][x]==0 && map[y][x]==map[i][j])
				{
					cnt[y][x]=++cc;
					y+=ry[0];
					x+=rx[0];
				}
				if(map[i][j]=='R' && R<cc) R=cc;
				if(map[i][j]=='B' && B<cc) B=cc;
			}
		}
		
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cnt[i][j]=0;
		for(int j=0;j<n;j++)
		{
			for(int i=0;i<n;i++)
			{
				if(map[i][j]=='.') continue;
				int y=i;
				int x=j;
				int cc=0;
				while(y>=0 && y<n && x>=0 && x<n && cnt[y][x]==0 && map[y][x]==map[i][j])
				{
					cnt[y][x]=++cc;
					y+=ry[1];
					x+=rx[1];
				}
				if(map[i][j]=='R' && R<cc) R=cc;
				if(map[i][j]=='B' && B<cc) B=cc;
			}
		}


		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cnt[i][j]=0;
		for(int j=0;j<n;j++)
		{
			for(int i=0;i<n;i++)
			{
				if(map[i][j]=='.') continue;
				int y=i;
				int x=j;
				int cc=0;
				while(y>=0 && y<n && x>=0 && x<n && cnt[y][x]==0 && map[y][x]==map[i][j])
				{
					cnt[y][x]=++cc;
					y+=ry[2];
					x+=rx[2];
				}
				if(map[i][j]=='R' && R<cc) R=cc;
				if(map[i][j]=='B' && B<cc) B=cc;
			}
		}


		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cnt[i][j]=0;
		for(int j=0;j<n;j++)
		{
			for(int i=0;i<n;i++)
			{
				if(map[i][j]=='.') continue;
				int y=i;
				int x=j;
				int cc=0;
				while(y>=0 && y<n && x>=0 && x<n && cnt[y][x]==0 && map[y][x]==map[i][j])
				{
					cnt[y][x]=++cc;
					y+=ry[3];
					x+=rx[3];
				}
				if(map[i][j]=='R' && R<cc) R=cc;
				if(map[i][j]=='B' && B<cc) B=cc;
			}
		}
		
		printf("Case #%d: ",t);
		if(R<m && B<m) printf("Neither\n");
		if(R<m && B>=m) printf("Blue\n");
		if(R>=m && B<m) printf("Red\n");
		if(R>=m && B>=m) printf("Both\n");
	}
	return 0;
}
