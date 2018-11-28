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
const int MM = 2000005;
int cc[MM],h[MM];
map<string,int> mp;
long long cal( int a,int b )
{
     mp.clear();
     int cnt = 0;
     char str[10];
     a = max( a,10 );
     long long sum = 0;
     for( int i = a; i <= b; ++i )
     {
          int k = 0,tmp = i;
          itoa( i,str,10 );
          k = strlen( str );
          char str1[10];
          strcpy( str1,str );
          int f = 0;
          for( int j = 0; j < k - 1; ++j )
          {
               int c = str1[0];
               for( int l = 0; l < k - 1; ++l )
                    str1[l] = str1[l+1];
               str1[k-1] = c;
               if( mp.count( str1 ) )
               {
                   f = 1;
                   mp[str1] ++;
                   break;
               }
           }
           if( !f )
           {
               mp[str]++;
           }
      }
      map<string,int>:: iterator it;
      for( it = mp.begin(); it != mp.end(); it++ )
      {
           if( it -> second > 1 )
           {
               int c = it -> second;
               sum += ( c*(c-1)/2 );
           }
       }
      return sum;
 }
int main(  )
{
	int Case,N,M;
	freopen( "C-small-attempt3.in","r",stdin );
	freopen( "C-small-attempt3.out","w",stdout );
	scanf( "%d",&Case );
	for( int ca = 1; ca <= Case; ++ca )
	{
           scanf( "%d%d",&N,&M );
           printf( "Case #%d: ",ca );
           cout << cal( N,M )  << endl;
           }
	return 0;
}
