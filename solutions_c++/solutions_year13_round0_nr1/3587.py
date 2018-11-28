// google code jam 2013 Qualification Round
// problem A

#include <iostream>
#include <cstdio>
using namespace std;

const int SIZE = 4;

char board[SIZE << 1][SIZE << 1];
int test_t, res; //  res: -1-not over 0-draw 1-X 2-O
int flag = 0, cnt = 0, pos;
bool dot = false;
FILE *fin, *fout;

int main()
{
    fin = fopen("A.in", "r");
    fout = fopen("A.out", "w");
    fscanf(fin, "%d", &test_t);
    for (int testcase = 1; testcase <= test_t; testcase++)
    {
        dot = false;
        res = -1;
        for (int i = 0; i < SIZE; i++)
            fscanf(fin, "%s", board[i]);
        // row
        for (int i = 0; res < 0 && i < SIZE; i++)
        {
            flag = 0, cnt = 0;
            for (; flag < SIZE; flag++)
                if (board[i][flag] == 'X' || board[i][flag] == 'O')
                    break;
            if (flag == SIZE)
                continue;
            for (int j = 0; j < SIZE; j++)
                if (board[i][j] != board[i][flag])
                    cnt++, pos = j;
            if (cnt > 1 || (cnt == 1 && board[i][pos] != 'T'))
                continue;
            res = (board[i][flag] == 'X' ? 1 : 2);
        }
        // column
        for (int i = 0; res < 0 && i < SIZE; i++)
        {
            flag = 0, cnt = 0;
            for (; flag < SIZE; flag++)
                if (board[flag][i] == 'X' || board[flag][i] == 'O')
                    break;
            if (flag == SIZE)
                continue;
            for (int j = 0; j < SIZE; j++)
                if (board[j][i] != board[flag][i])
                    cnt++, pos = j;
            if (cnt > 1 || (cnt == 1 && board[pos][i] != 'T'))
                continue;
            res = (board[flag][i] == 'X' ? 1 : 2);
        }
        // left diagonal
        flag = 0, cnt = 0;
        for (; flag < SIZE; flag++)
            if (board[flag][flag] == 'X' || board[flag][flag] == 'O')
                break;
        if (flag < SIZE)
        {
            for (int i = 0; i < SIZE; i++)
                if (board[i][i] != board[flag][flag])
                    cnt++, pos = i;
            if (cnt == 0 || (cnt == 1 && board[pos][pos] == 'T'))
                res = (board[flag][flag] == 'X' ? 1 : 2);
        }
        // right diagonal
        flag = 0, cnt = 0;
        for (; flag < SIZE; flag++)
            if (board[flag][3 - flag] == 'X' || board[flag][3 - flag] == 'O')
                break;
        if (flag < SIZE)
        {
            for (int i = 0; i < SIZE; i++)
                if (board[i][3 - i] != board[flag][3 - flag])
                    cnt++, pos = i;
            if (cnt == 0 || (cnt == 1 && board[pos][3 - pos] == 'T'))
                res = (board[flag][3 - flag] == 'X' ? 1 : 2);
        }
        // judge
        for (int i = 0; i < SIZE; i++)
            for (int j = 0; j < SIZE; j++)
                if (board[i][j] == '.')
                    dot = true;
        if (res < 0)
            res = (dot ? -1 : 0);
        // output    res: -1-not over 0-draw 1-X 2-O
        if (res < 0)
            fprintf(fout, "Case #%d: Game has not completed\n", testcase);
        else if (res == 0)
            fprintf(fout, "Case #%d: Draw\n", testcase);
        else if (res == 1)
            fprintf(fout, "Case #%d: X won\n", testcase);
        else if (res == 2)
            fprintf(fout, "Case #%d: O won\n", testcase);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
