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


int R,C;
string v[2344];

void clear(){
    ///Warning: Clear everything used by a test!
}

void read(){
    /// Input read goes here
    scanf("%d %d\n", &R, &C);
    for( int i = 0 ; i < R ; i++ ){
        char buff[3445];
        scanf("%s\n", buff);
        v[i] = buff;
        //cerr << v[i] << endl;
    }
}

void solve( int testid ){
    /// Solution goes here
    
    
    while(1){
        int update = 0;
        for( int i = 0 ; i < R - 1 ; i++ ){
            for( int j = 0 ; j < C - 1 ; j++ ){
                if( v[i][j] == '#' and v[i+1][j] == '#' and v[i+1][j+1] == '#' and v[i][j+1] == '#' ){
                    v[i][j] = v[i+1][j+1] = '/';
                    v[i][j+1] = v[i+1][j] = '\\';
                    update = 1;
                }
            }
        }
        if( !update ) break;
    }
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d:\n", testid+1);
    /// Output goes here:
    
    int cool = 1;
    
    for( int i = 0 ; i < R ; i++ ){
        for( int j = 0 ; j < C ; j++ ){
            if( v[i][j] == '#' )
                cool = 0;
        }
    }
    
    if( !cool ){
        printf("Impossible\n");
    }else{
        for( int i = 0 ; i < R ; i++ ){
            cout << v[i] << endl;
        }
    }
    
    /// I take care of the newline!
}

int main(){
    freopen( "A.in" , "r" , stdin );
    freopen( "A.out" , "w" , stdout );
    
    int numtests;
    
    scanf("%d\n", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        clear();
        read();
        solve( i );
    }
    
    return 0;
}
