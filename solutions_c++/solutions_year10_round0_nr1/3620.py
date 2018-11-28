//Writer tclsm
#include <iostream>
using namespace std;

const
                int maxn = 31;
                int n , k , tmp;
                
int main()
{
                freopen( "a.in" , "r" , stdin );
                freopen( "a.out" , "w" , stdout );
                int run;
                scanf( "%d" , &run );
                for ( int test = 1 ; test <= run ; test++ )
                {
                               scanf( "%d %d" , &n , &k );
                               tmp = 1 << n;
                               k = k % tmp;
                               printf( "Case #%d: " , test );
                               if ( k == tmp-1 ) printf( "ON\n" );
                               else              printf( "OFF\n" );
                }
                fclose( stdin );
                fclose( stdout );
}
