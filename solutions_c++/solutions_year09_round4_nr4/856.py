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
#define dumpo(x)     cout << #x << " = " << (x) << endl
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
#define SQR( a ) ( (double)(a) * (a) )

#define MYTYPE double
MYTYPE doCase()
{
    //
    // READ INPUT
    //
    int N = readOne<int>();
    VI X( N ), Y( N ), R( N );
    FOR( i, 0, N )
    {
        VI tmp = readMulti<int>();
        X[i] = tmp[0];
        Y[i] = tmp[1];
        R[i] = tmp[2];
    }
    
    
    //
    // DOIT!
    //
    double hi = 3000;
    double lo = 1;
    FOR( c, 0, 100 )
    {
        double r = ( hi + lo ) / 2;
        vector< VI > connect( N, VI( N, 0 ) );
        bool good = true;
        FOR( i, 0, N )
        {
            if ( r < R[i] ) { good = false; break; }
            FOR( j, 0, N )
            {
                if ( i == j ) connect[i][j] = 1;
                else if ( SQR( X[i] - X[j] ) + SQR( Y[i] - Y[j] ) <= SQR( r - R[i] + r - R[j] ) )
                    connect[i][j] = 1;
            }
        }
        
        int mask;
        for ( mask = 0; mask < 1 << N; mask ++ )
        {
            bool good = true;
            FOR( i, 0, N ) if ( mask & 1 << i )
            {
                FOR( j, 0, N ) if ( mask & 1 << j )
                {
                    if ( !connect[i][j] )
                    {
                        good = false;
                        goto done;
                    }
                }
            }
            FOR( i, 0, N ) if ( !( mask & 1 << i ) )
            {
                FOR( j, 0, N ) if ( !( mask & 1 << j ) )
                {
                    if ( !connect[i][j] )
                    {
                        good = false;
                        goto done;
                    }
                }
            }
            
          done:
            if ( good )
            {
                break;
            }
        }
        
        if ( mask == 1 << N )
            good = false;
        
#if 0
        int g0 = -1, g1 = -1;
        FOR( i, 0, N ) FOR( j, 0, N ) if ( i != j )
        {
            if ( !connect[i][j] ) {
                g0 = i;
                g1 = j;
                break;
            }
        }
        
        
        if ( g0 >= 0 )
        {
            VI group0, group1;
            FOR( i, 0, N )
            {
                
            }
        }
#endif
        
        if ( good )
        {
            hi = r;
        }
        else
        {
            lo = r;
        }
    }
    
    //
    // RESULT
    //
    
    return lo;
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

