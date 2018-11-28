#include <cstring>
#include <cstdio>
using namespace std;

int N,M;
int m[101][101];
int s[101][101];
int id[10000];

int dir[4][2] = {-1,0,0,-1,0,1,1,0};

int DFS(int loc)
{
	int nx,ny;
	int x = loc/M;
	int y = loc%M;
	int i,ret,lowest,lx,ly;
	if (s[x][y]!=-1) return s[x][y];
	lowest = 0x7f7f7f7f;
	for (i=0;i<4;++i)
	{
		nx = x+dir[i][0];
		ny = y+dir[i][1];
		if (ny<0||ny>=M||nx<0||nx>=N) continue;
		if (m[nx][ny]<lowest)
		{
			lowest = m[nx][ny];
			lx = nx, ly = ny;
		}
	}
	if (lowest>=m[x][y])
	{
		ret = loc;
	}
	else ret = DFS(lx*M+ly);
	return s[x][y] = ret;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,cases,cas,cnt;
	scanf("%d",&cases);
	for (cas=1;cas<=cases;++cas)
	{
		scanf("%d %d",&N,&M);
		for (i=0;i<N;++i)
		{
			for (j=0;j<M;++j) scanf("%d",&m[i][j]);
		}
		memset(s,-1,sizeof(s));
		for (i=0;i<N;++i)
		{
			for (j=0;j<M;++j)
			{
				DFS(i*M+j);
			}
		}
		memset(id,-1,sizeof(id));
		cnt = 'a';
		printf("Case #%d:\n",cas);
		for (i=0;i<N;++i)
		{
			for (j=0;j<M;++j)
			{
				if (j) printf(" ");
				if (id[s[i][j]]==-1)
				{
					id[s[i][j]]=cnt++;
				}
				printf("%c",id[s[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}

