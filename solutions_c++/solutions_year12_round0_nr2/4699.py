#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>

using namespace std;

int n , s , p;
int score[101];

int main()
{
    int t;
    scanf("%d" , &t );
    char c;

    int n , s , p , k , answer;
    int cnt = 0;
    while( t ) {
           t--;
           cnt++;
           answer = 0;
           scanf("%d" , &n );
           scanf("%d" , &s );
           scanf("%d" , &p );
           for ( int i = 0; i < n; i++ )
           {
               scanf("%d" , &k );
               if( k >= 3 * p )
                   answer++;
               else if( p >= 1 && ( k >= (3*p-2 ) )  )
                    answer++;
               else if( s > 0 && p >= 2 && ( k  >= ( 3 * p - 4 ) ) ) {
                    answer++;
                    s--;
               }
           }

           printf("Case #%d: %d\n" , cnt , answer );

    }
}
