#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

void recu( vector< int > Q, bool *P, int &min, int act, int step, int p );

int main()
{
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int t, k = 0;
    scanf("%d", &t );
    while( k++ < t )
    {
        int p, q;
        scanf("%d%d", &p, &q );
        vector< int > Q( q );
        for( int i = 0; i < q; ++i )
            scanf("%d", &Q[i] );
        int min = 999999;
        bool P[ p ];
        for( int i = 0; i < p; ++i )
            P[ i ] = true;
        recu( Q, P, min, 0, 0, p );
        printf("Case #%d: %d\n", k, min );
    }
    return 0;
}

int cuenta( int i, bool *P, int n )
{
    int c = 0;
    for( int j = i+1; j < n && P[j]; ++j, ++c );
    for( int j = i-1; j >= 0 && P[j]; --j, ++c );
    return c;
}

void recu( vector< int > Q, bool *P, int &min, int act, int step, int p )
{
    if( step == Q.size() )
    {
        if( act < min )
            min = act;
        return;
    }
    for( int i = 0; i < Q.size(); ++i )
    {
        if( P[ Q[ i ] - 1 ] ) // existe el prisionero
        {
            P[ Q[ i ] - 1 ] = false;
            recu( Q, P, min, act + cuenta( Q[i]-1, P, p ), step + 1, p );
            P[ Q[ i ] - 1 ] = true;
        }
    }
}
