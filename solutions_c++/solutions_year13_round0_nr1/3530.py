#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <ctime>
using namespace std;
char g[10][10];
void input()
{
	int i;
	for ( i=0 ; i<4 ; i++ ) scanf("%s",g[i]);
}
int judge1(int row,char c)
{
	int i,cnt0,cnt1;
	cnt0 = cnt1 = 0;
	for ( i=0 ; i<4 ; i++ )
	if (g[row][i] == c) cnt0++;
	else if (g[row][i] == 'T') cnt1++;
	if (cnt0+cnt1 == 4) return 1;
	else	return 0;
}
int judge2(int col,char c)
{
	int i,cnt0,cnt1;
	cnt0 = cnt1 = 0;
	for ( i=0 ; i<4 ; i++ )
	if (g[i][col] == c) cnt0++;
	else if(g[i][col] == 'T') cnt1++;
	if (cnt0+cnt1 == 4) return 1;
	else	return 0;
}
int judge3(char c)
{
	int i,cnt0,cnt1;
	cnt0 = cnt1 = 0;
	for ( i=0 ; i<4 ; i++ )
	if (g[i][i] == c) cnt0++;
	else if (g[i][i] == 'T') cnt1++;
	if (cnt1+cnt0 == 4) return 1;
	cnt0 = cnt1 = 0;
	for ( i=0 ; i<4 ; i++ )
	if (g[3-i][i] == c) cnt0++;
	else if (g[3-i][i] == 'T') cnt1++;
	if (cnt1+cnt0 == 4) return 1;
	return 0;
}
void solv()
{
	int i,j;
	for ( i=0 ; i<4 ; i++ )
	{
		if (judge1(i,'X') || judge2(i,'X') || judge3('X'))
		{
			printf("X won\n");
			return;
		}
		if (judge1(i,'O') || judge2(i,'O') || judge3('O'))
		{
			printf("O won\n");
			return;
		}
	}
	for ( i=0 ; i<4 ; i++ )
	for ( j=0 ; j<4 ; j++ )
	if (g[i][j] == '.')
	{
		printf("Game has not completed\n");
		return;
	}
	printf("Draw\n");
	return;
}
int main()
{
	int cas,tt=0;
	freopen("test.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
		printf("Case #%d: ",++tt);
		input();
		solv();
	}
	return 0;
}
