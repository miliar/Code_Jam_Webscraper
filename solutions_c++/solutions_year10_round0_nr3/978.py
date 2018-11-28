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

int doCase()
{
    //
    // READ INPUT
    //
    VI foo = readMulti<int>();
    VI groups = readMulti<int>();
    int r = foo[0];
    int k = foo[1];
    int n = foo[2];
    
    
    //
    // DOIT!
    //
    ll res = 0;
    int at = 0;
    for ( int i = 0; i < r; i ++ ) {
        int carry = 0;
        int jj;
        for ( jj = 0; jj < n; jj ++ ) {
            int j = ( at + jj ) % n;
            if ( carry + groups[j] <= k )
                carry += groups[j];
            else {
                break;
            }
        }
        at = ( at + jj ) % n;
        res += carry;
    }
    return res;
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

