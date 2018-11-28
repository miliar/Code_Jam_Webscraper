#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<algorithm>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

int n, k, p[100][25];
int con[16];

bool cross(int a[], int b[])
{
	for(int i = 1; i < k; i ++)
	{
		if(a[i-1] <= b[i-1] && a[i] >= b[i])return true;
		if(b[i-1] <= a[i-1] && b[i] >= a[i])return true;
	}
	return false;
}

int dp[1<<17][17], ans;

void dfs(int s, int u, int num, int size)
{
	//printf("%d %d %d\n", s, u, num);
	for(int i = 1; i <= size; i ++)
	{
		if(num >= dp[u][i])return;
	}
	//printf("%d %d %d ok1\n", s, u, num);
	if(num >= ans)return;
	//printf("%d %d %d ok2\n", s, u, num);
	dp[u][size] = num;
	if(u == (1<<n)-1){
		ans = num;
		return;
	}
	//printf("%d %d %d ok3\n", s, u, num);
	bool flag = false;

	for(int i = 0; i < n; i ++)
	{
		if(((1<<i)&u)==0 && (con[i]&s)==0)
		{
			dfs(s|(1<<i), u|(1<<i), num, size+1);
			flag = true;
		}
	}
	//printf("%d %d %d\n", s, u, num);
	//if(flag)puts("ok");
	//system("pause");
	if(!flag){
		for(int i = 0; i < n; i ++)
		{
			if(((1<<i)&u)==0)
			{
				dfs(1<<i, u|(1<<i), num+1, 1);
				break;
			}
		}
	}
}

int main()
{
	int T, cas;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	rep(cas,T)
	{
		scanf("%d %d", &n, &k);
		for(int i = 0; i < n; i ++)con[i] = 0;
		for(int i = 0; i < n; i ++)
		{
			for(int j = 0; j < k; j ++)
			{
				scanf("%d", &p[i][j]);
			}
			for(int j = 0; j < i; j ++)
			{
				if(cross(p[j], p[i]))
				{
					con[i] |= (1<<j);
					con[j] |= (1<<i);
				}
			}
		}
		//for(int i = 0; i < n; i ++)printf("%d\n", con[i]);
		for(int i = 0; i < (1<<n); i ++)
		for(int j = 0; j < 17; j ++)
		{
			dp[i][j] = 100000000;
		}
		ans = 100000000;
		dfs(0, 0, 1, 0);
		printf("Case #%d: %d\n", cas+1, ans);
	}
	return 0;
}
