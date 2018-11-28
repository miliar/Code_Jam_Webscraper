#include <stdio.h>
#include <string.h>

const int ten[] = {1,10,100,1000,10000};
const int maxn = 3001 ;
bool vis[maxn][maxn] ;

inline int get_min(int a,int b)	{	return a < b ? a : b ;	}
inline int get_max(int a,int b)	{	return a > b ? a : b ;	}

inline int cal(int t,int a,int b)
{
	int ans , i , j , k , len , num[10] , pre , st , x , y ;
	for( i = t , len = 0 ; i ; )
	{
		num[len++] = i % 10 ;
		i /= 10 ;
	}
	pre = t ;
	for( ans = 0 , i = len-1 ; i >= 1 ; i--)
	{
		st = ( pre - num[i] * ten[len-1] ) * 10 + num[i] ;
		if( st > t && st <= b ) ans++;
		pre = st ;
	}
	return ans ;
}

int main()
{
	int i , t , j , n , m , ans ;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	//cal(12345,100,1000000);
	scanf("%d",&t);
	for( i = 1 ; i <= t ; i++)
	{
		memset(vis,0,sizeof(vis));
		scanf("%d%d",&n,&m);
		for ( j = n , ans = 0 ; j <= m ; j++)	ans += cal(j,n,m);
		printf("Case #%d: %d\n",i,ans);
	}
}