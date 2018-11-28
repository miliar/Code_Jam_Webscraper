#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <complex>
using namespace std;

const int maxn = 120;

int visit[2][6*maxn];

int board[4*maxn][4*maxn];

struct diamond{
	int k;
	int num[maxn][maxn];
	void in()
	{
		scanf("%d",&k);
		for(int i = 0; i < k; i++)
		{
			for(int j = 0; j < i+1; j++)
				scanf("%d",&num[i - j][j]);
		}
		for(int i = k; i < 2*k-1; i++)
		{
			for(int j = 0; j < 2*k-1-i; j++)
				scanf("%d",&num[k- 1 - j][j + i + 1 - k]);
		} 
	}

	void out()
	{
		for(int i = 0; i < k; i++)
		{
			for(int j = 0; j < k; j++)
				printf("%d ",num[i][j]);
			printf("\n");
		}
	}

}d;

bool check(int a, int b){
	return a == 10 || b==10 || a==b;
}

bool check(int s, int x, int y)
{
	if(visit[0][maxn + x - y]==0 || visit[1][maxn + x  + y - s] == 0)return false;

	int unknow = 10;
	for(int i = 0; i < s; i++)
		for(int j = 0; j < s; j++)
			board[i][j] = unknow;
	
	for(int i = 0; i < d.k; i++)
		for(int j = 0; j < d.k; j++)
			board[i + y][j + x] = d.num[i][j];


	for(int i = 0; i < s; i++)
		for(int j = 0; j < s; j++)
			if( !check( board[i][j], board[j][i]) )
			{
					visit[0][maxn + x - y]== 0;
					return false;
			}
	visit[0][maxn + x - y]== 1;

	for(int i = 0; i < s; i++)
		for(int j = 0; j < s; j++)
			if( !check( board[i][j], board[s - 1 - j][s - 1 - i]) )
			{
					visit[1][maxn + x  + y - s] = 0;
					return false;
			}
	
	visit[1][maxn + x  + y - s] = 1;
	return true;
}

int get(int k)
{	
	return k*k;
}

int solve()
{
	for(int i = d.k; ; i++)
	{
		for(int j = 0; j <= i - d.k; j++)
			for(int p = 0; p <= i -d.k; p++)
			{
				if(check(i, j, p))return get(i) - get(d.k);
			}
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int runs,cas = 1;
	for(scanf("%d",&runs); runs > 0; runs--)
	{
		d.in();
		//d.out();
		memset(visit, -1, sizeof(visit));
		printf("Case #%d: %d\n",cas++, solve());
	}
}

/*
4
4
9
  1 1
 6 3 6
9 5 5 9
 6 3 6
  1 1
   9

2
 1
1 2
 1
3
  1
 6 3
9 5 5
 6 3
  1
*/