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
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 )
using namespace std;

typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

struct dbg {
    //dbg() : dbg_( cerr ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    ostringstream os; dbg() : dbg_( os ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    ~dbg() { dbg_ << endl; }
    dbg & operator <<( char const * str ) { dbg_ << str << ' '; return *this; }
    template < class T > dbg & operator <<( T const & t ) { dbg_ << t << ' '; return *this; }
    template < class T, class U > dbg & operator <<( pair< T, U > const & p ) { dbg_ << '('; *this << p.first; *this << p.second; dbg_ << ") "; return *this; }
    template < class T > dbg & operator <<( vector< T > const & v ) { print( all( v ) ); return *this; }
    template < class T, int N > dbg & operator <<( T (&v)[N] ) { print( v, v + N ); return *this; }
    template < class Iter > void print( Iter p, Iter q ) { dbg_ << '{'; for ( ; p != q; ++p ) *this << *p; dbg_ << "} "; }
    template < class T > dbg & operator <<( vector< vector< T > > const & v ) { for ( int i = 0; i != v.size(); ++i ) { dbg_ << ( i ? ' ' : '{' ); print( all( v[i] ) ); dbg_ << ( i == v.size() - 1 ? "} " : "\n" ); } return *this; }
    template < class T, int N, int M > dbg & operator <<( T (&v)[N][M] ) { for ( int i = 0; i != N; ++i ) { dbg_ << ( i ? ' ' : '{' ); print( v[i], v[i] + M ); dbg_ << ( i == N - 1 ? "} " : "\n" ); } return *this; }
    ostream & dbg_;
};

std::ifstream in( "a.in" );
std::ofstream out( "a.out" );

void main() {
    int ntests;
    in >> ntests;
    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        int n;
        in >> n;
        string s;
        vs names( n );
        getline( in, s);
        for ( int i = 0; i < n; ++i )
            getline( in, names[i] );

        dbg() << names;
        int m, res = 0;
        in >> m;
        getline( in, s );

        vi mark( n );
        int total = 0;

        for ( int i = 0; i < m; ++i ) {
            getline( in, s );
            int eng = find( all( names ), s ) - names.begin();
            dbg() << eng;
            if ( !mark[eng] ) {
                if ( total == n - 1 ) {
                    total = 1;
                    mark = vi( n );
                    mark[eng] = 1;
                    ++res;
                    dbg() << "switch";
                } else {
                    ++total;
                    mark[eng] = 1;
                }
            }
        }

        out << "Case #" << ntest << ": " << res << endl;
    }
}