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
int doCase()
{
    //
    // READ INPUT
    //
    vector<int> foo = readMulti<int>();
    int a1 = foo[0], a2 = foo[1], b1 = foo[2], b2 = foo[3];
    
    
    //
    // DOIT!
    //
    int res = 0;
    for ( int a = a1; a <= a2; a ++ ) for ( int b = b1; b <= b2; b ++ ) {
        if ( doit( a, b ) ) {
            res ++;
        }
    }
    
    
    //
    // RESULT
    //
    return res;
}

int main()
{
    memset( memo, -1, sizeof( memo ) );
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

