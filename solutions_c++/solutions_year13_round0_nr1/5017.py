#include <iostream>

using namespace std;

inline
bool counts( char board, char player ) {
    return board == player || board == 'T';
}

int checkPlayer( char board[4][4], char player ) {
    int i, j, k;
    int len[4][4][4];

    for( j = 0; j < 4; j++ )
        len[0][j][1] = len[0][j][2] = len[0][j][3] = counts(board[0][j], player) ? 1 : 0;
    for( i = 1; i < 4; i++ ) {
        // diagonal to left
        len[i][0][1] = counts(board[i][0],player) ? 1 : 0;
        for( j = 1; j < 4; j++ )
            len[i][j][1] = counts(board[i][j], player) ? len[i-1][j-1][1] + 1 : 0;

        // vertical
        for( j = 0; j < 4; j++ )
            len[i][j][2] = counts(board[i][j], player ) ? len[i-1][j][2] + 1 : 0;

        // diagonal to right
        for( j = 0; j < 3; j++ )
            len[i][j][3] = counts(board[i][j], player) ? len[i-1][j+1][3] + 1 : 0;
        len[i][3][3] = counts(board[i][3], player ) ? 1 : 0;
    }

    for( i = 0; i < 4; i++ ) {
        len[i][0][0] = counts(board[i][0], player) ? 1 : 0;

        for( j = 1; j < 4; j++ )
            len[i][j][0] = counts(board[i][j], player) ? len[i][j-1][0] + 1 : 0;
    }

    int best = 0;
    for( i = 0; i < 4; i++ ) {
        for( j = 0; j < 4; j++ ) {
            //cout << board[i][j];
        }
//        cout << "   ";
        for( k = 0; k < 4; k++ ) {
            for( j = 0; j < 4; j++ ) {
   //             cout << len[i][j][k];
                best = max( best, len[i][j][k] );
            }
     //       cout << " ";
        }
       // cout << endl;
    }
//    cout << endl;

    return best;
}

int main() {
    int n, N, i, j, k;
    char board[4][4];

    cin >> N;

    for( n = 1; n <= N; n++ ) {
        for( i = 0; i < 4; i++ ) {
            for( j = 0; j < 4; j++ )
                cin >> board[i][j];
        }

        if( checkPlayer( board, 'X' ) == 4 ) {
            cout << "Case #" << n << ": X won\n";
        } else if( checkPlayer( board, 'O' ) == 4 ) {
            cout << "Case #" << n << ": O won\n";
        } else {
            k = 0;
            for( i = 0; i < 4 && !k; i++ ){
                for( j = 0; j < 4; j++ ) {
                    if( board[i][j] == '.' ) {
                        k = 1;
                        break;
                    }
                }
            }
            if( k ) {
                cout << "Case #" << n << ": Game has not completed\n";
            } else {
                cout << "Case #" << n << ": Draw\n";
            }

        }
    }

    return 0;
};
