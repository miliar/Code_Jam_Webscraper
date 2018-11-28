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

int len;
int64 sum;
char s[20];

void dfs( int64 p , int64 x , int q , int y )
{
     int64 tmp; 
     if( q == len ){
		 if( p%2 == 0 || p%3 == 0 || p%5 == 0||p%7 == 0 ){
			 sum++;//printf("%d<= %d \n" , p ,x );
		 }
     return;
     }

	 tmp = x*10+y*(s[q]-'0');
     dfs( p-x+tmp , tmp , q+1 , y);
     tmp = (s[q]-'0');
     dfs( p + tmp , tmp  , q+1 , 1);
     dfs( p - tmp , -tmp  , q+1 , -1);
}

void solve()
{
    int i;
	sum = 0;
	scanf("%s" , s );//puts(s);
	len = strlen(s);
	dfs( (s[0]&15) , (s[0]&15) , 1 , 1 );
//	if( s[0] != '0' ) dfs( -(s[0]&15) , -(s[0]&15) , 1 , -1 );
//	dfs( 0 , -(s[0]&15) , 1 );
	printf("%lld\n" , sum );
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
/*
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

int len;
int64 sum;
char s[20];

void dfs( int p , int x , int q )
{
     int i , tmp; 
     if( q == len ){
     tmp = p+x;
     if( tmp%2 == 0 || tmp%3 == 0 || tmp%5 == 0||tmp%7 == 0 )sum++;
     tmp = p-x;
     if( tmp%2 == 0 || tmp%3 == 0 || tmp%5 == 0||tmp%7 == 0 )sum++;
     return;
     }

     tmp = x*10+(s[q]&15);
     dfs( p , tmp , q+1);
     dfs( p+x , (s[q]&15) , q+1);
     dfs( p-x , (s[q]&15) , q+1);
}

void solve()
{
    int i;
	sum = 0;
	scanf("%s" , s );
	len = strlen(s);
	dfs( (s[0]&15) , (s[0]&15) , 1 );
//	dfs( 0 , -(s[0]&15) , 1 );
	printf("%lld\n" , sum/2 );
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

*/
