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

int doCase()
{
    
    //
    // READ INPUT
    //
    int R, C, D;
    cin >> R >> C >> D;
    vector<string> tbl( R );
    FOR( i, 0, R ) {
        cin >> tbl[i];
    }

    int res = 0;
    //
    // DOIT!
    //
    FOR( y, 0, R ) FOR( x, 0, C ) FOR( len, 3, 11 ) {
        if ( y + len > R || x + len > C ) continue;
        double wx = 0, wy = 0;
        double total = 0;
        FOR( i, 0, len ) FOR( j, 0, len ) {
            if ( i == 0       && j == 0 ) continue;
            if ( i == len - 1 && j == 0 ) continue;
            if ( i == len - 1 && j == len - 1 ) continue;
            if ( i == 0       && j == len - 1 ) continue;
            
            int d = D + ( tbl[y+i][x+j] - '0' );
            wx += ( i + 0.5 - len / 2.0 ) * d;
            wy += ( j + 0.5 - len / 2.0 ) * d;
            //wy += ( i + 0.5 ) * d;
            //wx += ( j + 0.5 ) * d;
            //total += d;
        }
        //wx /= total;
        //wy /= total;
        //if ( fabs( wx - len / 2.0 ) < 1e-8 && fabs( wy - len / 2.0 ) < 1e-8 ) {
        //    res = max( res, len );
        //}
        //dump_( wx ); dump( wy );
//        if ( fabs( wx ) < 1e-10 && fabs( wy ) < 1e-10 ) {
        if ( wx == 0 && wy == 0 ) {
            res = max( res, len );
        }
    }
    
    
    //
    // RESULT
    //
    return res;

}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++) {
        int res = doCase();
        cout << "Case #" << caseno << ": ";
        if ( res == 0 ) cout << "IMPOSSIBLE";
        else cout << res;
        cout << endl;
    }
    return 0;
}

