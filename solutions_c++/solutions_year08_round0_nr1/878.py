//  dp
#include <vector>
#include <iostream>
#include <string>
using namespace std;

int F,  N,  Q;

int cnt,    rem,    ans,    lst;

vector<string>      V;

vector<string>      M;

int DP[1001][100];

int MX[1001];

int main() {
    
    freopen( "A-large.in", "r", stdin ); 
    freopen( "A_large.out","w", stdout ); 
    
    cin >> F;
    
    for( int t = 1; t <= F; ++t ) {
     
        cout << "Case #" << t << ": ";

        cin >> N >> ws;
        M.resize( N );
        for( int i = 0; i < N; ++i )
            getline( cin, M[i] );

        cin >> Q >> ws;
        V.resize( Q );
        for( int i = 0; i < Q; ++i )
            getline( cin, V[i] );

        memset( DP, 0, sizeof( DP ) );
        memset( MX, 0, sizeof( MX ) );
        
        for( int i = Q - 1; i >= 0; --i ) {
            MX[i] = -1;
            int MV = 0x7FFFFFFF;
            for( int j = 0; j < N; ++j ) {
                if( V[i] == M[j] ) DP[i][j] = -1;
                else if( i == Q - 1 ) DP[i][j] = 0;
                else {
                    DP[i][j] = 0x7FFFFFFF;
                    for( int k = i + 1; k < Q; ++k ) {
                        if( DP[k][j] != -1 )
                            DP[i][j] <?= DP[k][j];
                        DP[i][j] <?= ( DP[k][MX[k]] + 1 );
                        if( DP[k][j] == -1 )  break;
                    }
                    if( DP[i][j] < MV ) {
                        MX[i] = j;
                        MV = DP[i][j];
                    }
                }
            }
        }
        
        cout << DP[0][MX[0]] << endl;
        /*
        for( int i = 0; i < Q; ++i ) {
            for( int j = 0; j < N; ++j )
                printf( "%3d", DP[i][j] );
            puts("");
        }
        //*/
    }

}
