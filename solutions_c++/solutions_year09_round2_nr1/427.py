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

ifstream fin( "A-large.IN" ) ;
//#define fin cin
FILE *fo = fopen( "A-large.OUT" , "w" ) ;

int q[1000], Node[1000], E[1000][2] ;
int start[1000] ;
vector<string> a ;
string Tree ;

double getValue( string s )
{
    istringstream zzz( s ) ;
    double res ;
    zzz >> res ;
    return res ;
}

void process()
{
    string SS ;
    getline( fin, SS ) ;
    istringstream sin( SS ) ;
    int N ;
    sin >> N ;
    REP(i,N) {
        getline( fin, SS ) ;
        istringstream line( SS ) ;
        
        map<string,int> mk ;
        mk.clear() ;
        
        string name ;
        int tt ;
        line >> name >> tt ;
        REP(j,tt) {
            string feature ;
            line >> feature ;
            mk[feature] = 1 ;
        }
        int root = 1 ;
        double res = 1 ;
        do {
            res = res * getValue( a[ start[root]+1 ] ) ;
            if ( !E[root][0] ) break ;
            string feature = a[ start[root] + 2 ] ;
            if ( mk[feature] ) root = E[root][0] ;
            else root = E[root][1] ;
        }
        while (1) ;
        fprintf(fo,"%.7lf\n",res) ;
    }
}

void init()
{
    istringstream sin( Tree ) ;
    int vt = 0 ;
    int pt = 0 ;
    a.clear() ;
    a.push_back( "" ) ;
    string s ;
    int last = 0 ;
    while ( sin >> s ) {
        vt++ ;
        if ( s == "(" ) {
            q[++last] = vt ;
            Node[last] = ++pt ;
            E[pt][0] = E[pt][1] = 0 ;
        }
        else if ( s == ")" ) {
            int u = Node[last] ;
            start[u] = q[last] ;
            last-- ;
            if ( !last ) continue ;
            int cha = Node[last] ;
            if ( E[cha][0] ) E[cha][1] = u ; else E[cha][0] = u ;
        }
        a.push_back( s ) ;
    }
}

void info_in()
{
    string SS ;
    getline( fin, SS ) ;
    istringstream sin( SS ) ;
    int L ;
    sin >> L ;
    Tree = "" ;
    REP(i,L) {
        getline( fin, SS ) ;
        string xau = " " ;
        REP(j,SS.size())
            if ( SS[j] == '(' ) xau = xau + " ( " ;
            else if ( SS[j] == ')' ) xau = xau + " ) " ;
            else xau = xau + SS[j] ;
        xau = xau + " " ;
        Tree = Tree + xau ;
    }
}

main()
{
    string SS ;
    getline( fin, SS ) ;
    istringstream sin( SS ) ;
    int test ;
    sin >> test ;
    FOR(Case,1,test) {
        fprintf(fo,"Case #%d:\n",Case) ;
        info_in() ;
        init()    ;
        process() ;
    }
    fclose( fo ) ;
}
