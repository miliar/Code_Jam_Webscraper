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
    int R = readOne<int>();
    int left = 1 << 30, right = -1 << 30, top = 1 << 30, bottom = -1 << 30;
    vector< vector<int> > board( 110, vector<int>( 110, 0 ) );
    for ( int i = 0; i < R; i ++ ) {
        VI tmp = readMulti<int>();
        int l = tmp[0] + 1;
        int t = tmp[1] + 1;
        int r = tmp[2] + 1;
        int b = tmp[3] + 1;

        if ( l > r ) swap( l, r );
        if ( t > b ) swap( t, b );
        for ( int y = t; y <= b; y ++ )
            for ( int x = l; x <= r; x ++ )
                board[y][x] = 1;
        left = min( l, left );
        right = max( r, right );
        top = min( t, top );
        bottom = max( b, bottom );
    }
    
    //
    // DOIT!
    //
    int res = 0;
    while (1) {
        res ++;
        vector< vector<int> > nboard( 110, vector<int>( 110, 0 ) );
        int cnt = 0;

        for ( int y = top; y <= bottom; y ++ )
            for ( int x = left; x <= right; x ++ ) {
                if ( board[y][x] ) {
                    if ( board[y-1][x] + board[y][x-1] == 0 )
                        nboard[y][x] = 0;
                    else {
                        nboard[y][x] = 1;
                        cnt ++;
                    }
                }
                else {
                    if ( board[y-1][x] + board[y][x-1] == 2 ) {
                        nboard[y][x] = 1;
                        cnt ++;
                    }
                    else
                        nboard[y][x] = 0;
                }
            }
        if ( cnt == 0 )
            return res;
        board = nboard;
    }
    
    
    //
    // RESULT
    //
    
    return -1;
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

