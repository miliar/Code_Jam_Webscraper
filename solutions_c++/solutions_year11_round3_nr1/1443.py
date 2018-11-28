#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

char map[100][100];
bool was[100][100];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int R,C;

int calc(int i, int j)
{
	was[i][j]=true;
	int res=1;
	for(int d=0; d<4; ++d)
	{
		int ni=i+dx[d], nj=j+dy[d];
		if(ni<0 || ni>=R || nj<0 || nj>=C || was[ni][nj] || map[ni][nj]!='#') continue;
		res+=calc(ni,nj);
	}
	return res;
}

int nx[3]={1,0,1};
int ny[3]={0,1,1};
char seq[3]={'\\','\\','/'};

bool build()
{
	for(int i=0; i<R; ++i)
		for(int j=0; j<C; ++j)
		{
			if(map[i][j]!='#') continue;	
			map[i][j]='/';
			for(int d=0; d<3;++d)
			{
				int ni=i+nx[d], nj=j+ny[d];
				if(ni<0 || ni>=R || nj<0 || nj>=C || map[ni][nj]!='#') return false;
				map[ni][nj]=seq[d];
			}
			return build();
		}
	return true;
}

int main()
{

	int T;
	//freopen("input","r",stdin);
	cin >> T;
	for(int tNum=1; tNum<=T; ++tNum)
	{
		cin >> R >> C;
		for(int i=0; i<R; ++i)
			cin >> map[i];
		for(int i=0; i<R; ++i)
			for(int j=0; j<C; ++j)
				was[i][j]=false;
		bool ok=true;
		for(int i=0; i<R; ++i)
			for(int j=0; j<C; ++j)
				if(!was[i][j] && map[i][j]=='#')
				{
					int c=calc(i,j);
					if(c%4!=0)
					{
						ok=false;
					}	
				}
		printf("Case #%d:\n",tNum);
		if(ok)
		{
			if(!build())
				printf("Impossible\n");
			else{
				for(int i=0; i<R; ++i)
				{
					printf("%s\n",map[i]);
				}
			}
		}else	
			printf("Impossible\n");
	}	
	
	return 0;
}
