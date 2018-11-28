#include <iostream>
#include <cstdio>
using namespace std;

int N;
char board[17];

char check_row_or_col(int n, int diff)
{
    //    cerr << "(" << n << ", " << diff << ") ";
    char check = board[n];
    if (check == 'X' || check == 'O')
    {
        if (check == board[n + 1*diff] || board[n + 1*diff] == 'T')
            if (check == board[n + 2*diff] || board[n + 2*diff] == 'T')
                if (check == board[n + 3*diff] || board[n + 3*diff] == 'T')
                    return check;
    }
    else if (check == 'T')
    {
        check = board[n + 1*diff];
        if (check != '.')
        {
            if (check == board[n + 2*diff])
                if (check == board[n + 3*diff])
                    return check;
        }
    }
    return '\0';
}

int main()
{
    int i, j, k, n;
    char c;
    cin >> N;
    for (n = 1; n <= N; n++)
    {
        getchar();
        for (i = 0, k = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
                board[k++] = getchar();
            getchar();
        }
        for (i = 0; i < 4; i++)
            if ((c = check_row_or_col(i, 4)) != '\0') break;
        if (c == '\0')
            for (i = 0; i < 4; i++)
                if ((c = check_row_or_col(i * 4, 1)) != '\0') break;
        if (c == '\0') c = check_row_or_col(0, 5);
        if (c == '\0') c = check_row_or_col(3, 3);
        if (c == '\0')
        {
            for (i = 0; i < 16; i++)
                if (board[i] == '.') { c = '.'; break; }
        }

        cout << "Case #" << n << ": ";
        if (c == 'O' || c == 'X') cout << c << " won";
        else if (c == '\0') cout << "Draw";
        else cout << "Game has not completed";
        cout << endl;
    }
}
