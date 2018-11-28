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

string doCase()
{
    //
    // READ INPUT
    //
    vector<int> foo = readMulti<int>();
    int n = foo[0], k = foo[1];
    vector<string> board( n );
    for ( int i = 0; i < n; i ++ ) {
        board[i] = readOne<string>();
    }
    
    //
    // DOIT!
    //
    int win = 0;
    
    vector<string> nb( n );
    for ( int j = 0; j < n; j ++ ) {
        for ( int i = n - 1; i >= 0; i -- ) {
            if ( board[j][i] != '.' )
                nb[j] += board[j][i];
        }
    }
    for ( int i = 0; i < n; i ++ )
        nb[i] += string( n - nb[i].size(), '.' );
        
    for ( int i = 0; i < n; i ++ ) for ( int j = 0; j < n; j ++ ) {
        if ( nb[i][j] != '.' ) {
            for ( int dy = -1; dy <= 1; dy ++ ) for ( int dx = -1; dx <= 1; dx ++ ) if ( dx != 0 || dy != 0 )
            {
                int l;
                for ( l = 0; l < k; l ++ ) {
                    int ni = i + dy * l;
                    int nj = j + dx * l;
                    if ( ! ( 0 <= ni && ni < n && 0 <= nj && nj < n ) )
                        break;
                    if ( nb[ni][nj] != nb[i][j] )
                        break;
                }
                if ( l == k )
                    win |= ( nb[i][j] == 'R' ? 1 : 2 );
            }
        }
    }
    
    //
    // RESULT
    //
    if ( win == 0 )
        return "Neither";
    if ( win == 1 )
        return "Red";
    if ( win == 2 )
        return "Blue";
    return "Both";
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

