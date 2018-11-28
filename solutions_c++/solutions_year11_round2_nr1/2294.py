#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>

using namespace std;
int N;
char st[200][200];
double WP[200], OWP[200], OOWP[200], RPI[200];
int slose[200][200], swin[200][200];
vector<int> o[200];

int retrieve( int r, int idx, int mode ) {
    if ( idx <= 0 ) return 0;
    return ( mode ) ? slose[r][ idx ] : swin[r][ idx ];
}
int main() {
    int ntc;
    scanf("%d", &ntc);
    for( int TC=1; TC <= ntc; TC++ ) {
        memset( slose, 0, sizeof(slose) );
        memset( swin,  0, sizeof( swin) );
        scanf("%d", &N);
        for( int i=0; i<N; i++ ) scanf("%s", st[i]);
        for( int i=0; i<N; i++ ) {
            o[i].clear();
            int win = 0, lose = 0;
            for( int k=0; k<N; k++ ) {
                if ( '0' <= st[i][k] && st[i][k] <= '1' ) {
                    o[i].push_back( k );
                    if ( st[i][k] == '1' ) win++;
                    else lose++;
                    slose[i][k] = lose;
                    swin [i][k] = win ;
                } else {
                    slose[i][k] = retrieve( i, k-1, 1 );
                    swin [i][k] = retrieve( i, k-1, 0 );
                }
            }
            WP[i] = double( win ) / ( double(win) + double(lose) );
        }
        for( int i=0; i<N; i++ ) {
            OWP[i] = 0.0;
            for( int k=0; k<o[i].size(); k++ ) {

                int nlose = retrieve( o[i][k], N-1, 1 );
                int nwin  = retrieve( o[i][k], N-1, 0 );

                if ( st[ i ][ o[i][k] ] == '1' ) nlose--;
                else nwin--;

                OWP[i] = OWP[i] + ( double(nwin) / ( double(nlose) + double(nwin) ) );
            }
            OWP[i] = OWP[i] / double( o[i].size() );
        }
        for( int i=0; i<N; i++ ) {
            OOWP[i] = 0.0;
            for( int k=0; k<o[i].size(); k++ ) {
                OOWP[i] += OWP[ o[i][k] ];
            }
            OOWP[i] = OOWP[i] / double( o[i].size() );
        }
        for( int i=0; i<N; i++ ) {
            RPI[i] = (0.25 * WP[i]) + (0.5 * OWP[i]) + (0.25 * OOWP[i]);
        }
        printf("Case #%d:\n", TC);
        for( int i=0; i<N; i++ ) {
            printf("%.15lf\n", RPI[i]);
        }
    }
    return 0;
}
