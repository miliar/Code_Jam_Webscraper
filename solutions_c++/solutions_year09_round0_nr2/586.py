#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;
#define MOD 10000
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

int T;
int H,W;
int cnt;
const int C[4][2] = {-1,0,0,-1,0,1,1,0};
int map[100][100];
bool hash[100][100];
int f[100][100];

int dfs(int i, int j)
{
	if(hash[i][j])
		return f[i][j];
	hash[i][j] = true;
	int min = 10000, type;
	for(int k = 0; k < 4; k++)
		if(i+C[k][0]>=0&&i+C[k][0]<H&&j+C[k][1]>=0&&j+C[k][1]<W)
			if(map[i+C[k][0]][j+C[k][1]]<min)
				min = map[i+C[k][0]][j+C[k][1]], type = k;
	if(min>=map[i][j])
		return f[i][j] = cnt++;
	else
		return f[i][j] = dfs(i+C[type][0],j+C[type][1]);
}

void init()
{
	scanf("%d",&T);
}

void solve()
{
	for(int i = 0; i < T; i++)
	{
		cnt = 0;
		memset(hash,0,sizeof(hash));
		scanf("%d %d",&H,&W);
		for(int j = 0; j < H; j++)
			for(int k = 0; k < W; k++)
				scanf("%d",&map[j][k]);
		for(int j = 0; j < H; j++)
			for(int k = 0; k < W; k++)
				dfs(j,k);
		printf("Case #%d:\n",i+1);
		for(int j = 0; j < H; j++)
		{
			printf("%c",f[j][0]+'a');
			for(int k = 1; k < W; k++)
				printf(" %c",f[j][k]+'a');
			printf("\n");
		}
	}
}

void print()
{
}

int main(void)
{
    init();
    solve();
    print();
    return 0;
}
