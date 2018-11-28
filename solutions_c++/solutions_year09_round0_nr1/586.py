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

ifstream fin( "A-large.in" ) ;
ofstream fout( "A-large.out" ) ;

int mark[256] ;
int appear[5007] ;
string S[5007] ;
int N, D, L, check ;

void process()
{
    FOR(Case,1,N) {
        string s ;
        fin >> s ;
        int vt = 0 ;
        int kitu = 0 ;
        
        REP(kitu,L) {
            check++ ;
            if ( s[vt] == '(' ) while ( s[++vt] != ')' ) mark[ s[vt] ] = check ;
            else mark[ s[vt] ] = check ;
            
            REP(i,D)
                if ( appear[i] == check-1 && mark[ S[i][kitu] ] == check ) appear[i] = check ;            
            vt++ ;
        }
        
        int res = 0 ;
        REP(i,D) {
            res += appear[i] == check ;
            appear[i] = check ;
        }
        fout << "Case #" << Case << ": " << res << endl ;
    }
}

void info_in()
{
    fin >> L >> D >> N ;
    REP(i,D) fin >> S[i] ;
}

main()
{
    info_in() ;
    process() ;
    fout.close() ;
}
