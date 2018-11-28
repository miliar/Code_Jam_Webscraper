#include <iostream>
#include <algorithm>
using namespace std;

int     T,  N,  K;

int     val[2][20000];

int     expt;

bool    type[20000], chg[20000];

int     cnt[20000];

const int MAX = 0x7FFFFFFE / 2;

int main() {
    
    freopen( "A-large.in", "r", stdin );
    freopen( "result.txt", "w", stdout );
    
    cin >> T;
    
    for( int t = 1; t <= T; ++t ) {
    
        cin >> N >> expt;
        
        K = N / 2;
        
        for( int i = 1; i <= N; ++i )
            val[0][i] = val[1][i] = MAX;
        
        for( int i = 1; i <= K; ++i )
            cin >> type[i] >> chg[i];
            
        for( int i = K + 1; i <= N; ++i ) {
            int x;
            cin >> x;
            val[x][i] = 0;
        }
            
        for( int i = K; i >= 1; --i ) {
            int x0 = val[0][2*i], y0 = val[0][2*i+1],
                x1 = val[1][2*i], y1 = val[1][2*i+1];
            if( type[i] ) {
                val[1][i] <?= x1 + y1;
                val[0][i] <?= x0 + y0;
                val[0][i] <?= x0 + y1;
                val[0][i] <?= x1 + y0;
                if( chg[i] ) {
                    val[1][i] <?= ( x1 + y1 + 1 );
                    val[1][i] <?= ( x1 + y0 + 1 );
                    val[1][i] <?= ( x0 + y1 + 1 );
                    val[0][i] <?= ( x0 + y0 + 1 );
                }
            }
            else {
                val[1][i] <?= x1 + y1;
                val[1][i] <?= x1 + y0;
                val[1][i] <?= x0 + y1;
                val[0][i] <?= x0 + y0;
                if( chg[i] ) {
                    val[1][i] <?= ( x1 + y1 + 1 );
                    val[0][i] <?= ( x1 + y0 + 1 );
                    val[0][i] <?= ( x0 + y1 + 1 );
                    val[0][i] <?= ( x0 + y0 + 1 );
                }
            }
        }
        
        printf( "Case #%d: ", t );
        if( val[expt][1] == MAX )   puts( "IMPOSSIBLE" );
        else                        cout << val[expt][1] << endl;
    }
    
}
