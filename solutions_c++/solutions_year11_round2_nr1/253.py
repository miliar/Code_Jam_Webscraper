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
    int N = readOne<int>();
    vector<string> tbl( N );
    FOR( i, 0, N ) {
        string line = readOne<string>();
        tbl[i] = line;
    }
    
    //
    // DOIT!
    //

    vector<double> rpi( N ), owps( N );
    
    FOR( i, 0, N ) {
        double wp = 0;
        int c = 0, w = 0;
        FOR( j, 0, N ) if ( tbl[i][j] != '.' ) {
            c ++;
            if ( tbl[i][j] == '1' ) w ++;
        }
        wp = 1.0 * w / c;

        double owp = 0;
        int cc = 0;
        FOR( j, 0, N ) if ( tbl[i][j] != '.' ) {
            cc ++;
            int c = 0, w = 0;
            FOR( k, 0, N ) if ( k != i && tbl[j][k] != '.' ) {
                c ++;
                if ( tbl[j][k] == '1' ) w ++;
            }
            owp += 1.0 * w / c;
        }
        owp /= cc;
        owps[i] = owp;

        rpi[i] = 0.25 * wp + 0.5 * owp;
    }

    FOR( i, 0, N ) {
        double oowp = 0;
        int c = 0;
        FOR( j, 0, N ) if ( tbl[i][j] != '.' ) {
            c ++;
            oowp += owps[j];
        }
        oowp /= c;
        rpi[i] += 0.25 * oowp;
        printf( "%.10f\n", rpi[i] );
    }
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++) {
        cout << "Case #" << caseno << ":" << endl;
        doCase();
    }
    return 0;
}

