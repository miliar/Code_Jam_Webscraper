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
#include <cassert>
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

const int NUM = 3;
const int ALPHA = 1 << 8;
const char *MAP[][2] = 
{
    { "ejp mysljylc kd kxveddknmc re jsicpdrysi" , "our language is impossible to understand" },
    { "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" , "there are twenty six factorial possibilities" },
    { "de kr kd eoya kw aej tysr re ujdr lkgc jv" , "so it is okay if you want to just give up" }
};

int N;

string mapping( ALPHA , 0 );
string now;

void init(){
    mapping['y'] = 'a';
    mapping['e'] = 'o';
    mapping['q'] = 'z';
    mapping['z'] = 'q';
    
    for( int i = 0 ; i < ALPHA ; i++ )
        if( !( i >= 'a' and i <= 'z' ) )
            mapping[i] = i;
    
    for( int i = 0 ; i < NUM ; i++ ){
        int s = strlen( MAP[i][0] );
        
        assert( s == strlen( MAP[i][1] ) );
        
        for( int j = 0 ; j < s ; j++ )
            mapping[ MAP[i][0][j] ] = (char) MAP[i][1][j];
    }
    
    for( int i = 'a' ; i <= 'z' ; i++ ){
        int count = ::count( mapping.begin() , mapping.end() , (char) i );
        
        if( !count )
            eprintf("nothing maps to %c", i);
        else if( count > 1 )
            eprintf("more than one thing maps to %c", i);
    }
}

void read(){
    /// Input read goes here
    static char buffer[256];
    
    gets( buffer );
    
    int s = strlen( buffer );
    
    if( buffer[s - 1] == '\n' )
        buffer[s - 1] = 0;
    
    now = string( buffer );
}

void solve( int testid ){
    /// Solution goes here
    
    string result = "";
    
    for( int i = 0 ; i < now.size() ; i++ )
        result += mapping[ now[i] ];
    
    /// Warning: The " " after : INCLUDED!!!
    printf("Case #%d: ", testid+1);
    /// Output goes here:
    
    printf("%s", result.c_str());
    
    /// I take care of the newline!
    printf("\xA");
}

int main(){
    freopen( "A.in" , "r" , stdin );
    freopen( "A-small.out" , "w" , stdout );
    
    init();
    
    int numtests;
    
    scanf("%d\n", &numtests);
    
    for( int i = 0 ; i < numtests ; i++ ){
        read();
        solve( i );
    }
    
    return 0;
}
