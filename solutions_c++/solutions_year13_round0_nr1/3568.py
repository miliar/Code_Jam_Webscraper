#include<iostream>

using namespace std;

char board[4][5];

bool x_won()
{
    if( (board[0][0] == 'X' || board[0][0] == 'T') &&
        (board[0][1] == 'X' || board[0][1] == 'T') &&
        (board[0][2] == 'X' || board[0][2] == 'T') &&
        (board[0][3] == 'X' || board[0][3] == 'T')) return true;
    if( (board[1][0] == 'X' || board[1][0] == 'T') &&
        (board[1][1] == 'X' || board[1][1] == 'T') &&
        (board[1][2] == 'X' || board[1][2] == 'T') &&
        (board[1][3] == 'X' || board[1][3] == 'T')) return true;
    if( (board[2][0] == 'X' || board[2][0] == 'T') &&
        (board[2][1] == 'X' || board[2][1] == 'T') &&
        (board[2][2] == 'X' || board[2][2] == 'T') &&
        (board[2][3] == 'X' || board[2][3] == 'T')) return true;
    if( (board[3][0] == 'X' || board[3][0] == 'T') &&
        (board[3][1] == 'X' || board[3][1] == 'T') &&
        (board[3][2] == 'X' || board[3][2] == 'T') &&
        (board[3][3] == 'X' || board[3][3] == 'T')) return true;
    if( (board[0][0] == 'X' || board[0][0] == 'T') &&
        (board[1][0] == 'X' || board[1][0] == 'T') &&
        (board[2][0] == 'X' || board[2][0] == 'T') &&
        (board[3][0] == 'X' || board[3][0] == 'T')) return true;
    if( (board[0][1] == 'X' || board[0][1] == 'T') &&
        (board[1][1] == 'X' || board[1][1] == 'T') &&
        (board[2][1] == 'X' || board[2][1] == 'T') &&
        (board[3][1] == 'X' || board[3][1] == 'T')) return true;
    if( (board[0][2] == 'X' || board[0][2] == 'T') &&
        (board[1][2] == 'X' || board[1][2] == 'T') &&
        (board[2][2] == 'X' || board[2][2] == 'T') &&
        (board[3][2] == 'X' || board[3][2] == 'T')) return true;
    if( (board[0][3] == 'X' || board[0][3] == 'T') &&
        (board[1][3] == 'X' || board[1][3] == 'T') &&
        (board[2][3] == 'X' || board[2][3] == 'T') &&
        (board[3][3] == 'X' || board[3][3] == 'T')) return true;
    if( (board[0][0] == 'X' || board[0][0] == 'T') &&
        (board[1][1] == 'X' || board[1][1] == 'T') &&
        (board[2][2] == 'X' || board[2][2] == 'T') &&
        (board[3][3] == 'X' || board[3][3] == 'T')) return true;
    if( (board[0][3] == 'X' || board[0][3] == 'T') &&
        (board[1][2] == 'X' || board[1][2] == 'T') &&
        (board[2][1] == 'X' || board[2][1] == 'T') &&
        (board[3][0] == 'X' || board[3][0] == 'T')) return true;
    return false;
}

bool o_won()
{
    if( (board[0][0] == 'O' || board[0][0] == 'T') &&
        (board[0][1] == 'O' || board[0][1] == 'T') &&
        (board[0][2] == 'O' || board[0][2] == 'T') &&
        (board[0][3] == 'O' || board[0][3] == 'T')) return true;
    if( (board[1][0] == 'O' || board[1][0] == 'T') &&
        (board[1][1] == 'O' || board[1][1] == 'T') &&
        (board[1][2] == 'O' || board[1][2] == 'T') &&
        (board[1][3] == 'O' || board[1][3] == 'T')) return true;
    if( (board[2][0] == 'O' || board[2][0] == 'T') &&
        (board[2][1] == 'O' || board[2][1] == 'T') &&
        (board[2][2] == 'O' || board[2][2] == 'T') &&
        (board[2][3] == 'O' || board[2][3] == 'T')) return true;
    if( (board[3][0] == 'O' || board[3][0] == 'T') &&
        (board[3][1] == 'O' || board[3][1] == 'T') &&
        (board[3][2] == 'O' || board[3][2] == 'T') &&
        (board[3][3] == 'O' || board[3][3] == 'T')) return true;
    if( (board[0][0] == 'O' || board[0][0] == 'T') &&
        (board[1][0] == 'O' || board[1][0] == 'T') &&
        (board[2][0] == 'O' || board[2][0] == 'T') &&
        (board[3][0] == 'O' || board[3][0] == 'T')) return true;
    if( (board[0][1] == 'O' || board[0][1] == 'T') &&
        (board[1][1] == 'O' || board[1][1] == 'T') &&
        (board[2][1] == 'O' || board[2][1] == 'T') &&
        (board[3][1] == 'O' || board[3][1] == 'T')) return true;
    if( (board[0][2] == 'O' || board[0][2] == 'T') &&
        (board[1][2] == 'O' || board[1][2] == 'T') &&
        (board[2][2] == 'O' || board[2][2] == 'T') &&
        (board[3][2] == 'O' || board[3][2] == 'T')) return true;
    if( (board[0][3] == 'O' || board[0][3] == 'T') &&
        (board[1][3] == 'O' || board[1][3] == 'T') &&
        (board[2][3] == 'O' || board[2][3] == 'T') &&
        (board[3][3] == 'O' || board[3][3] == 'T')) return true;
    if( (board[0][0] == 'O' || board[0][0] == 'T') &&
        (board[1][1] == 'O' || board[1][1] == 'T') &&
        (board[2][2] == 'O' || board[2][2] == 'T') &&
        (board[3][3] == 'O' || board[3][3] == 'T')) return true;
    if( (board[0][3] == 'O' || board[0][3] == 'T') &&
        (board[1][2] == 'O' || board[1][2] == 'T') &&
        (board[2][1] == 'O' || board[2][1] == 'T') &&
        (board[3][0] == 'O' || board[3][0] == 'T')) return true;
    return false;
}

bool has_dot()
{
    for(int i = 0 ; i < 4 ; i++)
        for(int j = 0 ; j < 4 ; j++)
            if(board[i][j] == '.') return true;
    return false;
}

int main()
{
    int cas;
    cin >> cas;
    for(int i = 1 ; i <= cas ; i++)
    {
        cin >> board[0];
        cin >> board[1];
        cin >> board[2];
        cin >> board[3];
        cout << "Case #" << i << ": ";
        if(x_won()) cout << "X won\n";
        else if(o_won()) cout << "O won\n";
        else if(has_dot()) cout << "Game has not completed\n";
        else cout << "Draw\n";
    }
    return 0;
}
