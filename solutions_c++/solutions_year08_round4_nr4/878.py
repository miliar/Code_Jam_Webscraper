#include<iostream>
#include<cstdio>

using namespace std;

int Case,T;
char in[2000],out[2000];
int list[10],visit[10],k,Min,LEN;
void solve()
{
	int i,j;
	int ans ;
	int t = 0 ;
	for(i = 0 ; i < LEN ;)
	{
		for(j = 0 ; j < k ; j ++)
			out[i++] = in[list[j]-1+t];
		t += k ;
	}
	ans = 1 ;
	for(j = 1 ; j < LEN ; j ++)
	{
		if(out[j] != out[j-1])
			ans ++;
	}
	if(ans < Min)
		Min = ans ;
}
void dfs(int len)
{
	int i;
	if(len == k)
	{
		solve();
		return ;
	}
	for(i = 1 ; i <= k ; i ++)
	{
		if(visit[i])
			continue ;
		visit[i] = 1 ;
		list[len] = i ;
		dfs(len+1);
		visit[i] = 0 ;
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&T);
	for(Case = 1 ; Case <= T ; Case ++)
	{
		scanf("%d",&k);
		scanf("%s",in);
		LEN = strlen(in);
		memset(visit,0,sizeof(visit));
		Min = INT_MAX ;
		dfs(0);
		printf("Case #%d: %d\n",Case,Min);
	}
	return 0;
}