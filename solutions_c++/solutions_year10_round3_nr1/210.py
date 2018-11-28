#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    int t, tc = 0, n, count;
    scanf( "%d", &t );
    while( tc++ < t )
    {
        scanf( "%d", &n );
        vector< pair< int, int > > M( n );
        count = 0;
        for( int i = 0; i < n; ++i )
            scanf( "%d%d", &M[i].first, &M[i].second );
        for( int i = 0; i < n; ++i )
            for( int j = i + 1; j < n; ++j )
                if( M[i].first <= M[j].first && M[i].second >= M[j].second )
                    ++count;
                else if( M[i].first >= M[j].first && M[i].second <= M[j].second )
                    ++count;
        printf( "Case #%d: %d\n", tc, count );
    }
    return 0;
}
