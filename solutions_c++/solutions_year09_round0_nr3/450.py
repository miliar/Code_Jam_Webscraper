#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
char str[600] ;
int dp[600][200] ;
#define MOD 10000
vector<int> s[200] ;
vector<int> id[200];
char Q[200] ;
//welcome to code jam
//w 0 
//e 0 1 2
//l 0
//c 0 1
//o 0 1 2
//m 0 1
//t 0
//d 0
//
void init()
{
	int i ;
	char str[] = "welcome to code jam" ;
	for(i = 0 ; i < 200 ; i ++)
	{
		s[i].clear() ;
		id[i].clear() ;
	}
	for(i = 0 ; str[i] != '\0' ; i ++)
	{
		id[str[i]].push_back(i) ;
	}
}
int ans ;
void solve()
{
	int i,j,k ;
	int len = strlen(str);
	memset(dp,0,sizeof(dp)) ;
	ans = 0 ;
	int now,next ;
	for(i = 0 ; i < len ; i ++)
	{
		for(j = 0 ; j < id[str[i]].size() ; j ++)
		{
			now = id[str[i]][j] ;
			for(k = 0 ; k < i ; k ++)
			{
				if(now-1 >= 0)
				{
					dp[i][now] += dp[k][now-1] ;
					dp[i][now] %= MOD ;
				}
			}
			if(now == 0)
				dp[i][now] ++ ;
			dp[i][now] %= MOD ;
 		}
		ans += dp[i][18] ;
		ans %= MOD ;
	}

}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("ee.out","w",stdout) ;
	init() ;
	int T ;
	while(1 == scanf("%d",&T))
	{
		gets(str) ;
		int Case = 1 ;
		while(T --)
		{
			gets(str) ;
			solve() ;
			printf("Case #%d: %04d\n",Case++,ans) ;
		}
	}
	return 0 ;
}