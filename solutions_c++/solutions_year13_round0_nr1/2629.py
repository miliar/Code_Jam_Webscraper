#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>


char lines[15][15];

int dx[] = {1, 0, 1, 1};
int dy[] = {0, 1, 1, -1};

void solve() {
    for ( int i = 0;i < 4;++i )
        scanf ( "%s", lines[i] );
    int hasdot = 0;
    for ( int i = 0;i < 4;++i ) {
        for ( int j = 0;j < 4;++j ) {
            if ( lines[i][j] == '.' ) {
                hasdot = 1;
                continue;
            }
            for ( int k = 0;k < 4;++k ) {
                int cnt = 1;
                char c = lines[i][j];
                for ( int x = i + dx[k], y = j + dy[k];
                        x >= 0 && x < 4 && y >= 0 && y < 4;
                        x += dx[k], y += dy[k] ) {
                    if ( lines[x][y] == '.' ) break;
                    if ( c == 'T' ) c = lines[x][y];
                    if ( lines[x][y] == c || lines[x][y] == 'T' ) {
                        ++cnt;
                    } else break;
                }
                if ( cnt == 4 ) {
                    printf ( " %c won\n", c );
                    return;
                }
            }
        }
    }
    if ( hasdot )
        printf ( " Game has not completed\n" );
    else
        printf ( " Draw\n" );
}

int main() {
    int T;
    scanf ( "%d", &T );
    for ( int t = 1;t <= T;++t ) {
        printf ( "Case #%d:", t );
        solve();
    }
}