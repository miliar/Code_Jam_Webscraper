#include <iostream>
#include <queue>
using namespace std;
/*
int n,m;
int board[101][101];
bool visited[101][101];
int Bd[101][101];
int path[4][2] = {{-1,0},{0,-1},{1,0},{0,1}};
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

int count = 0;
void bfs(int sx,int sy)
{
	count ++;
	memset(visited,0,sizeof visited);
	queue<node> Q;
	visited[sx][sy] = 1;
	Bd[
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int cnt = 0;
	while(t --)
	{
		scanf("%d%d",&n,&m);
		for(int i = 0;i < n;i++)
			for(int j = 0;j < m;j++)
			{
				scanf("%d",&board[i][j]);
			}
		for(int i = 0;i < n;i++)
			for(int j = 0;j < m;j++)
				bfs(i,j);
	}
	return 0;
}
*/

char * patten = "welcome to code jam";
typedef __int64 ll;
char str[1000];
ll DP[501][20];
void print(int k,int value)
{
	int b[10];
	int c = 3;
	memset(b,0,sizeof b);
	while(value)
	{
		b[c--] = value % 10;
		value /= 10;
	}
	printf("Case #%d: " ,k); 
	for(int i = 0;i < 4;i++)
		printf("%d",b[i]);
	printf("\n");
}

int main()
{
	int t;
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%d",&t);
	getchar();
	int cnt = 0;
	while(t --)
	{
		gets(str);
		int lenp = strlen(patten);
		int lens = strlen(str);
		memset(DP,0,sizeof DP);
		for(int i = 0;i < lens;i++)
		{
			if(str[i] == patten[0])
				DP[i][0] = 1;
		}
		for(int i = 1;i < lens;i++)
		{
			for(int j = 1;j < lenp;j++)
			{
				ll sum = 0;
				if(str[i] == patten[j])
				{
					for(int k = 0;k < i;k++)
						sum += DP[k][j-1];
					sum %= 10000;
				}
				DP[i][j] = sum;
			}
		}
		ll s = 0;
		for(int i = 0;i < lens;i++)
			s += DP[i][lenp-1];
		s  %= 10000;
		print(++cnt,s );
	}
	return 0;
}