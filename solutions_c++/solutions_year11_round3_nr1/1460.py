#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

#define read freopen("A-large(1).in","r",stdin)
#define write freopen("zx.out","w",stdout)
const int N=55;

int row,column;
char map[N][N];

bool BFS(int x,int y)
{
	bool flag1=false, flag2=false, flag3=false;
	int rtx=x, rty=y+1;
	int lbx=x+1, lby=y;
	int rbx=x+1, rby=y+1;
	if(rtx>=0&&rtx<row&&rty>=0&&rty<column&&map[rtx][rty]=='#')
	{
		flag1=true;
		map[rtx][rty]='\\';
	}
	if(lbx>=0&&lbx<row&&lby>=0&&lby<column&&map[lbx][lby]=='#')
	{
		flag2=true;
		map[lbx][lby]='\\';
	}
	if(rbx>=0&&rbx<row&&rby>=0&&rby<column&&map[rbx][rby]=='#')
	{
		flag3=true;
		map[rbx][rby]='/';
	}
	if(flag1&&flag2&&flag3) return true;
	else return false;
}

int main()
{
	read, write;
	int ncase,ans;
	scanf("%d",&ncase);
	for(int ii=1;ii<=ncase;ii++)
	{
		ans=0;
		printf("Case #%d:\n",ii);
		scanf("%d%d",&row,&column);
		for(int i=0;i<row;i++)
			for(int j=0;j<column;j++)
			{
				cin>>map[i][j];
				if(map[i][j]=='#') ans++;
			}
		if(ans%4!=0)
		{
			printf("Impossible\n");
		}
		else if(ans==0)
		{
			for(int i=0;i<row;i++)
			{
				for(int j=0;j<column;j++) printf("%c",map[i][j]);
				printf("\n");
			}
		}
		else
		{
			bool flag=false,ok;
			for(int i=0;i<row;i++)
				for(int j=0;j<column;j++)
				{
					if(map[i][j]=='#')
					{
						map[i][j]='/';
						ok=BFS(i,j);
						if(!ok) flag=true;
					}
				}
			if(!flag)
			{
				for(int i=0;i<row;i++)
				{
					for(int j=0;j<column;j++) printf("%c",map[i][j]);
					printf("\n");
				}
			}
			else printf("Impossible\n");
		}
	}
	return 0;
}
	
