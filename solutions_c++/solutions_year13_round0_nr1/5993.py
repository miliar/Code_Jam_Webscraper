#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

void status(string *board)
{
    int rows[4];
    int cols[4];

    int T[2] = {-1,-1};

    int dots = 0;

    memset(rows, 0, sizeof(rows)*4);
    memset(cols, 0, sizeof(cols)*4);

    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            if(board[i][j] == 'X')
            {
                rows[i]++;
                cols[j]++;

                if(rows[i] == 4 || cols[j] == 4 || (T[0] == i && T[1] == j))
                {
                    cout << "X won\n";
                    return;
                }
            }
            else if(board[i][j] == 'O')
            {
                rows[i]--;
                cols[j]--;

                if(rows[i] == 4 || cols[j] == 4 || (T[0] == i && T[1] == j))
                {
                    cout << "O won\n";
                    return;
                }
            }
            else if(board[i][j] == 'T')
            {
                T[0] = i;
                T[1] = j;
            }
            else
            {
                dots++;
            }
        }
    }

    if((board[0][0] == board[1][1] || board[0][0] == 'T' || board[1][1] == 'T') && 
        (board[1][1] == board[2][2] || board[1][1] == 'T' || board[2][2] == 'T') && 
            (board[2][2] == board[3][3] || board[2][2] == 'T' || board[3][3] == 'T'))
    {
        cout << board[0][0] << " won\n";
        return;
    }
    else if(board[0][3] == board[1][2] && board[1][2] == board[2][1] && board[2][1] == board[3][0])
    {
        cout << board[0][0] << " won\n";
        return;
    }

    if(dots)
    {
        cout << "Game has not completed\n";
        return;
    }

    cout << "Draw\n";
}

int main()
{
    int T;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        //vector<string> board;
        string board[4];

        cin >> board[0] >> board[1] >> board[2] >> board[3];

        status(board);
    }

    return 0;
}
