#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
#include<vector>
#include<map>
#include<algorithm>
#include<string.h>
#include<string>
int dp[101][101];
int map1[101][101];
int h, w;
int is(int a, int b)
{
	if(1<=a && a <= h && 1<=b && b <= w)
		return 1;
	return 0;
}
int f(int r, int c)
{

	int &res = dp[r][c];
	if(map1[r][c] == 1)
	{
		res = 0;
		return res;
	}
	if(res!=-1)
		return res;
	res = 0;
	//if(is(r-1, c) && map1[r-1][c]!=1)
	//	res = (res + f(r-1, c)%10007)%10007;
	//if(is(r, c-1)&&map1[r][c-1]!=1)
	//	res = (res + f(r, c-1)%10007)%10007;
	if(is(r-2, c-1)&&map1[r - 2][c - 1]!=1)
		res = (res + f(r - 2, c-1)%10007)%10007;
	if(is(r-1, c-2)&&map1[r-1][c-2]!=1)
		res = (res + f(r- 1, c-2)%10007)%10007;
	return res;
}
int main()
{
	int n;
	int i;
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	scanf("%d", &n);
	for(i = 0; i < n; i++)
	{
		int r;
		scanf("%d%d%d", &h, &w, &r);
		int j;
		memset(map1, 0, sizeof(map1));
		memset(dp, -1, sizeof(dp));
		for(j = 0; j < r; j++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			map1[a][b] = 1;
		}
		dp[1][1] = 1;
		f(h, w);
		//for(j = 1; j<= h; j++)
		//{
		//	int k; 
		//	for(k = 1; k<=w;k++)
		//		cout<<dp[j][k]<<" ";
		//	cout<<endl;
		//}
		printf("Case #%d: %d\n", i + 1, dp[h][w]);
	}	
}