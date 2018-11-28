#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstdarg>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

#define	REP( i, n )         for( (i) = 0 ; (i) < (n) ; (i)++ )
#define	IREP( i, n )	    for( (i) = (n) - 1 ; (i) >= 0 ; (i)-- )
#define REPV( i, a, b )     for( (i) = (a) ; (i) <= (b) ; (i)++ )
#define IREPV( i, a, b )    for( (i) = (b) ; (i) >= (a) ; (i)-- )
#define REPIT( it, x )      for( (it) = (x).begin( ) ; (it) != (x).end( ) ; (it)++ )
#define ALL( x )            (x).begin( ), (x).end( )
#define MP                  make_pair
#define PB                  push_back
#define CLR( x )            memset( (x), 0, sizeof( x ) )
#define CLRV( x, v )        memset( (x), (v), sizeof( x ) )
#define CPY( y, x )         memcpy( (y), (x), sizeof( x ) )
#define	X                   first
#define Y                   second

typedef long long Ll;
typedef pair< int, int > Pii;
typedef pair< Ll, Ll > Pll;
typedef vector< int > Vi;
typedef vector< Ll > Vl;
typedef vector< string > Vs;

const int MAXTL = 8192, MAXLL = 80, INF = 0x3f3f3f3f;
const Ll INFL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-9;
int nl, na;
char ss[MAXTL];
    
void eatWS( int *pos )
{
    while( ss[*pos] && isspace( ss[*pos] ) )
        (*pos)++;
}

double computeProb( int *pos, const set< string > &feats )
{
    eatWS( pos );
    // ss[pos] should be '('
    assert( ss[*pos] == '(' );
    (*pos)++;

    string probStr;
    eatWS( pos );
    while( isdigit( ss[*pos] ) ||
           ss[*pos] == '.' )
    {
        probStr += ss[*pos];
        (*pos)++;
    }
    double prob = atof( probStr.c_str( ) ); 

    eatWS( pos );
    if( ss[*pos] == ')' )
    {
        (*pos)++;
        return prob;
    }

    string featName;
    double prob1, prob2;
    while( isalpha( ss[*pos] ) )
    {
        featName += ss[*pos];
        (*pos)++;
    }
    prob1 = computeProb( pos, feats );
    prob2 = computeProb( pos, feats );
    eatWS( pos );
    assert( ss[*pos] == ')' );
    (*pos)++;

    if( feats.find( featName ) == feats.end( ) )
        return prob * prob2;
    return prob * prob1;
}

int main( )
{
    int it, nt;
    scanf( "%d\n", &nt );
    for( it = 1 ; it <= nt ; it++ )
    {
        int i, j;
        char *p = ss;
        scanf( "%d\n", &nl );
        for( i = 0 ; i < nl ; i++ )
        {
            fgets( p, MAXLL + 2, stdin );
            p += strlen( p ); 
        }

        int nf;
        char buf[16];
        string animal;
        printf( "Case #%d:\n", it );

        scanf( "%d", &na );
        for( i = 0 ; i < na ; i++ )
        {
            scanf( "%s %d ", buf, &nf );
            animal = buf;

            set< string > feats;
            for( j = 0 ; j < nf ; j++ )
            {
                scanf( " %s", buf );
                feats.insert( string( buf ) );
            }

            int pos = 0;
            printf( "%.7lf\n", computeProb( &pos, feats ) );
        }
    }
    return 0;    
}
