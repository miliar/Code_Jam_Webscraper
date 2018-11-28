#include"iostream"
#include"string.h"
#include"algorithm"
#include"queue"

using namespace std;

#define Min(a,b) ((a)<(b)) ? a : b
#define Max(a,b) ((a)>(b)) ? a : b
#define maxn 1010
#define maxm 10010
#define inf 1<<29
#define int64 long long

int f[maxn] , p , k , l;


void solve()
{
    int i , j , cnt;
	int64 sum = 0;
	scanf("%d %d %d" , &p , &k , &l );
	for( i = 0;i < l;i++ )
		scanf("%d" , &f[i]);	//printf("%d %d %d<\n" , p , k*p , l);
	if( p*k < l ) {
		printf("Impossible\n");return;
	}
	sort( f , f + l );

	cnt = 1;
	for( i = l-1 , j = -1;i >= 0;i-- )
	{
		j++;
		if( j == k ){
			j = 0;cnt++;
		}
		sum += (int64)cnt*f[i];
	//	printf("-> %lld %d\n" , sum  , cnt);
	}
	printf("%lld\n" , sum);
}

int main()
{
    int cas , i;
    scanf("%d" , &cas);
    for(  i = 1;i <= cas;i++ )
	{
		printf("Case #%d: " , i );
		solve();
	}
    return 0;
}
