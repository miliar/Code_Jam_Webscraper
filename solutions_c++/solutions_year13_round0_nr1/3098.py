#include <cstdio>
#include <cstdlib>
using namespace std;

char board[4][4];

int main() {
    freopen("A-large.txt", "r", stdin);
    freopen("A-large-out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for ( int i = 0; i < t; i++ ) {
        for ( int j = 0; j < 4; j++ ) {
            scanf("%s", &board[j]);
        }
        int num_o = 0, num_x = 0, num_t = 0, cur_count = 0;
        /* Check horizontal wins */
        for ( int j = 0; j < 4; j++ ) {
            num_o = 0;
            num_t = 0;
            num_x = 0;
            for ( int k = 0; k < 4; k++ ) {
                if ( board[j][k] == 'O' ) num_o++;
                if ( board[j][k] == 'X' ) num_x++;
                if ( board[j][k] == 'T' ) num_t++;
            }
            if ( num_o + num_t == 4 ) {
                 printf("Case #%d: O won\n", i+1);
                 goto restart;
            }
            if ( num_x + num_t == 4 ) {
                 printf("Case #%d: X won\n", i+1);
                 goto restart;
            }
        }
        /* Check vertical wins */
        for ( int k = 0; k < 4; k++ ) {
            num_o = 0;
            num_x = 0;
            num_t = 0;
            for ( int j = 0; j < 4; j++ ) {
                if ( board[j][k] == 'O' ) num_o++;
                if ( board[j][k] == 'X' ) num_x++;
                if ( board[j][k] == 'T' ) num_t++;
            }
            if ( num_o + num_t == 4 ) {
                 printf("Case #%d: O won\n", i+1);
                 goto restart;
            }
            if ( num_x + num_t == 4 ) {
                 printf("Case #%d: X won\n", i+1);
                 goto restart;
            }
        }
        /* Check diagonal wins */
        num_o = 0;
        num_x = 0;
        num_t = 0;
        for ( int j = 0; j < 4; j++ ) {
            if ( board[j][j] == 'O' ) num_o++;
            if ( board[j][j] == 'X' ) num_x++;
            if ( board[j][j] == 'T' ) num_t++;
        }
        if ( num_o + num_t == 4 ) {
             printf("Case #%d: O won\n", i+1);
             goto restart;
        }
        if ( num_x + num_t == 4 ) {
             printf("Case #%d: X won\n", i+1);
             goto restart;
        }
        num_o = 0;
        num_x = 0;
        num_t = 0;
        for ( int j = 0; j < 4; j++ ) {
            if ( board[j][3-j] == 'O' ) num_o++;
            if ( board[j][3-j] == 'X' ) num_x++;
            if ( board[j][3-j] == 'T' ) num_t++;
        }
        if ( num_o + num_t == 4 ) {
             printf("Case #%d: O won\n", i+1);
             goto restart;
        }
        if ( num_x + num_t == 4 ) {
             printf("Case #%d: X won\n", i+1);
             goto restart;
        }
        /* Check draw */
        cur_count = 0;
        for ( int j = 0; j < 4; j++ ) {
            for ( int k = 0; k < 4; k++ ) {
                if ( board[j][k] != '.' ) cur_count++;
            }
        }
        if ( cur_count == 16 ) printf("Case #%d: Draw\n", i+1);
        else printf("Case #%d: Game has not completed\n", i+1);
        restart:
                continue;
    }
    return 0;
}
