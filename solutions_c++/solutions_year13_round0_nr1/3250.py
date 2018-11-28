#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int T;
char g[5][5];

int main()
{
    freopen("d.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    scanf("%d", &T);
    int icase = 1;
    while ( T-- ) {
        getchar();
        bool X = false, Y = false, D = true, C = false;
        for( int i = 0; i < 4; ++i, getchar() ) 
            for( int j = 0; j < 4; ++j ) {
                scanf("%c", &g[i][j]);
                if( g[i][j] == '.' ) C = true;
            }
        //判断每一行的情况下有没有赢家
        for( int i = 0; i < 4; ++i ) {
            X = Y = true;
            for( int j = 0; j < 4; ++j ) {
                if ( g[i][j] != 'X' && g[i][j] != 'T' ) X = false;
                if ( g[i][j] != 'O' && g[i][j] != 'T' ) Y = false;
                if ( !X && !Y ) break;
            }
            if ( X || Y ) break;
        }
        if ( !X && !Y ) {
        //判断两条对角线有没有赢家
            X = Y = true;
            for ( int i = 0; i < 4; ++i ) {
                if ( g[i][i] != 'X' && g[i][i] != 'T' ) X = false;
                if ( g[i][i] != 'O' && g[i][i] != 'T' ) Y = false;
                if ( !X && !Y ) break;
            }
        }
        if ( !X && !Y ) {
            X = Y = true;
            for ( int i = 0; i < 4; ++i ) {
                if ( g[i][3-i] != 'X' && g[i][3-i] != 'T' ) X = false;
                if ( g[i][3-i] != 'O' && g[i][3-i] != 'T' ) Y = false;
                if ( !X && !Y ) break;
            }
        }
        if ( !X && !Y ) {
        //判断每一列上有没有赢家
            for ( int j = 0; j < 4; ++j ) {
                X = Y = true;
                for ( int i = 0; i < 4; ++i ) {
                    if ( g[i][j] != 'X' && g[i][j] != 'T' ) X = false;
                    if ( g[i][j] != 'O' && g[i][j] != 'T' ) Y = false;
                    if ( !X && !Y ) break;
                }
                if ( X || Y ) break;
            }
        }
        printf("Case #%d: ", icase++);
        if ( X ) printf("X won\n");
        else if ( Y ) printf("O won\n");
        else if ( C ) printf("Game has not completed\n");
        else if ( D ) printf("Draw\n");
    }
}
