#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <cstring>
using namespace std ;

#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) for( int i=0,_n=(n);i<_n;i++)
#define DEP(i,n) for( int i=(n)-1;i>=0;i--)

const int maxS = 107 ;

int h0[4] = {-1,+0,+0,+1} ;
int h1[4] = {+0,-1,+1,+0} ;

int W, H ;
int lab[maxS*maxS], altitude[maxS][maxS], basin[maxS*maxS] ;

int get_root( int i, int j )
{
    int node = i * W + j ;
    while ( lab[node] >= 0 ) node = lab[node] ;
    return node ;
}

void _union( int u, int v )
{
    if ( lab[u] <= lab[v] ) {
        lab[u] += lab[v] ;
        lab[v] = u ;
    }
    else _union( v, u ) ;
}

int inside( int x, int y )
{
    return x >= 0 && y >= 0 && x < H && y < W ;
}

void process()
{
    memset( lab, -1, sizeof(lab) ) ;
    REP(i,H)
        REP(j,W) {
            int vi = i ;
            int vj = j ;
            REP(z,4) {
                int dd = i + h0[z] ;
                int cc = j + h1[z] ;
                if ( !inside( dd, cc ) ) continue ;
                if ( altitude[i][j] <= altitude[dd][cc] ) continue ;
                if ( altitude[dd][cc] < altitude[vi][vj] ) vi = dd, vj = cc ;
            }
            if ( vi != i || vj != j ) _union( get_root(i, j), get_root(vi, vj) ) ;
        }
        
    memset( basin, 0, sizeof(basin) ) ;
    int nbasin = 0 ;
    REP(i,H) {
        REP(j,W) {
            int root = get_root(i, j) ;
            int node = i * W + j ;
            if ( !basin[root] ) basin[root] = ++nbasin ;
            if ( j > 0 ) printf(" " ) ;
            printf("%c",basin[root]+'a'-1) ;
        }
        printf("\n") ;
    }
}

void info_in()
{
    scanf("%d%d",&H,&W) ;
    REP(i,H)
    REP(j,W) scanf("%d",&altitude[i][j]) ;
}

main()
{
    freopen( "B-large.in" , "r" , stdin ) ;
    freopen( "B-large.out" , "w" , stdout ) ;
    int T ;
    scanf("%d",&T) ;
    FOR(Case,1,T) {
        info_in() ;
        printf("Case #%d:\n",Case) ;
        process() ;
    }
}
