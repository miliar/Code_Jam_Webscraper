#include<stdio.h>
#include<string.h>

char tab[90000];
int flag[10] = {0};
int re[10];
int len;
char temp[90000];
int k;
int ans;

void dfs( int dep, int last)
{
	int i, j;
	if( dep == last )
	{
		int kk = 0;
		for( i=0, j=0; i<len; i++ )
		{
			temp[i] = tab[kk+re[j++]];
			if( j == k )
			{
				kk += k;
				j = 0;
			}
		}
		int aa = 1;
		for( i=1; i<len; i++ )
		{
			if( temp[i] != temp[i-1] )
			{
				aa ++;
			}
		}
		if( aa < ans || ans == -1 )
			ans = aa;
		return ;
	}
	for( i=1; i<=last; i++)
	{
		if( flag[i] == 0 )
		{
			re[dep] = i-1;
			flag[i] = 1;
			dfs(dep+1, last);
			flag[i] = 0;
		}
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d", &T);
	int ca;
	for( ca=1; ca<=T; ca++ )
	{
		ans = -1;
		scanf("%d", &k);
		scanf("%s", tab);
		len = strlen(tab);
		dfs( 0, k );
		printf("Case #%d: %d\n", ca, ans);
	}
}