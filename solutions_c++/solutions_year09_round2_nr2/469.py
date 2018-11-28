#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <cstring>
#include <set>
#include <map>
using namespace std ;

#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) for( int i=0,_n=(n);i<_n;i++)
#define DEP(i,n) for( int i=(n)-1;i>=0;i--)

ifstream fin( "B-large.IN" ) ;
ofstream fout( "B-large.OUT" ) ; 
int A[10], C[100], Ok[10] ;

void process()
{
    string S ;
    fin >> S ;
    memset( A, 0, sizeof(A) ) ;
    REP(i,S.size()) A[ S[i] - '0' ]++ ;
    
    REP( i, S.size() ) C[i] = S[i] - '0' ;
    if ( !next_permutation( C, C+S.size() ) ) {
        FOR(i,1,9)
            if ( A[i] ) {
                fout << i ;
                A[i]-- ;
                break ;
            }
            
        fout << 0 ;
        REP(i,10) 
            REP(j,A[i]) fout << i ;
    }
    else REP(i, S.size()) fout << C[i] ;
    fout << endl ;
}

main()
{
    int test ;
    fin >> test ;
    FOR(Case,1,test) {
        fout << "Case #" << Case << ": " ;
        process() ;
    }
    fout.close() ;
}
