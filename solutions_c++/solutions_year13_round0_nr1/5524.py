#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int Case, cnt, xrnum, xcnum, ornum, ocnum, tmp, flag, cmt;
char ch[7][7];

int main ( ) {
    freopen ( "A-small-attempt2.in", "r", stdin );
    freopen ( "output.txt", "w", stdout );
    scanf ( "%d", &Case );
    for ( cnt = 1; cnt <= Case; ++cnt ) {
        for ( int i = 0; i < 4; ++i ) {
            scanf ( "%s", ch[i] );
            getchar ( );
        }
        scanf ( "\n" );

        tmp = flag = 0;
        for ( int i = 0; i < 4; ++i ) {
            xrnum = xcnum = ornum = ocnum = 0;
            for ( int j = 0; j < 4; ++j ) {
                if ( ch[i][j] == 'X' || ch[i][j] == 'T' ) xrnum++;
                if ( ch[i][j] == 'O' || ch[i][j] == 'T' ) ornum++;
                if ( ch[j][i] == 'X' || ch[j][i] == 'T' ) xcnum++;
                if ( ch[j][i] == 'O' || ch[j][i] == 'T' ) ocnum++;
                if ( ch[i][j] != '.' || ch[j][i] != '.' ) tmp++;
            }
            if ( xrnum == 4 || xcnum == 4 ) {
                flag = 1;
                break;
            }
            if ( ornum == 4 || ocnum == 4 ) {
                flag = 2;
                break;
            }
        }
        if ( ( ch[0][0] ==  'X' || ch[0][0] == 'T' ) && ( ch[1][1] ==  'X' || ch[1][1] == 'T' ) && ( ch[2][2] ==  'X' || ch[2][2] == 'T' ) && ( ch[3][3] ==  'X' || ch[3][3] == 'T' ) ) flag = 1;
        if ( ( ch[0][3] ==  'X' || ch[0][3] == 'T' ) && ( ch[1][2] ==  'X' || ch[1][2] == 'T' ) && ( ch[2][1] ==  'X' || ch[2][1] == 'T' ) && ( ch[3][0] ==  'X' || ch[3][0] == 'T' ) ) flag = 1;
        if ( ( ch[0][3] ==  'O' || ch[0][3] == 'T' ) && ( ch[1][2] ==  'O' || ch[1][2] == 'T' ) && ( ch[2][1] ==  'O' || ch[2][1] == 'T' ) && ( ch[3][0] ==  'O' || ch[3][0] == 'T' ) ) flag = 2;
        if ( ( ch[0][0] ==  'O' || ch[0][0] == 'T' ) && ( ch[1][1] ==  'O' || ch[1][1] == 'T' ) && ( ch[2][2] ==  'O' || ch[2][2] == 'T' ) && ( ch[3][3] ==  'O' || ch[3][3] == 'T' ) ) flag = 2;

        printf ( "Case #%d: ", cnt );

        if ( flag == 1 ) printf ( "X won\n" );
        else if ( flag == 2 ) printf ( "O won\n" );
        else if ( tmp == 16 ) printf ( "Draw\n" );
        else printf ( "Game has not completed\n" );
    }
    return 0;
}
