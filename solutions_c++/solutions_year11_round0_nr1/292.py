#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <cstring>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump_(x)     cerr << #x << " = " << (x) << " ";
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(zZz,0,x.size()) cout << x[zZz] << " "; cout << endl


template< typename type > type readOne()
{
    type res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//

vector< pair<char,int> > sequences;

int doCase()
{
    sequences.clear();
    int n;
    cin >> n;
    FOR( i, 0, n ) {
        char c; int p;
        cin >> c >> p;
        sequences.push_back( make_pair( c, p - 1 ) );
    }
    int p = 0, q = 0, at = 0;
    for ( int t = 0; ; t ++ ) {
//        dump_( t ); dump_( p ); dump_( q ); dump( at );
        if ( at >= n ) return t;
        int dp = 0, dq = 0;
        for ( int i = at; i < n; i ++ ) {
            if ( sequences[i].first == 'O' ) {
                if ( sequences[i].second > p ) dp = 1;
                else if ( sequences[i].second < p ) dp = -1;
                break;
            }
        }
        for ( int i = at; i < n; i ++ ) {
            if ( sequences[i].first == 'B' ) {
                if ( sequences[i].second > q ) dq = 1;
                else if ( sequences[i].second < q ) dq = -1;
                break;
            }
        }
//        dump_( dp ); dump( dq );
        if ( sequences[at].first == 'O' && sequences[at].second == p ) {
            at ++;
            if ( dq != 0 ) q += dq;
        }
        else if ( sequences[at].first == 'B' && sequences[at].second == q ) {
            at ++;
            if ( dp != 0 ) p += dp;
        }
        else {
            p += dp;
            q += dq;
        }
    }
    return -1;
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;
    return 0;
}
