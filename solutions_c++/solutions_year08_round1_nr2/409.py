#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

bool ct[2][2000][2000];

int main() {
    int C;
    cin >> C;
    int c = 0;
    while( c < C ) {
        int N,M;
        cin >> N >> M;
        memset(ct,false, sizeof(ct));
        int i,j,k;
        for( i = 0; i < M; i++ ) {
            int T;
            cin >> T;
            for( j = 0; j < T; j++ ) {
                int X,Y;
                cin >> X >> Y;
                ct[Y][X-1][i] = true;
            }
        }
        bool m[2000];
        bool v[2000];
        bool can = false;
        for( i = 0; i <= N; i++ ) {
            memset(m,false,sizeof(m));
            memset(v,false,sizeof(v));
            for( j = 0; j < i; j++ ) m[j] = true;
            sort(m,m+N);
            for( j = 0; j < N; j++ ) {
                int tmp = 0;
                if( m[j] ) tmp = 1;
                for( k = 0; k < M; k++ ) {
                    if( ct[tmp][j][k] ) v[k] = true;
                }
            }
            int cnt = 0;
            for( j = 0; j < M; j++ ) {
                if( v[j] ) cnt++;
            }
            //cout << cnt << endl;
            if( cnt == M ) can = true;
            if( can ) break;
            while( next_permutation(m,m+N) ) {
                memset(v,false,sizeof(v));
                for( j = 0; j < N; j++ ) {
                    int tmp = 0;
                    if( m[j] ) tmp = 1;
                    for( k = 0; k < M; k++ ) {
                        if( ct[tmp][j][k] ) v[k] = true;
                    }
                }
                int cnt = 0;
                for( j = 0; j < M; j++ ) {
                    if( v[j] ) cnt++;
                }
                //cout << cnt << endl;
                if( cnt == M ) can = true;
                if( can ) break;
            }
            if( can ) break;
        }
        printf("Case #%d:",c+1);
        if( !can ) printf(" IMPOSSIBLE\n");
        else {
            for( i = 0; i < N; i++ ) {
                if( m[i] ) printf(" 1");
                else printf(" 0");
            }
            printf("\n");
        }
        c++;
    }
    system("pause");
    return 0;
}
