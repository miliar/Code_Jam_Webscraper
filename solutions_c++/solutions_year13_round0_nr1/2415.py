#include <iostream>
#include <string>

using namespace std;

int main()
{
    int count;
    cin >> count;
    for (int c = 1; c <= count; ++c)
    {
        cout << "Case #" << c << ": ";

        string board[4];

        cin >> board[0];
        cin >> board[1];
        cin >> board[2];
        cin >> board[3];

        bool done = false;

        for (int i = 0; i < 3; ++i)
        {
            if (((board[i][0] == 'X' || board[i][0] == 'T') &&
                 (board[i][1] == 'X' || board[i][1] == 'T') &&
                 (board[i][2] == 'X' || board[i][2] == 'T') &&
                 (board[i][3] == 'X' || board[i][3] == 'T')) ||
                ((board[0][i] == 'X' || board[0][i] == 'T') &&
                 (board[1][i] == 'X' || board[1][i] == 'T') &&
                 (board[2][i] == 'X' || board[2][i] == 'T') &&
                 (board[3][i] == 'X' || board[3][i] == 'T')))
            {
                cout << "X won" << endl;
                done = true;
                break;
            }
            if (((board[i][0] == 'O' || board[i][0] == 'T') &&
                 (board[i][1] == 'O' || board[i][1] == 'T') &&
                 (board[i][2] == 'O' || board[i][2] == 'T') &&
                 (board[i][3] == 'O' || board[i][3] == 'T')) ||
                ((board[0][i] == 'O' || board[0][i] == 'T') &&
                 (board[1][i] == 'O' || board[1][i] == 'T') &&
                 (board[2][i] == 'O' || board[2][i] == 'T') &&
                 (board[3][i] == 'O' || board[3][i] == 'T')))
            {
                cout << "O won" << endl;
                done = true;
                break;
            }
        }

        if (((board[0][0] == 'X' || board[0][0] == 'T') &&
             (board[1][1] == 'X' || board[1][1] == 'T') &&
             (board[2][2] == 'X' || board[2][2] == 'T') &&
             (board[3][3] == 'X' || board[3][3] == 'T')) ||
            ((board[0][3] == 'X' || board[0][3] == 'T') &&
             (board[1][2] == 'X' || board[1][2] == 'T') &&
             (board[2][1] == 'X' || board[2][1] == 'T') &&
             (board[3][0] == 'X' || board[3][0] == 'T')))
        {
            cout << "X won" << endl;
            done = true;
        }

        if (((board[0][0] == 'O' || board[0][0] == 'T') &&
             (board[1][1] == 'O' || board[1][1] == 'T') &&
             (board[2][2] == 'O' || board[2][2] == 'T') &&
             (board[3][3] == 'O' || board[3][3] == 'T')) ||
            ((board[0][3] == 'O' || board[0][3] == 'T') &&
             (board[1][2] == 'O' || board[1][2] == 'T') &&
             (board[2][1] == 'O' || board[2][1] == 'T') &&
             (board[3][0] == 'O' || board[3][0] == 'T')))
        {
            cout << "O won" << endl;
            done = true;
        }

        if (done) continue;

        bool any = false;
        for (int i = 0; i < 3; ++i)
        {
            for (int j = 0; j < 3; ++j)
            {
                if (board[i][j] == '.')
                    any = true;
            }
        }

        if (!any)
        {
            cout << "Draw" << endl;
        }
        else
        {
            cout << "Game has not completed" << endl;
        }
    }

    return 0;
}

