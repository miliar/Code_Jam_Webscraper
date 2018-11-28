/*
PROB: bot-trust
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
#if 0
#define eprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )
#else
#define eprintf(msg, ... ) 0
#endif
#define pprintf(msg, ... ) fprintf(stderr," %s:%d in %s at %.4lf :: " msg "\xA" , strrchr( __FILE__ , '\\' )+1 , __LINE__ , __FUNCTION__ , now() , ##__VA_ARGS__ )

using namespace std;

const int PUSH = 3;
const int dx[] = { -1 , 0 , 1 , 0 };
const int MAXN = 1 << 7;
const int INF = 1 << 30;

int T,N;
int dist[MAXN][MAXN][MAXN];
vector< pair<int,int> > v;

struct State{
    int r1 , r2 , cmd;
    inline State( int r1 = 0 , int r2 = 0 , int cmd = 0 ){
        this->r1 = r1;
        this->r2 = r2;
        this->cmd = cmd;
    }
    inline bool operator<( const struct State &other ) const{
        if( this->r1 != other.r1 )
            return this->r1 < other.r1;
        else if( this->r2 != other.r2 )
            return this->r2 < other.r2;
        else
            return this->cmd < other.cmd;
    }
    inline bool operator>( const struct State &other ) const{
        return other < *this;
    }
};

char getmeaningful(){
    char c = fgetc( stdin );
    while( !feof( stdin ) and ( c != 'B' and c != 'O' ) ) c = fgetc( stdin );
    return c;
}

void read(){
    scanf("%d", &N);
    
    v.clear();
    
    for( int i = 0 ; i < N ; i++ ){
        char c = getmeaningful();
        int x;
        scanf("%d", &x);
        v.push_back( make_pair( (c) == 'B' , x ) );
    }
    
    foreach( item , v ){
        eprintf("Bot #%d -> %d", item->first, item->second);
    }
}

int solve(){
    priority_queue< pair<int,State> , vector< pair<int,State> > , greater< pair<int,State> > > pq;
    pq.push( make_pair( 0 , State( 1 , 1 , 0 ) ) );
    
    for( int i = 1 ; i < MAXN ; i++ )
        for( int j = 1 ; j < MAXN ; j++ )
            for( int k = 0 ; k <= N ; k++ )
                dist[i][j][k] = INF;
    
    dist[1][1][0] = 0;
    
    while( !pq.empty() ){
        pair<int,State> top = pq.top();
        int away = top.first;
        int r1 = top.second.r1;
        int r2 = top.second.r2;
        int cmd = top.second.cmd;
        
        pq.pop();
        
        if( away > dist[r1][r2][cmd] )
            continue;
        
        eprintf("at (%d,%d,%d) = %d", r1,r2,cmd, dist[r1][r2][cmd] );
        
        if( cmd == N ) return dist[r1][r2][cmd];
        
        for( int i = 0 ; i < 4 ; i++ ){
            if( i == PUSH and v[cmd].first == 1 ) continue;
            if( i == PUSH and v[cmd].second != r1 ) continue;
            for( int j = 0 ; j < 4 ; j++ ){
                if( j == PUSH and v[cmd].first == 0 ) continue;
                if( j == PUSH and v[cmd].second != r2 ) continue;
                
                int nr1 = r1 + dx[i];
                int nr2 = r2 + dx[j];
                if( nr1 < 0 or nr1 > 100 or nr2 < 0 or nr2 > 100 ) continue;
                int ncmd = cmd + ( ( i == PUSH ) or ( j == PUSH ) );
                int ndist = dist[r1][r2][cmd] + 1;
                
                if( dist[nr1][nr2][ncmd] > ndist ){
                    dist[nr1][nr2][ncmd] = ndist;
                    pq.push( make_pair( ndist , State( nr1 , nr2 , ncmd ) ) );
                }
            }
        }
    }
    
    return 0;
}

int main(){
    freopen( "bot-trust.in" , "r" , stdin );
    freopen( "bot-trust.out" , "w" , stdout );
    
    scanf("%d\n", &T);
    
    for( int i = 0 ; i < T ; i++ ){
        read();
        printf("Case #%d: %d\n", i+1, solve());
    }
    
    return 0;
}
