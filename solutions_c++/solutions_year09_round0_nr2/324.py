#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>

using namespace std;

const int INF = 30000;

char out[30];
int label[110][110];
bool flag[110][110];
int map[110][110];
int h,w;
int cc;

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

bool check(int x,int y)
{
	if(x<1 || x>h || y<1 || y>w) return false;
	return true;
}

int dfs(int x,int y)
{
	if(label[x][y]) return label[x][y];
	int low=INF,pos=-1;
	int i;
	int xx,yy;
	for(i=0;i<4;i++)
	{
		xx=x+dx[i],yy=y+dy[i];
		if(check(xx,yy) && map[x][y]>map[xx][yy] && map[xx][yy]<low)
		{
			low=map[xx][yy];
			pos=i;
		}
	}
	if(pos==-1)
		label[x][y]=cc++;
	else label[x][y]=dfs(x+dx[pos],y+dy[pos]);
	return label[x][y];
}

struct Pos
{
	int x,y;
	bool operator <(const Pos &b) const
	{
		return map[x][y]<map[b.x][b.y];
	}
};

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t,ca=1;
	int i,j;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&h,&w);
		for(i=1;i<=h;i++)
			for(j=1;j<=w;j++)
				scanf("%d",&map[i][j]);
		for(i=0;i<=h;i++)
			map[i][0]=map[i][w+1]=INF;
		for(i=0;i<=w;i++)
			map[0][i]=map[h+1][i]=INF;
		cc=1;
		memset(label,0,sizeof(label));
		priority_queue<Pos> q;
		Pos tt;
		for(i=1;i<=h;i++)
		{
			for(j=1;j<=w;j++)
			{
				tt.x=i,tt.y=j;
				q.push(tt);
			}
		}
		while(!q.empty())
		{
			tt=q.top();q.pop();
			if(label[tt.x][tt.y]!=0) continue;
			dfs(tt.x,tt.y);
		}
		int k=0;
		memset(out,-1,sizeof(out));
		for(i=1;i<=h;i++)
			for(j=1;j<=w;j++)
				if(out[label[i][j]]==-1)
					out[label[i][j]]='a'+(k++);
		printf("Case #%d:\n",ca++);
		for(i=1;i<=h;i++)
		{
			for(j=1;j<w;j++)
				printf("%c ",out[label[i][j]]);
			printf("%c\n",out[label[i][j]]);
		}
	}
	return 0;
}
