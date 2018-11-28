
#include <cstdio>
#include <string>
using namespace std;

string testCase(char board[4][4])
{
    int count = 16;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            count -= (board[i][j] == '.') ? 1 : 0;
        }
    }

    for (int i = 0; i < 4; i++)
    {
        int count_x_a = 0,
            count_o_a = 0,
            count_x_b = 0,
            count_o_b = 0;

        for (int j = 0; j < 4; j++)
        {
            count_o_a += (board[i][j] == 'O' || board[i][j] == 'T') ? 1 : 0;
            count_x_a += (board[i][j] == 'X' || board[i][j] == 'T') ? 1 : 0;

            count_o_b += (board[j][i] == 'O' || board[j][i] == 'T') ? 1 : 0;
            count_x_b += (board[j][i] == 'X' || board[j][i] == 'T') ? 1 : 0;
        }

        bool
            o_won = count_o_a >= 4 || count_o_b >= 4,
            x_won = count_x_a >= 4 || count_x_b >= 4;

        if (o_won)
        {
            return "O won";
        }

        if (x_won)
        {
            return "X won";
        }
    }

    int count_o_p = 0,
        count_x_p = 0,
        count_o_n = 0,
        count_x_n = 0;

    for (int i = 0; i < 4; i++)
    {
        count_o_n += (board[i][i] == 'O' || board[i][i] == 'T') ? 1 : 0;
        count_x_n += (board[i][i] == 'X' || board[i][i] == 'T') ? 1 : 0;

        auto j = 4 - i - 1;
        count_o_p += (board[i][j] == 'O' || board[i][j] == 'T') ? 1 : 0;
        count_x_p += (board[i][j] == 'X' || board[i][j] == 'T') ? 1 : 0;
    }

    if (count_o_n >= 4 || count_o_p >= 4)
    {
        return "O won";
    }

    if (count_x_n >= 4 || count_x_p >= 4)
    {
        return "X won";
    }

    if (count >= 16)
    {
        return "Draw";
    }
    return "Game has not completed";
}

int main()
{
    FILE *file_in = fopen("input.txt", "rt"),
        *file_out = fopen("output.txt", "wt");

    int t;
    fscanf(file_in, "%d", &t);

    for (int current = 1; current <= t; current++)
    {
        char board[4][4];

        for (int i = 0; i < 4; i++)
        {
            char buffer[16];
            fscanf(file_in, "%s", buffer);

            for (int j = 0; j < 4; j++)
            {
                board[i][j] = buffer[j];
            }
        }

        auto result = testCase(board);
        fprintf(file_out, "Case  #%d: %s\n", current, result.c_str());
    }

    return 0;
}
