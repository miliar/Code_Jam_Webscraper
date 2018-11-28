#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<queue>
using namespace std;

typedef pair<int,int> PII;
const int dx[]={0,1,0,-1};
const int dy[]={1,0,-1,0};

int T;
int h,n,m;
int c[105][105];
int f[105][105];
bool b[105][105];
int t[105][105][4];
int dist[105][105];

bool in(int x,int y)
{
	return x>=0&&y>=0&&x<n&&y<m;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		memset(dist,-1,sizeof(dist));
		queue<PII> Q;
		memset(b,0,sizeof(b));
		scanf("%d%d%d",&h,&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&c[i][j]);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&f[i][j]);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				for(int k=0;k<4;k++)
				{
					int nx=i+dx[k];
					int ny=j+dy[k];
					if(!in(nx,ny))
						continue;
					if(c[nx][ny]-f[i][j]<50||c[nx][ny]-f[nx][ny]<50||c[i][j]-f[nx][ny]<50)
						t[i][j][k]=100000000;
					else
						t[i][j][k]=max(0,(h+50-c[nx][ny]));
				}
		Q.push(make_pair(0,0));
		dist[0][0]=0;
		while(!Q.empty())
		{
			PII tmp=Q.front();
			Q.pop();
			int x=tmp.first;
			int y=tmp.second;
			b[x][y]=false;
			int nt=dist[x][y];
			for(int i=0;i<4;i++)
			{
				int nx=x+dx[i];
				int ny=y+dy[i];
				if(!in(nx,ny))
					continue;
				int tt=0;
				if(nt>=t[x][y][i])
					tt=nt+((h-nt-f[x][y])>=20?10:100);
				else
					tt=t[x][y][i]+((h-t[x][y][i]-f[x][y])>=20?10:100);
				if(nt==0&&t[x][y][i]==0)
					tt=0;
				if(dist[nx][ny]<0||dist[nx][ny]>tt)
				{
					dist[nx][ny]=tt;
					if(!b[nx][ny])
					{
						b[nx][ny]=true;
						Q.push(make_pair(nx,ny));
					}
				}
			}
		}
		printf("Case #%d: %d.%d\n",test,dist[n-1][m-1]/10,dist[n-1][m-1]%10);
	}
	return 0;
}

