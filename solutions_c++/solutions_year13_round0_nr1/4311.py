#include<cstdio>

char ns[10][10];
int  ni[10][10];

bool checkWin( char ch ) {

    int nsum, nsum2;
    for( int i=0; i<4; i++ ) {
        nsum = nsum2 = 0;
        for( int k=0; k<4; k++ ) nsum += ni[i][k], nsum2 += ni[k][i];
        if ( nsum == 4 * 100 || nsum == 3 * 100 + 1000000 || nsum2 == 4 * 100 || nsum2 == 3 * 100 + 1000000 ) return ch == 'X';
        if ( nsum == 4 * 10000 || nsum == 3 * 10000 + 1000000 || nsum2 == 4 * 10000 || nsum2 == 3 * 10000 + 1000000 ) return ch == 'O';
    }
    nsum = nsum2 = 0;
    nsum  = ni[0][0] + ni[1][1] + ni[2][2] + ni[3][3];
    nsum2 = ni[0][3] + ni[1][2] + ni[2][1] + ni[3][0];
    if ( nsum == 4 * 100 || nsum == 3 * 100 + 1000000 || nsum2 == 4 * 100 || nsum2 == 3 * 100 + 1000000 ) return ch == 'X';
    if ( nsum == 4 * 10000 || nsum == 3 * 10000 + 1000000 || nsum2 == 4 * 10000 || nsum2 == 3 * 10000 + 1000000 ) return ch == 'O';
    return false;
}

int main() {

    int ntc;
    scanf("%d", &ntc);
    for( int TC=1; TC<=ntc; TC++ ) {
        bool isContainZero = false;
        for( int i=0; i<4; i++ ) {
            scanf("%s", ns[i]);
            for( int k=0; k<4; k++ ) {
                if ( ns[i][k] == 'X' ) ni[i][k] = 100;
                else if ( ns[i][k] == 'O' ) ni[i][k] = 10000;
                else if ( ns[i][k] == 'T' ) ni[i][k] = 1000000;
                else {
                    ni[i][k] = 0;
                    isContainZero = true;
                }
            }
        }

        bool isXWin = checkWin( 'X' );
        bool isOWin = checkWin( 'O' );
        
        printf("Case #%d: ", TC);
        if ( !isXWin && isOWin ) {
            printf("O won\n");
        } else if ( isXWin && !isOWin ) {
            printf("X won\n");
        } else {
            if ( isContainZero ) printf("Game has not completed\n");
            else printf("Draw\n");
        }

    }
    return 0;
}
