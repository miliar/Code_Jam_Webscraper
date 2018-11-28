/*
TASK: B
LANG: C++
KEYW: 
*/
#include <iostream>
#include <cstdio>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <numeric>
#include <ext/hash_map>
#include <ext/hash_set>
#include <cmath>
#include <cassert>
#include <map>
#include <vector>
#include <ctime>
#include <string>
#define foreach(_var,_container) for( typeof( (_container).begin() ) _var = (_container).begin() ; _var != (_container).end() ; ++_var )
#define now() double( double( clock() ) / double( CLOCKS_PER_SEC ) )
#if 0
#define eprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )
#else
#define eprintf(msg, ... ) 0
#endif
#define pprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )

using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
typedef pair<int,int> PII;

#define PB push_back
#define MP make_pair
#define CLEAR0(x) memset( (x) , 0 , sizeof((x)) )
#define CLEAR1(x) memset( (x) , -1 , sizeof((x)) )

const double EPS = 1e-9;
const int INF = 1 << 30;

inline int epscmp( double a , double b ){
    if( fabs(a-b) < EPS )
        return 0;
    else if( a + EPS < b )
        return -1;
    else
        return 1;
}

const int MAXN = 1 << 7;

int N, S, P;
int s[MAXN];
int dp[MAXN][MAXN];

inline bool inrange( int a , int b , int maxd = 1 ){
    return abs( a - b ) <= maxd;
}

int get( int n , int s ){
    if( n == N and !s )
        return 0;
    else if( n == N )
        return -INF;
    
    int &self = dp[n][s];
    
    if( self != -1 )
        return self;
    
    self = -INF;
    
    for( int s1 = 0 ; s1 <= 10 ; s1++ ){
        if( s1 > ::s[n] ) continue;
        
        for( int s2 = max( 0 , s1 - 2 ) ; s2 <= min( 10 , s1 + 2 ) ; s2++ ){
            if( s1 + s2 > ::s[n] ) continue;
            
            int s3 = ::s[n] - s1 - s2;
            
            if( 0 <= s3 and s3 <= 10 ){
                if( !inrange( s1 , s2 , 2 ) or !inrange( s2 , s3 , 2 ) or !inrange( s1 , s3 , 2 ) )
                    continue;
                
                int needs = ( (abs( s1 - s2 ) == 2) or (abs( s2 - s3 ) == 2) or (abs( s1 - s3 ) == 2) );
                
                eprintf("At #%d -> (%d,%d,%d)", n + 1, s1, s2, s3);
                
                if( needs and !s )
                    continue;
                
                self = max( self , ((s1 >= P) or (s2 >= P) or (s3 >= P)) + get( n + 1 , s - needs ) );
            }
        }
    }
    
    return self;
}

void clear(){
    ///Warning: Clear everything used by a test!
    memset( dp , -1 , sizeof( dp ) );
}

void read(){
    /// Input read goes here
    scanf("%d %d %d", &N, &S, &P);
    
    for( int i = 0 ; i < N ; i++ )
        scanf("%d", &s[i]);
}

void solve( int testid ){
    /// Solution goes here
    
    
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d: ", testid+1);
    /// Output goes here:
    
    printf("%d", max( 0 , get( 0 , S )));
    
    /// I take care of the newline!
    printf("\xA");
}

int main(){
    freopen( "B.in" , "r" , stdin );
    freopen( "B.out" , "w" , stdout );
    
    int numtests;
    
    scanf("%d\xA", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        clear();
        read();
        solve( i );
    }
    
    return 0;
}
