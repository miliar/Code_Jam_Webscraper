#include <iostream>
#include <queue>
#include <map>
using namespace std;

map<int,char> M;
const int maxum = (1<<29);
int G[101][101];
bool visited[101][101];
int root[1000000];
char buf[101][101];
int G2[101][101];
int path[4][2] = {{-1,0},{0,-1},{1,0},{0,1}};

int n,m;
struct node
{
	int x;
	int y;
	node(int a,int b)
	{
		x = a;
		y = b;
	}
};
int select(node Nd)
{
	int h = G[Nd.x][Nd.y];
	int p = -1;
	for(int i = 0;i < 4;i++)
	{
		int tx = Nd.x + path[i][0];
		int ty = Nd.y + path[i][1];
		if(tx < 0 || tx >= n) continue;
		if(ty < 0 || ty >= m) continue;
	//	if(visited[tx][ty]) continue;
		if(G[tx][ty] < h)
		{
			h = G[tx][ty];
			p = i;
		}
	}
	return p;
}
bool in (int a,int b)
{
	if(a < 0 || a >= n) return 0;
	if(a < 0 || a >= m) return 0;
	return 1;
}

void bfs(int sx,int sy)
{
	visited[sx][sy] = 1;
	queue<node> Q;
	Q.push(node(sx,sy));
	int cnt = 1;
	while(!Q.empty())
	{
		node tmp = Q.front();
		Q.pop();
		int pos = select(tmp);
		if(pos != -1)
		{
			int tx = tmp.x + path[pos][0];
			int ty = tmp.y + path[pos][1];
			if(!visited[tx][ty])
			{
				visited[tx][ty] = true;
				//G2[tx][ty] = k;
				Q.push(node(tx,ty));
			 root[tmp.x * 1000 + tmp.y] = tx * 1000 + ty;
				cnt ++;
			}
			else 
			{
				root[tmp.x * 1000 + tmp.y] = tx * 1000 + ty;
				return;
			}
		}
	}
}
void init()
{
	for(int i = 0;i < 1000000;i++)
		root[i] = i;
}
int find(int a)
{
	if(root[a] != a)
		root[a] = find(root[a]);
	return root[a];
}
int main()
{
	int t;freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%d",&t);
	int ccc = 0;
	
	while(t --)
	{
		//g = 0;
		init();
		M.clear();
		memset(visited,0,sizeof visited);
		scanf("%d%d",&n,&m);
		for(int i = 0;i < n;i++)
			for(int j = 0;j < m;j++)
			{
				scanf("%d",&G[i][j]);
			}
		for(int i = 0;i < n;i++)
			for(int j = 0;j < m;j++)
			{
				bfs(i,j);
			}
		int k = 0;
		for(int i = 0;i < n;i++)
		{
			for(int j = 0;j < m;j++)
			{
				int r = find(i * 1000 + j);
				if(M.find(r) == M.end())
				{
					buf[i][j] = 'a' + k ;
					M[r] =  'a' + k ++;
				}
				else 
					buf[i][j] = M[r];
			}
		}
		printf("Case #%d:\n",++ccc);
		for(int i = 0;i < n;i++)
		{
			for(int j = 0;j < m;j++)
				printf("%c ",buf[i][j]);
			printf("\n");
		}

	}
	return 0;
}