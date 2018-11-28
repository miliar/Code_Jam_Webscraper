#include <iostream.h>


int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    long n, N, K, i, j;
    //scanf("%ld", &n);
    cin >> n;
    for( i = 1; i <= n; i++ )
    {
         cin >> N >> K;
         j = 1 << N;
         if( K%j == j-1)  
         {
             printf( "Case #%d: ON\n", i );
         }
         else
         {
             printf( "Case #%d: OFF\n", i );
         }
     }   
}
