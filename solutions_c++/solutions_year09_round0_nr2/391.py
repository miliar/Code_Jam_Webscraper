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

vector<string> doCase()
{
    //
    // READ INPUT
    //
    VI t = readMulti<int>();
    int H = t[0], W = t[1];
    vector< vector<int> > tbl;
    for ( int i = 0; i < H; i ++ )
    {
        VI t = readMulti<int>();
        tbl.PB( t );
    }
    
    //
    // DOIT!
    //
    vector<int> tbl2( H * W );
    FOR( i, 0, W * H )
        tbl2[i] = i;
    
    int dx[] = {  0, -1, +1,  0 };
    int dy[] = { -1,  0,  0, +1 };
    FOR( i, 0, H )
        FOR( j, 0, W )
        {
            int minA = tbl[i][j];
            int mi = i, mj = j;
            FOR( dir, 0, 4 )
            {
                int ni = i + dy[dir], nj = j + dx[dir];
                if ( 0 <= ni && ni < H && 0 <= nj && nj < W )
                {
                    if ( tbl[ni][nj] < minA )
                    {
                        minA = tbl[ni][nj];
                        mi = ni;
                        mj = nj;
                    }
                }
            }
            tbl2[i * W + j] = mi * W + mj;
        }
        
        
    while ( 1 )
    {
        /*
        FOR( i, 0, H )
        {
            cout << endl;
            FOR( j, 0, W )
                fprintf( stdout, "%03d ", tbl2[i * W + j] );
        }
        cout << endl;
        */
        
        int changed = 0;
        FOR( i, 0, W * H )
        {
            int n = tbl2[i];
            if ( tbl2[n] != n )
            {
                tbl2[i] = tbl2[n];
                changed ++;
            }
        }
        if ( changed == 0 ) break;
    }
    
    
    //
    // RESULT
    //
    
    vector<string> res( H, string( W, '-' ) );
    map< int, char > basins;
    char cur = 'a';
    FOR( i, 0, W * H )
    {
        int y = i / W;
        int x = i % W;
        if ( basins.count( tbl2[i] ) == 0 )
        {
            basins[ tbl2[i] ] = cur;
            cur ++;
        }
        res[y][x] = basins[ tbl2[i] ];
    }
    
    return res;
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
    {
        cout << "Case #" << caseno << ":\n";
        vector<string> res = doCase();
        for ( int i = 0; i < res.size(); i ++ )
        {
            for ( int j = 0; j < res[i].size(); j ++ )
            {
                if ( j > 0 )
                    cout << ' ';
                cout << res[i][j];
            }
            cout << endl;
        }
    }

	return 0;
}

