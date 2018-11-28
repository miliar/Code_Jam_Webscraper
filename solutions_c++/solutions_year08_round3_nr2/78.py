#include <iostream>
#include <math.h>
#include <string>
#include <algorithm>
using namespace std;
char str[20];
int len ,ans;
void dfs(int pos , __int64 num)
{
	if(pos == len)
	{
		if( num % 2 == 0 || num % 3 == 0 || num % 5 == 0 || num % 7 == 0)
		{
			ans ++ ;
		}
		return ;
	}
	__int64 sum = 0 ; 
	for(int i = pos; i<len; i ++)
	{
		sum = sum * 10 + str[i] - '0';
		if(pos != 0)
			dfs(i + 1, num - sum);
		dfs(i + 1, num + sum);
	}
}
int main()
{
	int test;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &test) ;
	int ca = 1;
	while(test -- )
	{
		scanf("%s", str);
		len = strlen(str);
		ans = 0; 
		dfs(0, 0);
		printf("Case #%d: %d\n", ca++, ans);
	}
	return 0;
}