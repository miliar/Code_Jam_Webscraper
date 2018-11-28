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
    int numPoints, D;
    cin >> numPoints;
    cin >> D;
    vector<int> points( numPoints );
    vector<int> numVendors( numPoints );
    int total = 0;
    FOR( i, 0, numPoints ) {
        cin >> points[i] >> numVendors[i];
        total += numVendors[i];
    }

    if ( total <= 1 ) return 0;
    
    //
    // DOIT!
    //
    double lo = 0;
    double hi = 4000000000000.0;
    int c = 100;
    numVendors[0] --;
    numVendors[ numPoints - 1 ] --;
    while ( c -- ) {
        double mid = ( lo + hi ) / 2;
        double cur = points[0] - mid;
        bool good = true;
        FOR( p, 0, numPoints ) {
            FOR( v, 0, numVendors[p] ) {
                cur = cur + D;
                if ( cur > points[p] + mid ) {
                    good = false;
                    goto fin;
                }
                cur = max( cur, points[p] - mid );
            }
        }
    fin:
        if ( good && cur + D <= points[ numPoints - 1 ] + mid ) {
            hi = mid;
        }
        else {
            lo = mid;
        }
    }
    
    //
    // RESULT
    //
    
    return ( lo + hi ) / 2;
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++) {
        printf( "Case #%d: %.10f\n", caseno, doCase() );
    }
    return 0;
}

