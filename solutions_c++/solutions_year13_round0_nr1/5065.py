#include <cstdio>
#include <cstdlib>

int T;
int win;
bool chk;
bool space;
char in[4][5];

int main(){
    int i, j;
    int k = 0;

    freopen( "A-large.in", "r", stdin);
    freopen( "out.txt", "w", stdout);

    scanf("%d", &T);
    while( k++ < T){
        win = 0;
        space = 0;
        chk = 0;

        for( i = 0; i < 4; i++){
            scanf("%s", in[i]);
            for( j = 0; j < 4; j++)
                if( in[i][j] == '.')space = 1;
        }

        for( i = 0; i < 4 && !win; i++){
            chk = 0;
            for( j = 0; j < 4; j++){
                if( in[i][j] != 'O' && in[i][j] != 'T')chk = 1;
            }
            if( !chk)win = 1;

            chk = 0;
            for( j = 0; j < 4; j++){
                if( in[i][j] != 'X' && in[i][j] != 'T')chk = 1;
            }
            if( !chk)win = 2;
        }

        for( i = 0; i < 4 && !win; i++){
            chk = 0;
            for( j = 0; j < 4; j++){
                if( in[j][i] != 'O' && in[j][i] != 'T')chk = 1;
            }
            if( !chk)win = 1;

            chk = 0;
            for( j = 0; j < 4; j++){
                if( in[j][i] != 'X' && in[j][i] != 'T')chk = 1;
            }
            if( !chk)win = 2;


        }

        chk = 0;
        for( i = 0; i < 4; i++)
            if( in[i][i] != 'O' && in[i][i] != 'T')chk = 1;
        if( !chk)win = 1;

        chk = 0;
        for( i = 0; i < 4; i++)
            if( in[i][i] != 'X' && in[i][i] != 'T')chk = 1;
        if( !chk)win = 2;

        chk = 0;
        for( i = 0; i < 4; i++)
            if( in[i][3 - i] != 'O' && in[i][3 - i] != 'T')chk = 1;
        if( !chk)win = 1;

        chk = 0;
        for( i = 0; i < 4; i++)
            if( in[i][3 - i] != 'X' && in[i][3 - i] != 'T')chk = 1;
        if( !chk)win = 2;

        printf("Case #%d: ", k);

        if( win == 0 && space == 0)printf("Draw\n");
        else if( win == 0 && space == 1)printf("Game has not completed\n");
        else if( win == 1)printf("O won\n");
        else printf("X won\n");
    }
}
