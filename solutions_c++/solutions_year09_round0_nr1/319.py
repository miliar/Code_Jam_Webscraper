#include<stdio.h>
#include<memory.h>
bool hash[510][18][28];
char s[5100][18];
int l, d, n;
char need[5100];
int ans[510];
void work(int id, int t, int now)
{
	if (t >= l)
		return ;
	if (need[now] == '(')
	{
		now++;
		while(need[now] != ')')
		{
			hash[id][t][need[now] - 'a'] = 1;
			now++;
		}
		now++;
	}
	else
	{
		hash[id][t][need[now] - 'a'] = 1;
		now++;
	}
	work(id, t + 1, now);
}
bool judge(int p, int q)
{
	int i;
	for(i = 0; i < l; i++)
	{
		if (hash[q][i][s[p][i] - 'a'] == 0)
			return false;
	}
	return true;
}
void run()
{
	int i, j;
	memset(hash, 0, sizeof(hash));
	memset(ans, 0, sizeof(ans));
	for(i = 0; i < d; i++)
		scanf("%s",s[i]);
	for(i = 0; i < n; i++)
	{
		scanf("%s",need);
		work(i, 0, 0);
	}
	for(i = 0; i < d; i++)
	{
		for(j = 0; j < n; j++)
		{
			if (judge(i, j))
				ans[j]++;
		}
	}
	for(i = 0; i < n; i++)
	{
		printf("Case #%d: %d\n",i + 1, ans[i]);
	}
}
int main()
{
	int i, j;
	freopen("21.in","r",stdin);
	freopen("111.txt","w",stdout);
	while(scanf("%d%d%d",&l, &d, &n) == 3)
	{
		run();
	}
}