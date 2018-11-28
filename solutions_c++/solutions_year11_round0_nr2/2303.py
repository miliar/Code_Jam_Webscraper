/*
PROB: magicka
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
#include <stack>
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

const int MAXN = 1 << 17;
const int AZ = 128;

int T,N,C,D;
char t[AZ][AZ];
char op[AZ][AZ];
char text[MAXN];

void read(){
    scanf("%d", &C);
    
    memset( t , 0 , sizeof( t ) );
    memset( op , 0 , sizeof( op ) );
    
    for( int i = 0 ; i < C ; i++ ){
        char buff[1 << 3];
        scanf("%s", buff);
        t[ buff[0] ][ buff[1] ] = t[ buff[1] ][ buff[0] ] = buff[2];
    }
    
    scanf("%d", &D);
    for( int i = 0 ; i < D ; i++ ){
        char buff[1 << 3];
        scanf("%s", buff);
        op[ buff[0] ][ buff[1] ] = op[ buff[1] ][ buff[0] ] = 1;
    }
    
    scanf("%d", &N);
    scanf("%s", text);
    
    ///printf("%s\n", text);
}

string solve(){
    string s = "";
    
    for( int i = 0 ; i < N ; i++ ){
        if( s.empty() ){
            s += text[i];
        }else{
            /// if combines?
            int len = s.size();
            if( t[ s[len-1] ][ text[i] ] ){
                s[len-1] = t[ s[len-1] ][ text[i] ];
            }else{
                int done = 0;
                for( int j = 0 ; j < len ; j++ ){
                    if( op[ text[i] ][ s[j] ] ){
                        done = 1;
                        s = "";
                        break;
                    }
                }
                if( !done ){
                    s += text[i];
                }
            }
        }
    }
    
    string news = "[";
    
    for( int i = 0 ; i < s.size() ; i++ ){
        news += s[i];
        if( i+1 != s.size() )
            news += ", ";
    }
    
    news += "]";
    
    return news;
}

int main(){
    freopen( "magicka.in" , "r" , stdin );
    freopen( "magicka.out" , "w" , stdout );
    
    scanf("%d", &T);
    
    for( int i = 0 ; i < T ; i++ ){
        read();
        printf("Case #%d: %s\n", i+1, solve().c_str());
    }
    
    return 0;
}
