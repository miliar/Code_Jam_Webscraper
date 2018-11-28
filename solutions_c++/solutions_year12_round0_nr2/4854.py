
#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>

using namespace std;

int n,s,p,T,count,k,ans;
int score[110];

int main()
{
    scanf("%d" , &T );
    char c;
    count = 0;
    while( T-- ) {
           count++;
           ans = 0;
           scanf("%d" , &n );
           scanf("%d" , &s );
           scanf("%d" , &p );
           for ( int i = 0; i < n; i++ )
           {
               scanf("%d" , &k );
               if( k >= 3 * p )
                   ans++;
               else if( p >= 1 && ( k >= (3*p-2 ) )  )
                    ans++;
               else if( s > 0 && p >= 2 && ( k  >= ( 3 * p - 4 ) ) ) {
                    ans++;
                    s--;
               }
           }

           printf("Case #%d: %d\n" , count , ans );

    }
}

