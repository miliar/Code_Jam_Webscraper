/*
PROB: candy
LANG: C++
KEYW: 
*/
/// Thanks to Him I can know and learn! Love Christ!
/// "Without Me you can do nothing" ( John 15:5 )
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cstring>
#include <queue>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <numeric>
#include <algorithm>
#define foreach(_var,_container) for( typeof( (_container).begin() ) _var = (_container).begin() ; _var != (_container).end() ; ++_var )
#define now() double( double( clock() ) / double( CLOCKS_PER_SEC ) )
#if 1
#define eprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )
#else
#define eprintf(msg, ... ) 0
#endif
#define pprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )

using namespace std;

const int MAXN = 1 << 7;

int T,N;
int c[MAXN];

/**
011
101
110
---

c[0] = 2
c[1] = 2
c[3] = 2;
**/

void read(){
    scanf("%d", &N);
    for( int i = 0 ; i < N ; i++ )
        scanf("%d", &c[i]);
}

void solve( int testid ){
    int xall = 0;
    int sumall = 0;
    for( int i = 0 ; i < N ; i++ )
        xall ^= c[i], sumall += c[i];
    if( xall != 0 )
        printf("Case #%d: NO\n", testid+1);
    else{
        sort( c , c + N );
        
        printf("Case #%d: %d\n", testid+1, sumall - c[0]);
    }
}

int main(){
    freopen( "candy.in" , "r" , stdin );
    freopen( "candy.out" , "w" , stdout );
    
    scanf("%d", &T);
    
    for( int i = 0 ; i < T ; i++ ){
        read();
        solve( i );
    }
    
    return 0;
}
