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

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(i,0,x.size()) cout << x[i] << " "; cout << endl


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

//       prev   pos
int memo[ 300 ][110];
int n;
vector<int> bar;
int del, in, margin;

int doit( int prev, int pos )
{
    if ( pos == n )
        return 0;
    int& res = memo[ prev ][ pos ];
    if ( res != -1 ) return res;
    res = 1 << 30;
    
    if ( prev == 256 || abs( bar[pos] - prev ) <= margin ) {
        res = doit( bar[pos], pos + 1 );
    }
    
    // insert
    if ( prev != 256 && abs( bar[pos] - prev ) > margin ) {
        for ( int t = 0; t <= 255; t ++ ) {
            if ( abs( t - prev ) <= margin )
                res = min( res, in + doit( t, pos ) );
        }
    }
    
    // delete
    res = min( res, del + doit( prev, pos + 1 ) );
    
    // modify
    for ( int t = 0; t < 256; t ++ ) {
        if ( prev == 256 || abs( t - prev ) <= margin )
            res = min( res, abs( bar[pos] - t ) + doit( t, pos + 1 ) );
    }
    
    return res;
}

int doCase()
{
    //
    // READ INPUT
    //
    vector<int> foo = readMulti<int>();
    del = foo[0];
    in = foo[1];
    margin = foo[2];
    n = foo[3];
    bar = readMulti<int>();
    
    //
    // DOIT!
    //
    memset( memo, -1, sizeof( memo ) );
    return doit( 256, 0 );
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

