#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std ;

#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) for( int i=0,_n=(n);i<_n;i++)
#define DEP(i,n) for( int i=(n)-1;i>=0;i--)

#define all(a) (a).begin() , (a).end()
template<class T> inline int size(const T&c) { return c.size(); } 

typedef vector< pair<int, int> > VP ;

int h0[4] = {+0,-1,+0,+1} ;
int h1[4] = {-1,+0,+1,+0} ;
int Op[4] = {2,3,0,1} ;

int n, m ;
VP sres, start ;

inline int inside( int x, int y )
{
    return x >= 0 && x < n && y >= 0 && y < m ;
}

string S[15] ;
int mark[15][15] ;

map<VP,int> appear ;
map<VP,bool> danger ;
int xuat_hien[15][15] ;

int Checked = 0 ;

int dfs( int x, int y )
{
    xuat_hien[x][y] = 0 ;
    int res = 1 ;
    REP(z,4) {
        int dd = x + h0[z] ;
        int cc = y + h1[z] ;
        
        if ( !inside( dd, cc ) ) continue ;
        if ( S[dd][cc] == '#' ) continue ;
        if ( xuat_hien[dd][cc] != Checked ) continue ;
        res += dfs( dd, cc ) ;
    }
    return res ;
}

inline int connected( VP state )
{
    Checked++ ;
    REP(i,size(state) ) xuat_hien[ state[i].first ][ state[i].second ] = Checked ;
    return dfs( state[0].first, state[0].second ) == size( state ) ;
}

void process()
{
    memset( mark, 0, sizeof(mark) ) ;
    appear.clear() ;
    danger.clear() ;
    Checked = 0 ;
    memset( xuat_hien, 0, sizeof(xuat_hien) ) ;
    
    queue< VP > q ;
    q.push( start ) ;
    appear[start] = 1 ;
    danger[start] = false ;
    
    int Time = 0 ;
    while ( !q.empty() ) {
        VP Hehe = q.front() ;
        q.pop() ;
        
        if ( Hehe == sres ) {
            cout << appear[Hehe] - 1 << endl ;
            return ;
        }
        
        Time++ ;
        REP(i,size(Hehe)) mark[ Hehe[i].first ][ Hehe[i].second ] = Time ;
        
        REP(i,size(Hehe)) {
            int x = Hehe[i].first ;
            int y = Hehe[i].second ;
            REP(z,4) {
                int dd = x + h0[z] ;
                int cc = y + h1[z] ;
                
                if ( !inside( dd, cc ) ) continue ;
                if ( S[dd][cc] == '#' ) continue ;
                
                if ( mark[dd][cc] == Time ) continue ;
                
                dd = x - h0[z] ;
                cc = y - h1[z] ;
                
                if ( !inside( dd, cc ) ) continue ;
                if ( S[dd][cc] == '#' ) continue ;
                if ( mark[dd][cc] == Time ) continue ;
                
                VP new_state = Hehe ;
                new_state[i] = make_pair( dd, cc ) ;
                
                int connect = connected(new_state) ;
                if ( danger[Hehe] && !connect ) continue ;
                sort( all(new_state) ) ;
                
                if ( appear[new_state] ) continue ;
                danger[new_state] = !connect ;
                appear[new_state] = appear[Hehe] + 1 ;
                q.push( new_state ) ;
            }
        }
    }
    cout << -1 << endl ;
}

void init()
{
    sres = VP() ;
    start = VP() ;
    REP(i,n) {
        REP(j,m) 
            if ( S[i][j] == 'x' ) sres.push_back( make_pair(i, j) ) ;
            else if ( S[i][j] == 'o' ) start.push_back( make_pair(i, j) ) ;
            else if ( S[i][j] == 'w' ) {
                sres.push_back( make_pair(i, j) ) ;
                start.push_back( make_pair(i, j) ) ;
            }
    }
        
    sort( all(sres)  ) ;
    sort( all(start) ) ;
}

void info_in()
{
    cin >> n >> m ;
    REP(i,n) cin >> S[i] ;
}

main()
{
    int test ;
    cin >> test ;
    FOR(Case,1,test) {
        info_in() ;
        init()    ;
        cout << "Case #" << Case << ": " ;
        process() ;
    }
}
