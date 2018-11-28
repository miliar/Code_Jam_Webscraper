#include<cstdio>
#include<utility>
#include<algorithm>
#include<cstring>
#include<map>
#include<cctype>
#include<cassert>

using namespace std;
typedef pair<int,int> pii;

#define M 105
#define INF 0x3f3f3f3f;

int alt[M][M];
pii sink[M][M];
int h,w;
pii dummy(-1,-1);

pii dfs(int x,int y)
{
	if(sink[x][y]!=dummy)
		return sink[x][y];
	//printf("D %d %d\n",x,y);
	// NWES - SEWN
	int dx[]={1,0,0,-1};
	int dy[]={0,1,-1,0};
	
	int i;
	int malt=alt[x][y]-1;
	int maltdir=-1;
	for(i=0;i<4;++i)
	{
		int nx=x+dx[i];
		int ny=y+dy[i];
		if(nx>=0 && nx<h && ny>=0 && ny<w && alt[nx][ny]<=malt)
		{
			malt=alt[nx][ny];
			maltdir=i;
		}
	}
	//printf("D %d\n",maltdir); 
		if(maltdir==-1)
			return sink[x][y]=make_pair(x,y);
		else
			return sink[x][y]=dfs(x+dx[maltdir],y+dy[maltdir]);
	
}

int main()
{
	int tc,t;
	scanf("%d",&tc);
	
	for(t=1;t<=tc;++t)
	{
		scanf("%d %d",&h,&w);
		int i,j;
		for(i=0;i<h;++i)
			for(j=0;j<w;++j)
			{
				scanf("%d",&alt[i][j]);
				sink[i][j]=dummy;
			}
		
		for(i=0;i<h;++i)
			for(j=0;j<w;++j)
				sink[i][j]=dfs(i,j);
		printf("Case #%d:\n",t);
		
		char c='a';
		map<pii,char> m;
		for(i=0;i<h;++i,puts(""))
			for(j=0;j<w;++j)
			{
				if(j)
					putchar(' ');
				if(m.find(sink[i][j])==m.end())
				{
					assert(islower(c));
					putchar(c);
					m[sink[i][j]]=c;
					++c;
				}
				else
					putchar(m[sink[i][j]]);	
			}
	}
	return 0;
}
