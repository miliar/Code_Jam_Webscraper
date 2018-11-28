#include <stdio.h>
#include <algorithm>
using namespace std;
char str[2000];
char tttt[2000];
int L[10],route[10];
int num,len ,MIN;
void solve()
{
	int i,j;
	int ans ;
	int strl = strlen(str);
	int t = 0 ;
	for(i = 0 ; i < strl ;)
	{

		for(j = 0 ; j < len ; j ++)
			tttt[i++] = str[L[j]-1+t];
		t += num ;
	}
	ans = 0 ;
	for(i = 0 ; i < strl ;)
	{
		j = i ;

		while(j+1 < strl && tttt[j] == tttt[j+1])
			j ++ ;

		j ++ ;
		i = j ;
		ans ++ ;
	}
	if(MIN == -1 || ans < MIN)
		MIN = ans ;
}
void DFS()
{
	int i;
	if(len == num)
	{
		solve();
		return ;
	}
	for(i = 1 ; i <= num ; i ++)
	{
		if(route[i])
			continue ;
		route[i] = 1 ;
		L[len ++] = i ;
		DFS();
		len -- ;
		route[i] = 0 ;
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	int cases , f = 0;
	scanf("%d",&cases);
	while(cases --)
	{
		scanf("%d",&num);
		scanf("%s",str);
		memset(route,0,sizeof(route));
		len = 0 ;
		MIN = -1 ;
		DFS();
		printf("Case #%d: %d\n",++f,MIN);
	}
	return 0;
}