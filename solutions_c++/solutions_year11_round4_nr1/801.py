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

double doCase()
{
    
    //
    // READ INPUT
    //
    int X, S, R, t, N;
    vector< pair<int,int> > foo;
    cin >> X >> S >> R >> t >> N;
    foo.push_back( make_pair( 0, 0 ) );
    FOR( i, 0, N ) {
        int b, e, w;
        cin >> b >> e >> w;
        X -= ( e - b );
        foo.push_back( make_pair( w, e - b ) );
    }
    foo[0].second = X;
    sort( foo.begin(), foo.end() );
    
    //
    // DOIT!
    //
    double remaining = t;
    double res = 0;
    FOR( i, 0, N + 1 ) {
        int dis = foo[i].second;
        int w = foo[i].first;
//        dump_( dis ); dump_( w );
        double allrun = 1.0 * dis / ( w + R );
        if ( allrun <= remaining ) {
            remaining -= allrun;
            res += allrun;
        }
        else {
            res += ( remaining + ( dis - remaining * ( w + R ) ) / ( w + S ) );
            remaining = 0;
        }
//        dump_(remaining); dump( res );
    }

    return res;
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++) {
        cout << "Case #" << caseno << ": ";
        printf( "%.10f\n", doCase() );
    }
    return 0;
}

