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
int P;
vector<int> M;
vector<ll> prices;

#define node2team( node ) ( 1 + (node) - (1<<P) )
#define inf (1LL<<50)

ll memo[3000][15];
ll solve( int node, int missed, int depth )
{
    ll& res = memo[node][missed];
    if ( res != -1 ) return res;
    res = inf;
    if ( depth == P ) {
        int team = node2team( node );
        if ( missed > M[team] )
            return res = inf;
        return res = 0;
    }

    // buy
    ll s = solve( node * 2 + 1, missed, depth + 1 );
    ll t = solve( node * 2 + 2, missed, depth + 1 );
    res = min( inf, prices[node] + s + t );
//    fprintf( stderr, "at node = %d(depth=%d): buy => %lld(price=%lld, s=%lld, t=%lld)\n", node, depth, res, prices[node], s, t );

    // not buy
    ll u = solve( node * 2 + 1, missed + 1, depth + 1 );
    ll v = solve( node * 2 + 2, missed + 1, depth + 1 );
    res = min( res, min( inf, u + v ) );
//    fprintf( stderr, "at node = %d(depth=%d): not => %lld(u=%lld, v=%lld)\n", node, depth, res, u, v );
    
    return res;
}

ll doCase()
{
    //
    // READ INPUT
    //
    P = readOne<int>();
    M = readMulti<int>();
    prices = vector<ll>();
    for ( int i = 0; i < P; i ++ ) {
        vector<ll> t = readMulti<ll>();
        reverse( ALL( t ) );
        for ( int j = 0; j < t.size(); j ++ )
            prices.push_back( t[j] );
    }
    reverse( ALL( prices ) );
//    dump_vec( prices );
    
    //
    // DOIT!
    //
    memset( memo, -1, sizeof( memo ) );
    return solve( 0, 0, 0 );
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

