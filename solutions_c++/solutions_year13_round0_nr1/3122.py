#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string JudgeGame( char board[4][4] ) {
    bool is_x_victory = false;
    bool is_o_victory = false;

    // Test for X win (rows)
    for ( int i = 0; i < 4; i++ ) {
        bool is_row_win = true;

        for ( int j = 0; j < 4; j++ ) {
            if ( board[i][j] == 'O' || board[i][j] == '.' )
                is_row_win = false;
        }

        if ( is_row_win )
            is_x_victory = true;
    }
               
    // Test for X win (cols)
    for ( int j = 0; j < 4; j++ ) {
        bool is_col_win = true;

        for ( int i = 0; i < 4; i++ ) {
            if ( board[i][j] == 'O' || board[i][j] == '.' )
                is_col_win = false;
        }
        
        if ( is_col_win )
            is_x_victory = true; 
    }

    // Test for X win (main diagonal)
    bool is_diag_win = true;
    if ( board[0][0] == 'O' || board[1][1] == 'O' || board[2][2] == 'O' || board[3][3] == 'O' || board[0][0] == '.' || board[1][1] == '.' || board[2][2] == '.' || board[3][3] == '.' )
        is_diag_win = false;

    if ( is_diag_win )
        is_x_victory = true;

    // Test for X win (sub-diagonal)
    is_diag_win = true;
    if ( board[0][3] == 'O' || board[1][2] == 'O' || board[2][1] == 'O' || board[3][0] == 'O' || board[0][3] == '.' || board[1][2] == '.' || board[2][1] == '.' || board[3][0] == '.' )

        is_diag_win = false;

    if ( is_diag_win )
        is_x_victory = true;

    // Test for O win (rows)
    for ( int i = 0; i < 4; i++ ) {
        bool is_row_win = true;

        for ( int j = 0; j < 4; j++ ) {
            if ( board[i][j] == 'X' || board[i][j] == '.' )
                is_row_win = false;
        }

        if ( is_row_win )
            is_o_victory = true;
    }
               
    // Test for O win (cols)
    for ( int j = 0; j < 4; j++ ) {
        bool is_col_win = true;

        for ( int i = 0; i < 4; i++ ) {
            if ( board[i][j] == 'X' || board[i][j] == '.' )
                is_col_win = false;
        }
        
        if ( is_col_win )
            is_o_victory = true; 
    }

    // Test for O win (main diagonal)
    is_diag_win = true;
    if ( board[0][0] == 'X' || board[1][1] == 'X' || board[2][2] == 'X' || board[3][3] == 'X' || board[0][0] == '.' || board[1][1] == '.' || board[2][2] == '.' || board[3][3] == '.' )
        is_diag_win = false;

    if ( is_diag_win )
        is_o_victory = true;

    // Test for O win (sub-diagonal)
    is_diag_win = true;
    if ( board[0][3] == 'X' || board[1][2] == 'X' || board[2][1] == 'X' || board[3][0] == 'X' || board[0][3] == '.' || board[1][2] == '.' || board[2][1] == '.' || board[3][0] == '.' )
        is_diag_win = false;

    if ( is_diag_win )
        is_o_victory = true;

    // Return winner (if there is one)
    if ( is_x_victory )
        return "X won";

    if ( is_o_victory )
        return "O won";

    // No winner, test for incomplete
    for ( int i = 0; i < 4; i++ )
        for ( int j = 0; j < 4; j++ )
            if ( board[i][j] == '.' )
                return "Game has not completed";

    // Hey, nobody won! If X didn't win, O didn't win and it's not incomplete then PIGEON HOLE PRINCIPLE
    return "Draw";
}

int main ( int argc, char* argv[] ) {
    fstream infile( "small.txt" );
    int num_cases;

    infile >> num_cases;
    for ( int i = 0; i < num_cases; i++ ) {
        char board[4][4];

        for ( int j = 0; j < 4; j++ ) {
            for ( int k = 0; k < 4; k++ ) {
                infile >> board[j][k];
            }
        }
        cout << "Case #" << ( i + 1 ) << ": " << JudgeGame( board ) << endl;
    }

    return 0;
}
