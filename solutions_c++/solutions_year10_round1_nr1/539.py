#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int z,n,K,dx[]={-1,-1,-1,0,0,1,1,1},dy[]={-1,0,1,-1,1,-1,0,1};
char map[1000][1000];
//	(check(i,j,dx[d],dy[d],map[i][j],0)

inline bool check(int x,int y,int dx,int dy,char c,int deep)
{
	//cout<<x<<' '<<y<<' '<<dx<<' '<<dy<<' '<<c<<' '<<deep<<endl;
	if(K==deep)
		return true;
	if(map[x][y]!=c)
		return 0;
	return check(x+dx,y+dy,dx,dy,c,deep+1);
}

int main()
{
	freopen("gcjr2a.in","r",stdin);
	freopen("gcjr2a.out","w",stdout);
	scanf("%d",&z);
	for(int zz=1;zz<=z;++zz)
	{
		memset(map,0,sizeof(map));
		scanf("%d %d\n",&n,&K);
		bool flag1=0,flag2=0;
		for(int i=101;i<=n+100;++i)
		{
			for(int j=101;j<=n+100;++j)
				scanf("%c",&map[i][j]);
			scanf("%\n");
		}
		for(int i=101;i<=n+100;++i)
		{
			int k=n+100;
			for(int j=n+100;j>100;--j)
				if(map[i][j]!='.')
				{
					if(k==j)
					{
						--k;
						continue;
					}
					map[i][k--]=map[i][j];
					map[i][j]='.';
				}
		}
		for(int i=101;i<=n+100;++i)
			for(int j=101;j<=n+100;++j)
				for(int d=0;d<8;++d)
					if(map[i][j]!='.'&&check(i,j,dx[d],dy[d],map[i][j],0))
						if(map[i][j]=='R')
							flag1=1;
						else
							flag2=1;
		if(flag1&&flag2)
		{
			printf("Case #%d: %s\n",zz,"Both");
			continue;
		}
		if(flag1)
			printf("Case #%d: %s\n",zz,"Red");
		if(flag2)
			printf("Case #%d: %s\n",zz,"Blue");
		if(!(flag2||flag1))
			printf("Case #%d: %s\n",zz,"Neither");
	}
	return 0;
}
