#include <iostream>

using namespace std;

int main(){
    
    int tc, Tc;
    
    freopen( "A-large.in", "r", stdin );
    freopen( "a.large.txt", "w", stdout );
    
    scanf( "%d", &Tc );
    
    for( tc = 1; tc <= Tc; tc++ ){
           
           long long n, k;
           
           scanf( "%I64d%I64d", &n, &k );
           
           long long m = ( 1 << n );
           
           long long ans = k % m;
           
           if( ans == m - 1 ){
               printf( "Case #%d: ON\n", tc );
           }
           else{
                printf( "Case #%d: OFF\n", tc );
           }
    }
    
    return 0;
}
                  
