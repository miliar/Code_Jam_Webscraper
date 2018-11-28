#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;


bool find(const vector< vector<char> >& board, char c)
{
    // check rows
    for (int i = 0; i < 4; i++)
    {
        bool found = true;
        for (int j = 0; j < 4; j++)
            if (board[i][j] != c && board[i][j] != 'T')
                found = false;
        if (found)
            return true;
    }

    // check col's
    for (int i = 0; i < 4; i++)
    {
        bool found = true;
        for (int j = 0; j < 4; j++)
            if (board[j][i] != c && board[j][i] != 'T')
                found = false;
        if (found)
            return true;
    }

    // check diag 1
    bool found = true;
    for (int i = 0; i < 4; i++)
    {
        if (board[i][i] != c && board[i][i] != 'T')
            found = false;
    }
    if (found)
        return true;

    // check diag 2
    found = true;
    for (int i = 0; i < 4; i++)
    {
        if (board[3-i][i] != c && board[3-i][i] != 'T')
            found = false;
    }
    if (found)
        return true;

    return false;
}


bool hasDots(const vector< vector<char> >& board)
{
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (board[i][j] == '.')
                return true;
    return false;
}


void solve()
{
    vector< vector<char> > board(4, vector<char>(4, '.'));
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            cin >> board[i][j];

    if (find(board, 'X'))
        cout << "X won" << endl;
    else if (find(board, 'O'))
        cout << "O won" << endl;
    else if (hasDots(board))
        cout << "Game has not completed" << endl;
    else
        cout << "Draw" << endl;
}


int main()
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        cout << "Case #" << caseNum << ": ";
        solve();
    }

    return 0;
}
