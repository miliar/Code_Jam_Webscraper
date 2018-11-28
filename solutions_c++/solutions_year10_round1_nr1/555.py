/* 
 * Problem: Google Code Jam 2010 Round 1A rotate
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2010.5.22 9:00
 * State: Solved
 * Memo: 數值計算
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 51;
char F[MAXN][MAXN],G[MAXN];
int N,K;
bool red,blue;

bool check_h(char c,int i,int j)
{
	if (j+K-1>N)
		return false;
	for (int k=0;k<K;k++)
		if (F[i][j+k] != c)
			return false;
	return true;
}

bool check_v(char c,int i,int j)
{
	if (i+K-1>N)
		return false;
	for (int k=0;k<K;k++)
		if (F[i+k][j] != c)
			return false;
	return true;
}

bool check_x(char c,int i,int j)
{
	if (i+K-1>N || j+K-1>N)
		return false;
	for (int k=0;k<K;k++)
		if (F[i+k][j+k] != c)
			return false;
	return true;
}

bool check_x2(char c,int i,int j)
{
	if (i+K-1>N || j-K+1<1)
		return false;
	for (int k=0;k<K;k++)
		if (F[i+k][j-k] != c)
			return false;
	return true;
}

bool check(char c)
{
	for (int i=1;i<=N;i++)
		for (int j=1;j<=N;j++)
			if (check_h(c,i,j) || check_v(c,i,j) || check_x(c,i,j) || check_x2(c,i,j))
				return true;
	return false;
}

void debug()
{
	printf("\n");
	for (int i=1;i<=N;i++)
	{
		for (int j=1;j<=N;j++)
			printf("%c",F[i][j]);
		printf("\n");
	}
	printf("\n");
}

void solve()
{
	red = blue = false;
	int i,j,k;
	for (i=1;i<=N;i++)
		for (j=1;j<=N;j++)
			F[i][j] = '.';
	for (i=1;i<=N;i++)
	{
		for (j=1;j<=N;j++)
		{
			char c = getchar();
			while (c == 10 || c== 13) c = getchar();
			F[j][N-i+1] = c;
		}
	}
	//debug();
	for (j=1;j<=N;j++)
	{
		k = 0;
		for (i=N;i>=1;i--)
		{
			if (F[i][j] != '.')
				G[++k] = F[i][j];
		}
		for (i=1;i<=N;i++)
		{
			if (i>k)
				G[i] = '.';
			F[N-i+1][j] = G[i];
		}
	}
	//debug();
	if (check('R'))
		red = true;
	if (check('B'))
		blue = true;
}

int main()
{
	int T;
	freopen("rotate.in","r",stdin);
	freopen("rotate.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",i);
		solve();
		if (red && blue)
			printf("Both\n");
		else if (red && !blue)
			printf("Red\n");
		else if (!red && blue)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
