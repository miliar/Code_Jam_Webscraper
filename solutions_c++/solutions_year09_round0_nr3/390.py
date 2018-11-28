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
    
    gets( inp );
    stringstream ss( inp );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    
    gets( inp );
    stringstream ss( inp );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//

#define MOD 10000

int memo[501][30];
int solve( const string& str, const string& welcome, int p, int q )
{
    if ( q >= welcome.size() )
        return 1;
    if ( p >= str.size() )
        return 0;
    int& res = memo[p][q];
    if ( res != -1 ) return res;
    res = solve( str, welcome, p + 1, q );
    if ( str[p] == welcome[q] )
        res = ( res + solve( str, welcome, p + 1, q + 1 ) ) % MOD;
    return res;
}

string doCase()
{
    //
    // READ INPUT
    //
    char input[1000];
    gets( input );
    string str( input );
    
    //
    // DOIT!
    //
    memset( memo, -1, sizeof( memo ) );
    const string welcome = "welcome to code jam";
    int t = MOD + solve( str, welcome, 0, 0 );
    
    //
    // RESULT
    //
    stringstream ss;
    ss << t;
    return ss.str().substr( 1 );
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

