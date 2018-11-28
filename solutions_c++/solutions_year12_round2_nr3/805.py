#include <cstdio>
#include <cstring>

const int MAXN = 21;

int s[MAXN], n,cnt;
bool finish, v[MAXN];
bool r[2][MAXN];

void print()
{
	for(int i = 0; i < 2; i ++)
	{
		for(int j = 0; j < n; j ++)
			if(r[i][j]) printf("%d ", s[j]);
		printf("\n");
	}
}
void check(int now, int sum, int res)
{
	if(finish) return;
	if(now < n)
	{
		v[now] = 0;
		check(now + 1, sum, res);
		v[now] = 1;
		check(now + 1, sum + s[now], res);
	}
	else if(sum == res) 
		{
			memcpy(r[cnt], v, sizeof(v));
			cnt ++;
			if(cnt >= 2) 
			{
				finish = true;
				print();
			}
		}
}

void dfs(int now, int sum)
{
	if(finish) return;
	if(now < n)
	{
		dfs(now + 1, sum);
		dfs(now + 1, sum + s[now]);
	}
	else
	{
		cnt = 0;
		check(0, 0, sum);
	}
}

void work()
{
	finish = false;
	scanf("%d", &n);
	for(int i = 0; i < n; i ++)
		scanf("%d", s + i);
	dfs(0, 0);
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i ++)
	{
		printf("Case #%d:\n", i);
		work();
	}
	return 0;
}
