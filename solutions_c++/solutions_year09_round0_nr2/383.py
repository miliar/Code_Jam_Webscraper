#include "iostream"
#include "string"
#include "algorithm"
#include "vector"
using namespace std;

#define min(a, b) ((a)<(b)?(a):(b))
#define min3(a, b, c) ((a)<(b)?((a)<(c)?(a):(c)):((b)<(c)?(b):(c)))
#define max(a, b) ((a)>(b)?(a):(b))
#define max3(a, b, c) ((a)>(b)?((a)>(c)?(a):(c)):((b)>(c)?(b):(c)))


int hmap[110][110];
int H, W;

char di[110][110];
int mark[110][110];

int stat=0;

char getDi(int x, int y)
{
	int nowH=hmap[x][y];
	int minH=min(min(hmap[x-1][y], hmap[x+1][y]), min(hmap[x][y-1], hmap[x][y+1]));

	if(minH>=nowH)
		return '$';

	if(hmap[x-1][y]==minH)
		return 'N';
	if(hmap[x][y-1]==minH)
		return 'W';		
	if(hmap[x][y+1]==minH)
		return 'E';
	if(hmap[x+1][y]==minH)
		return 'S';
}


void dfs(int sx, int sy)
{
	mark[sx][sy]=stat;
	if(di[sx-1][sy]=='S')
		dfs(sx-1, sy);
	if(di[sx+1][sy]=='N')
		dfs(sx+1, sy);
	if(di[sx][sy+1]=='W')
		dfs(sx, sy+1);
	if(di[sx][sy-1]=='E')
		dfs(sx, sy-1);	
}

void wuming()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int main()
{
	wuming();

	int i, j, k;

	int T;
	scanf("%d", &T);
	int test=0;
	while(T--)
	{
		memset(mark, -1, sizeof(mark));
		memset(hmap, 0x0f, sizeof(hmap));
		stat=0;

		scanf("%d%d", &H, &W);
		for(i=1; i<=H; ++i)
			for(j=1; j<=W; ++j)
				scanf("%d", &hmap[i][j]);

		for(i=1; i<=H; ++i)
			for(j=1; j<=W; ++j)
				di[i][j]=getDi(i, j);

		for(i=1; i<=H; ++i)
			for(j=1; j<=W; ++j)
				if(di[i][j]=='$')
				{
					++stat;
					dfs(i, j);
				}
		
		char ch[30]={0};
		char nowC='a';
		for(i=1; i<=H; ++i)
			for(j=1; j<=W; ++j)
				if(ch[mark[i][j]]==0)
					ch[mark[i][j]]=nowC++;
		printf("Case #%d:\n", ++test);
		for(i=1; i<=H; ++i)
		{
			for(j=1; j<W; ++j)
				printf("%c ", ch[mark[i][j]]);
			printf("%c\n", ch[mark[i][j]]);
		}	
	}

	return 0;
}