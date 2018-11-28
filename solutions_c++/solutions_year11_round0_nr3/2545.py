#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T;
    scanf( "%d", &T );
    for ( int tc = 1; tc <= T; tc++ ) {
        int N, sol = 0;
        scanf( "%d", &N );
        vector<int> vals;
        for ( int i = 0; i < N; i++ ) {
            int v;
            scanf( "%d", &v );
            vals.push_back( v );
        }
        printf( "Case #%d: ", tc );
        for ( int i = 0; i < 20; i++ ) {
            int count = 0;
            for ( int j = 0; j < N; j++ )
                if ( vals[j] & (1<<i) ) count++;
            if ( count&1 ) goto fail;
        }
        sort( vals.begin(), vals.end() );
        for ( int i = 1; i < N; i++ ) sol += vals[i];
        printf( "%d\n", sol );
        continue;
    fail:
        printf( "NO\n" );
    }
}
