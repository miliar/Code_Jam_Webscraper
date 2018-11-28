#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<cmath>
#include<cstring>
#include<set>
#include<queue>
#include<list>
#include<vector>
#include<ctime>
using namespace std;

#define EPS 1e-8
#define L long long
#define INF ( 1 << 30 )
#define LL(x) ((x)<<1)
#define RR(x) ((x)<<1|1)
#define LOW(x) ((x)&(-x))
#define MEM(x,y) memset(x,y,sizeof(x));

#ifdef LOCAL
	#define RFILE(x) freopen(x,"r",stdin);
	#define WFILE(x) freopen(x,"w",stdout);
	#define BUG puts( "Fuck!" );
	#define SP system( "pause" );
	#define _PT int __start,__end; __start = clock();
	#define PT  __end = clock(); printf( "n运行时间为:  %d msnn",__end-__start ); SP
#else
	#define RFILE(x)
	#define WFILE(x)
	#define BUG
	#define SP
	#define PT
#endif
char str[1005];
char h[26] = {121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};
int main(  )
{
	int Case;
	freopen( "A-small-attempt3.in","r",stdin );
	freopen( "A-small-attempt3.out","w",stdout );
	scanf( "%d",&Case );
	gets( str );
	for( int ca = 1; ca <= Case; ++ca )
	{
         gets( str );
         printf( "Case #%d: ",ca );
         for( int i = 0; str[i]; ++i )
         {
              if( str[i] == ' ' )
                  putchar( ' ' );
              else
                  putchar( h[str[i]-'a'] );
         }
         puts( "" );
     }
	return 0;
}
