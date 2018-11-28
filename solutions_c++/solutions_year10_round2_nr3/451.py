#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int x[100];
int v[100];
map < string , bool > h;

struct ele{
	int x;
	int v;
};

bool cmp(ele a , ele b)
{
	return a.x < b.x;
}

int dp[1010][1010];
int c[1010][1010];
void cal()
{

	int i , j;
	c[0][0] = 1;
	c[1][0] = 1;
	c[1][1] = 1;
	for (i = 2 ; i <= 500 ; i ++){
		c[i][0] = 1;
		for (j = 1 ; j <= i ; j ++){
			c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
			c[i][j] %= 100003;
			//printf("%d " , c[i][j]);
		}
		//printf("\n");
	}

}

int dfs(int k , int x)
{

	if (dp[k][x] != -1)
		return dp[k][x];
	int ret = 0;
	for (int i = 1 ; i < k ; i ++){
		if (k - i <= x - k){
			ret += dfs(i , k) * c[x - k - 1][k - i - 1];
		}
		ret %= 100003;
	}
	return dp[k][x]  = ret;
}

int a[510];

int main()
{
	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);

	int t;
	cal();
	int cas = 0;
	memset(dp , -1 , sizeof(dp));
	for (int i = 1 ; i <= 500 ; i ++)
		dp[1][i] = 1;
	for (int i = 1; i <= 500 ; i ++){
		for (int j = 1 ; j < i ; j ++){
			dp[j][i] = dfs(j , i);
			if (dp[j][i] >= 0)
			//	printf("%d %d : %d\n" , j , i , dp[j][i]);
			a[i] += dp[j][i];
			a[i] %= 100003;
		}
		//printf("%d : %d\n" , i , a[i]);
	}
	

	scanf("%d" , &t);
	while (t --)
	{
		cas ++;
		int n;
		scanf("%d" , &n);
		printf("Case #%d: %d\n" , cas , a[n]);

	}
}