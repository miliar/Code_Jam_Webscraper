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

string Pattern = "welcome to code jam" ;
const int MOD = 10000 ;

ifstream fin( "C-large.in" ) ;
ofstream fout( "C-large.out" ) ;

int d[507][20] ;

int cal()
{
    string S ;
    getline( fin, S ) ;
    memset( d, 0, sizeof(d) ) ;
    if ( S[0] == 'w' ) d[0][0] = 1 ;
    FOR(i,1,S.size()-1) {
        d[i][0] = ( d[i-1][0] + ( S[i] == 'w' ) ) % MOD ;
        FOR(j,1,Pattern.size()-1) {
            d[i][j] = d[i-1][j] ;
            if ( S[i] == Pattern[j] ) d[i][j] = ( d[i][j] + d[i-1][j-1] ) % MOD ;
        }
    }
    return d[S.size()-1][Pattern.size()-1] ;
}

main()
{
    int N ;
    string SS ;
    getline( fin, SS );
    istringstream sin( SS ) ;
    sin >> N ;
    FOR(Case,1,N) {
        fout << "Case #" << Case << ": " ;
        int res = cal() ;
        string sres = "" ;
        REP(i,4) {
            sres += res % 10 + '0' ;
            res /= 10 ;
        }
        reverse( sres.begin(), sres.end() ) ;
        fout << sres << endl ;
    }
    fout.close() ;
}

//welcome to code jam
