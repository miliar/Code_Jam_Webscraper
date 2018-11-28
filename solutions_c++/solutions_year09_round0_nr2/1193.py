#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define maxn 105
#define inf 1000000

int a[maxn][maxn];
int h, w;
int color[maxn][maxn];
char ch[100];
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};

bool valid(int i, int j)
{
	return i >= 0 && j >= 0 && i < h && j < w;
}

bool edge(int i, int j, int &ri, int &rj)
{
	int minv = inf;
	for (int d = 0; d < 4; d++)
	{
		int ii = i + di[d];
		int jj = j + dj[d];
		if (!valid(ii,jj)) continue;
		if (a[ii][jj] < minv)
		{
			minv = a[ii][jj];
			ri = ii;
			rj = jj;
		}
	}
	return minv < a[i][j];
}


void dfs1(int i, int j, int c)
{
	color[i][j] = c;
	for (int d = 0; d < 4; d++)
	{
		int ii = i + di[d];
		int jj = j + dj[d];
		if (!valid(ii,jj)) continue;
		if (color[ii][jj] != -1) continue;
		int i2, j2;
		if (edge(ii,jj,i2,j2))
			if (i2 == i && j2 == j)
				dfs1(ii,jj,c);
	}
}

void solvecase() {
	scanf("%d%d", &h, &w);
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{
			scanf("%d", &a[i][j]);
			//deg[i][j] = 0;
			color[i][j] = -1;
		}
	/*for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{
			int ii, jj;
			if (edge(i,j,ii,jj))
			{
				deg[ii][jj]++;
			}
		}*/
	int cur = 0, x, y;
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{		
			if (color[i][j] == -1 && !edge(i,j,x,y))
			{
				dfs1(i,j,cur);
				cur++;
			}
		}
	memset(ch, 0, sizeof(ch));
	char cc = 'a';
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			if (ch[color[i][j]] == 0)
				ch[color[i][j]] = cc++;
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			printf("%c", ch[color[i][j]]);
			if (j+1 < w) printf(" ");
		}
		printf("\n");
	}
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d:\n", i+1);
		solvecase();
		//printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}