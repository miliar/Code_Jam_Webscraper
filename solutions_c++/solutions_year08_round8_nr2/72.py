#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "b.in" );
ofstream out( "b.out" );

template < class T > int index( vector< T > & v, T const & t ) {
    int pos = find( v.begin(), v.end(), t ) - v.begin();
    if ( pos == v.size() ) v.push_back( t );
    return pos;
}

typedef pair< int, pair< int, int > > pos_t;
typedef map< pos_t, int > map_t;

pos_t make_pos( int a, int b, int c ) {
    return make_pair( a, make_pair( b, c ) );
}

bool make_pos( pos_t const & p, int c, pos_t & res ) {
    static vi v;
    v.clear();
    if ( p.first != -1 ) v.push_back( p.first );
    if ( p.second.first != -1 ) v.push_back( p.second.first );
    if ( p.second.second != -1 ) v.push_back( p.second.second );
    v.push_back( c );
    sort( all( v ) );
    v.erase( unique( all( v ) ), v.end() );
    if ( v.size() > 3 ) return false;
    while ( v.size() < 3 ) v.push_back( -1 );
    res = make_pair( v[0], make_pair( v[1], v[2] ) );
    return true;
}

void main() {
    int ntests;
    in >> ntests;
    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        out << "Case #" << ntest << ": ";

        vs colors;
        int n;
        vvi c, r;
        in >> n;
        c = r = vvi( 10001 );
        for ( int i = 0; i < n; ++i ) {
            string s;
            int left, right;
            in >> s >> left >> right;
            int color = index( colors, s );
            c[left].push_back( color );
            r[left].push_back( right );
        }

        int const max = 10001;
        vector< map_t > v( max );
        v[0][make_pos( -1, -1, -1 )] = 0;
        for ( int i = 1; i < max; ++i ) {
            if ( v[i-1].empty() ) break;
            for ( map_t::iterator it = v[i-1].begin(); it != v[i-1].end(); ++it )  {
                for ( int j = 0; j < c[i].size(); ++j ) {
                    pos_t pos;
                    if ( make_pos( it->first, c[i][j], pos ) ) {
                        for ( int k = i; k <= r[i][j]; ++k ) {
                            if ( v[k].find( pos ) == v[k].end() ) {
                                v[k][pos] = it->second + 1;
                            } else {
                                int & t = v[k][pos];
                                t = min( t, it->second + 1 );
                            }
                        }
                    }
                }
            }
        }

        if ( v[max - 1].empty() ) {
            out << "IMPOSSIBLE\n";
            continue;
        }
        int res = n;
        for ( map_t::iterator it = v[max-1].begin(); it != v[max-1].end(); ++it ) {
            res = min( res, it->second );
        }
        out << res << endl;
    }
}