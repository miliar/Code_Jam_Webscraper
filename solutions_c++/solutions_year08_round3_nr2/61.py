
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

char cmd[20];
int len ,ans;
void DFS(int  pos , __int64 cm )
{
	if(pos == len)
	{
		if( cm % 2 == 0 || cm % 3 == 0 || cm % 5 == 0 || cm % 7 == 0)
		{
			ans ++ ;
		}
		return ;
	}
	__int64 sum = 0 ; 
	for(int i = pos ; i < len; i ++ )
	{
		sum = sum * 10 + cmd[i] - '0' ;
		if(pos != 0)
			DFS(i + 1, cm - sum );
		DFS(i + 1, cm + sum );
	}
}
int main(void)
{
	int cases ;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&cases) ;
	int f = 0;
	while( cases -- )
	{
		scanf("%s",cmd) ;
		len = strlen( cmd );
		ans = 0; 
		DFS( 0 , 0);
		printf("Case #%d: ",++f);
		printf("%d\n",ans);
	}
	return 0;
}
