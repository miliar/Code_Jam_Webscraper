/* File:   watersheds.cpp
 * Author: Venkatesh
 * Created on September 3, 2009, 7:31 PM
 * Powered by NetBeans 6.5
 */
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <bitset>
#include <cctype>
#include <numeric>
#include <cstdlib>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
#define pb push_back
#define sz size()
#define all(x) (x).begin(), (x).end()
#define GI ( { int t; scanf("%d",&t); t; } )
#define dbg(x) cout << #x << "= " << x << endl;
#define dbgg(x) cout << #x << endl;
#define eps 1e-8
#define eps1 1e-5
#define pi 2*acos(0.0)
#define mp make_pair
#define ff first
#define ss second

FILE *fi = freopen( "bLarge.in", "r", stdin );
FILE *fo = freopen( "bLarge.out", "w", stdout );


int H, W;
vector< vector<int> > in;
vector< vector< pair<int,int> > > sinks;


bool compare( pair<pair<int,int>,int> p1, pair<pair<int,int>,int> p2 )
{
    if( in[p1.ff.ff][p1.ff.ss] < in[p2.ff.ff][p2.ff.ss] )
        return 1;
    else if( in[p1.ff.ff][p1.ff.ss] == in[p2.ff.ff][p2.ff.ss] )
    {
        if( p1.ss < p2.ss )
            return 1;
        else
            return 0;
    }
    else
        return 0;
}


void solve( int i, int j )
{
    vector< pair< pair<int,int>,int> > v;

    pair< pair<int,int>, int> u = mp( mp(-1,-1), 1 );
    pair< pair<int,int>, int> l = mp( mp(-1,-1), 2 );
    pair< pair<int,int>, int> r = mp( mp(-1,-1), 3 );
    pair< pair<int,int>, int> d = mp( mp(-1,-1), 4 );

    if( i > 0 )
    {
        u.ff.ff = i-1;
        u.ff.ss = j;
        v.pb( u );
    }

    if( j > 0 )
    {
        l.ff.ff = i;
        l.ff.ss = j-1;
        v.pb( l );
    }

    if( i < H-1 )
    {
        d.ff.ff = i+1;
        d.ff.ss = j;
        v.pb( d );
    }

    if( j < W-1 )
    {
        r.ff.ff = i;
        r.ff.ss = j+1;
        v.pb( r );
    }

    sort( all(v), compare );

    if( sinks[ v[0].ff.ff ][ v[0].ff.ss ].ff != -1 )
        sinks[i][j] = sinks[ v[0].ff.ff ][ v[0].ff.ss ];
    else
    {
        solve( v[0].ff.ff, v[0].ff.ss );
        sinks[i][j] = sinks[ v[0].ff.ff ][ v[0].ff.ss ];
    }

    return;
}


int main()
{
    int t = GI;

    for( int caseno=1; caseno<=t; caseno++ )
    {
        H = GI;
        W = GI;

        in.clear();
        in.resize( H, vector<int>(W) );

        for( int i=0; i<H; i++ )
            for( int j=0; j<W; j++ )
                in[i][j] = GI;

        sinks.clear();
        sinks.resize( H, vector< pair<int,int> >(W, mp(-1,-1)) );

        map< pair<int,int>, char > m;
        map< pair<int,int>, char > :: iterator it;


        for( int i=0; i<H; i++ )            // find sinks
        {
            for( int j=0; j<W; j++ )
            {
                int c = 0;
                int ref = 0;

                if( i > 0 )
                {
                    ref++;
                    if( in[i][j] <= in[i-1][j] )
                        c++;
                }

                if( j > 0 )
                {
                    ref++;
                    if( in[i][j] <= in[i][j-1] )
                        c++;
                }

                if( i < H-1 )
                {
                    ref++;
                    if( in[i][j] <= in[i+1][j] )
                        c++;
                }
                
                if( j < W-1 )
                {
                    ref++;
                    if( in[i][j] <= in[i][j+1] )
                        c++;
                }

                if( c == ref )
                {
                    sinks[i][j] = mp( i, j );
                    m.insert( mp( mp(i,j), '*' ) );

                    //cout<<i<<" "<<j<<endl;
                }
            }
        }


        for( int i=0; i<H; i++ )            // find basins
        {
            for( int j=0; j<W; j++ )
            {
                if( sinks[i][j].ff == -1 )
                {
                    /*dbgg(going to recurse...);
                    dbg(i);
                    dbg(j);*/

                    solve( i, j );
                }
            }
        }


        int c = 0;

        for( int i=0; i<H; i++ )            // assign alphabets
        {
            for( int j=0; j<W; j++ )
            {
                it = m.find( sinks[i][j] );

                if( it == m.end() )
                    cout<<"Error!!";

                if( it->ss == '*' )
                {
                    it->ss = c + 'a';
                    c++;
                }
            }
        }


        vector< vector<char> > ans( H, vector<char>(W) );

        for( int i=0; i<H; i++ )            // construct regions
        {
            for( int j=0; j<W; j++ )
            {
                it = m.find( sinks[i][j] );
                ans[i][j] = it->ss;
            }
        }

        int i, j;
        printf( "Case #%d:\n", caseno );

        for( i=0; i<H; i++ )            // print regions
        {
            for( j=0; j<W-1; j++ )
                printf( "%c ", ans[i][j] );
            printf( "%c\n", ans[i][j] );
        }
    }

    return 0;
}
