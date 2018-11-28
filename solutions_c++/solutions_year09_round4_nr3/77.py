#include <climits>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmin( T &res, const U &x ) { if ( x < res ) res = x; }
template <typename T> inline int get_bit ( const T &x, int index ) { return (int)((x >> index) & 1); }

int n;
int memo[1<<16];
char graf[16][16];

int calc(int mask) {
    if ( mask == (1<<n)-1 ) return 0;

    int &ret = memo[mask];
    if ( ret != -1 ) return ret;

    ret = INT_MAX/2;

    int av = ((1<<n)-1) & ~mask;
    for ( int sub=av; sub>0; sub=(sub-1)&av ) {
        int inside[16], ninside = 0;
        for ( int i=0; i<n; ++i ) {
            if ( get_bit(sub, i) ) inside[ninside++] = i;
        }

        bool ok = 1;
        for ( int i=0; ok && i<ninside; ++i ) {
            for ( int j=i+1; ok && j<ninside; ++j )
                ok &= graf[inside[i]][inside[j]];
        }
        if ( ok ) relaxmin(ret, 1+calc(mask | sub));
    }
    return ret;
}

int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        int k; cin >> n >> k;
        int y[n][k];
        for ( int i=0; i<n; ++i ) {
            for ( int j=0; j<k; ++j )
                cin >> y[i][j];
        }

        memset(graf, 1, sizeof graf);
        for ( int i=0; i<n; ++i ) {
            for ( int j=i+1; j<n; ++j ) {
                for ( int m=0; m+1<k; ++m ) {
                    if ( y[i][m] >= y[j][m] && y[i][m+1] <= y[j][m+1] ||
                         y[i][m] <= y[j][m] && y[i][m+1] >= y[j][m+1] )
                        graf[i][j] = graf[j][i] = 0;
                }
            }
        }

        memset(memo, -1, sizeof memo);
        cout << "Case #" << tt << ": " << calc(0) << "\n";
    }

    return 0;
} 
