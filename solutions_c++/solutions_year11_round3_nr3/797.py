/*
TASK: C
LANG: C++
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
#include <map>
#include <vector>
#include <ctime>
#include <string>
#define foreach(_var,_container) for( typeof( (_container).begin() ) _var = (_container).begin() ; _var != (_container).end() ; ++_var )
#define now() double( double( clock() ) / double( CLOCKS_PER_SEC ) )
#if 1
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
const ll INF = 1LL << 60;

inline int epscmp( double a , double b ){
    if( fabs(a-b) < EPS )
        return 0;
    else if( a + EPS < b )
        return -1;
    else
        return 1;
}

int L,N,H;
int f[65465];

void clear(){
    ///Warning: Clear everything used by a test!
}

void read(){
    /// Input read goes here
    scanf("%d %d %d", &N, &L, &H);
    for( int i = 0 ; i < N ; i++ ){
        scanf("%d", &f[i]);
        //cerr << f[i] << endl;
    }
}

inline bool can( int x ){
    /// check if it divides them all
    int cnt = 0;
    for( int i = 0 ; i < N ; i++ ){
        if( ( f[i] % x == 0 ) or ( x % f[i] == 0 ) ) cnt++;
    }
    return cnt == N;
}

void solve( int testid ){
    /// Solution goes here
    
    int i = 0;
    
    for( i = L ; i <= H ; i++ ){
        if( can( i ) ){
            break;
        }
    }
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d: ", testid+1);
    /// Output goes here:
    
    if( i == H + 1 ) printf("NO");
    else printf("%d", i);
    
    /// I take care of the newline!
    printf("\n");
}

int main(){
    freopen( "C.in" , "r" , stdin );
    freopen( "C.out" , "w" , stdout );
    
    int numtests;
    
    scanf("%d", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        clear();
        read();
        solve( i );
    }
    
    return 0;
}
