/*
TASK: C
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
#include <set>
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

const int MAXA = 1 << 21;
const int MAXLOG = 8;

int A, B;
vector< int > numbers[MAXA];

int getrev( int myx ){
    /// A <= myx <= B !
    
    static int dig[MAXLOG];
    
    int at = 0, x = myx;
    
    while( x )
        dig[ at++ ] = x % 10, x /= 10;
    
    int result = 0;
    
    for( int j = 0 ; j < at ; j++ ){
        int y = 0;
        
        for( int i = j ; i >= 0 ; i-- )
            y = 10 * y + dig[i];
        
        for( int i = at - 1 ; i > j ; i-- )
            y = 10 * y + dig[i];
        
        if( A <= y and y <= B )
            ++result;
        
        eprintf("%d -> %d", x, y);
    }
    
    return result;
}

int get( int x ){
    int old = x;
    
    int log = 1;
    
    while( log * 10 <= x ) log *= 10;
    
    vector< int > &all = numbers[x];
    
    do{
        int last = x % 10;
        x /= 10;
        
        x = last * log + x;
        
        //if( A <= x and x <= B )
        if( log <= x and x < log * 10 ) /// same number of digits
            all.push_back( x );
        
        //eprintf("%d -> %d", old, x);
    }while( x != old );
    
    sort( all.begin() , all.end() );
    all.erase( unique( all.begin() , all.end() ) , all.end() );
    
    return all.size();
}

int query( int x , int a , int b ){
    /// a <= x and x <= b is required

    vector< int > :: iterator lo = upper_bound( numbers[x].begin() , numbers[x].end() , x );
    vector< int > :: iterator hi = upper_bound( numbers[x].begin() , numbers[x].end() , b );
    
    return hi - lo;
}

void init(){
    /// Calculates the numbers
    for( int i = 1 ; i < MAXA ; i++ )
        get(i);
}

void read(){
    scanf("%d %d", &A, &B);
}

void solve( int testid ){
    /// Solution goes here
    
    int answer = 0;
    
    eprintf("A is %d , B is %d", A, B);
    
    for( int i = A ; i <= B ; i++ )
        answer += query( i , A , B );
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d: ", testid+1);
    /// Output goes here:
    
    printf("%d", answer);
    
    /// I take care of the newline!
    printf("\xA");
}

int main(){
    freopen( "C.in" , "r" , stdin );
    freopen( "C-small.out" , "w" , stdout );
    
    init();
    
    int numtests;
    
    scanf("%d\xA", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        read();
        solve( i );
    }
    
    return 0;
}
