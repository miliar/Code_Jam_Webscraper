#include<cstdio>
#include<string.h>

using namespace std;

bool used[50];
double dp[50];

int cnt[100], N, C;

void depart(int num, int val)
{
	int i;
	for(i = 2; i <= num/i; i ++)
	{
		while(num % i == 0)
		{
			num /= i;
			cnt[i] += val;
		}
	}
	if(num > 1)
	{
		cnt[num] += val;
	}
}

double Com(int n, int m, int val)
{
	int i;
	/*
	for(i = m; i > m-n; i --)
	{
		depart(i, 1*val);
	}
	for(i = 1; i <= n; i ++)
	{
		depart(i, (-1)*val);
	}
	*/
	double ans = 1;
	for(i = m; i > m-n; i --)
	{
		ans *= i;
	}
	for(i = 1; i <= n; i ++)
	{
		ans /= i;
	}
	return ans;
}

double p(int i, int j)
{
	int k;
	double ans = 1;
	memset(cnt, 0, sizeof(cnt));
	ans *= Com(j-i, C-i, 1);
	ans *= Com(N-j+i, i, 1);
	ans /= Com(N, C, -1);
	return ans;
	/*
	Com(j-i, C-i, 1);
	Com(N-j+i, i, 1);
	Com(N, C, -1);
	for(k = 1; k <= 40; k ++)
	{
		while(cnt[k] > 0)
		{
			cnt[k] --;
			ans *= (double)k;
		}
		while(cnt[k] < 0)
		{
			cnt[k] ++;
			ans /= (double)k;
		}
	}
	return ans;
	*/
}

double dfs(int i)
{
	int k;
	if(used[i])return dp[i];
	double ans = 1;
	for(k = i+1; k <= i+N && k <= C; k ++)
	{
		ans += dfs(k)*p(i, k);
	}
	ans /= (1.0 - p(i, i));
	used[i] = true;
	dp[i] = ans;
	return ans;
}

int main()
{
	int cas, T;
	N = 1;
	C = 2;
	int i, j;
	
	/*while(scanf("%d %d", &i, &j)!=EOF)
	{
		printf("%lf\n", p(i, j));
	}
	*/
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		scanf("%d %d", &C, &N);
		memset(used, false, sizeof(used));
		used[C] = true;
		dp[C] = 0;
		printf("Case #%d: %lf\n", cas, dfs(0));
	}
	return 0;
}
