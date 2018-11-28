/*
TASK: A
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
const ll INF = 1LL << 60;

inline int epscmp( double a , double b ){
    if( fabs(a-b) < EPS )
        return 0;
    else if( a + EPS < b )
        return -1;
    else
        return 1;
}

int N;
string in[120];

double WP( int x ){
    int all = count( in[x].begin() , in[x].end() , '0' );
    int c = count( in[x].begin() , in[x].end() , '1' );
    if( c + all == 0 ) return 1;
    return c / (double) ( c + all );
}
double OWP( int x ){
    double sum = 0;
    int cnt = 0;
    for( int i = 0 ; i < N ; i++ ){
        if( in[i][x] == '.' ) continue;
        cnt++;
        int zeros = 0, ones = 0;
        for( int j = 0 ; j < N ; j++ ){
            if( j == x ) continue;
            if( in[i][j] == '1' ) ones++;
            else if( in[i][j] == '0' ) zeros++;
        }
        sum += ones / double( ones + zeros );
    }
    
    return sum / cnt;
}
double OOWP( int x ){
    if( N == 1 ) return 0;
    double sum = 0;
    int cnt = 0;
    for( int i = 0 ; i < N ; i++ ){
        if( in[i][x] == '.' ) continue;
        cnt++;
        sum += OWP( i );
    }
    return sum / cnt;
}

void clear(){
    ///Warning: Clear everything used by a test!
}

void read(){
    /// Input read goes here
    cin >> N;
    for( int i = 0 ; i < N ; i++ ){
        cin >> in[i];
        //cout << "#" << i +1 << " " << in[i] << endl;
    }
}

void solve( int testid ){
    /// Solution goes here
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d:\n", testid+1);
    /// Output goes here:
    
    for( int i = 0 ; i < N ; i++ ){
        eprintf("Team #%d: WP = %.3lf, OWP = %.3lf, OOWP = %.3lf", i+1, WP(i), OWP(i), OOWP(i));
        printf("%.10lf\n", 0.25 * WP(i) + 0.5 * OWP(i) + 0.25 * OOWP(i) );
    }
    
}

int main(){
    freopen( "A.in" , "r" , stdin );
    freopen( "A.out" , "w" , stdout );
    
    int numtests;
    
    scanf("%d", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        clear();
        read();
        solve( i );
    }
    
    return 0;
}
