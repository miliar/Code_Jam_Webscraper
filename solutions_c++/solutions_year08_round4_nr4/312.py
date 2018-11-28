#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

char ch[2008], temp[2008];
int list[16], flag[16];
int k, len, Min;

void work()
{
	int i, j, ans, t = 0, l;
	l = strlen(ch);
	for(i = 0 ; i < l ;)
	{
		for(j = 0 ; j < len ; j ++)
		{
			temp[i++] = ch[list[j]-1+t];
		}
		t += k ;
	}
	ans = 0 ;
	for(i = 0 ; i < l ;)
	{
		j = i ;
		while(j+1 < l && temp[j] == temp[j+1])
		{
			j ++ ;
		}
		j ++ ;
		i = j ;
		ans ++ ;
	}
	if(Min == -1 || ans < Min)
		Min = ans ;
}
void dfs()
{
	int i;
	if(len == k)
	{
		work();
		return ;
	}
	for(i = 1 ; i <= k ; i ++)
	{
		if(flag[i])
			continue ;
		flag[i] = 1 ;
		list[len ++] = i ;
		dfs();
		len -- ;
		flag[i] = 0 ;
	}
}
int main()
{
	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("D.out","w",stdout);
	int t = 1, T;
	scanf("%d",&T);
	while (T --)
	{
		scanf("%d",&k);
		scanf("%s",ch);
		len = 0; Min = -1;
		memset(flag,0,sizeof(flag));
		dfs();
		printf("Case #%d: %d\n",t ++,Min);
	}
	return 0;
}