#include <cstdio>
#include <cstring>

const char* winstr[] = 
    { "Neither", "Red", "Blue", "Both", };
    
const int RED = 1;
const int BLU = 2;

int main()
{
    int cases; fscanf(stdin, "%d", &cases);
    for (int i = 1; i <= cases; ++i)
    {
        int n, k; fscanf(stdin, "%d %d", &n, &k);
        char board[n][n], line[n + 1];
        
        for (int row = 0; row < n; ++row)
        {
            fscanf(stdin, "%s", line);
            strncpy(board[row], line, n);
        };
        
        for (int row =     0; row <  n; ++row)
        for (int col = n - 1; col >= 0; --col)
        {
            int z;
            if (board[row][col] == '.')
            {
                for (z = col - 1; z >= 0; --z) if (board[row][z] != '.')
                { board[row][col] = board[row][z]; board[row][z] = '.'; break; };
            };
        };
        
        int winner = 0;
        
        // search rows
        for (int row = 0; row < n; ++row) for (int col = 0; col <= n - k; ++col)
            if (board[row][col] != '.')
        {
            int z; for (z = 0; z < k && board[row][col + z] == board[row][col]; ++z);
            if (z == k) winner |= (board[row][col] == 'R') ? RED : BLU;
        }
        
        // search cols
        for (int row = 0; row <= n - k; ++row) for (int col = 0; col < n; ++col)
            if (board[row][col] != '.')
        {
            int z; for (z = 0; z < k && board[row + z][col] == board[row][col]; ++z);
            if (z == k) winner |= (board[row][col] == 'R') ? RED : BLU;
        }
        
        // search maj diags
        for (int row = 0; row <= n - k; ++row) for (int col = 0; col <= n - k; ++col)
            if (board[row][col] != '.')
        {
            int z; for (z = 0; z < k && board[row + z][col + z] == board[row][col]; ++z);
            if (z == k) winner |= (board[row][col] == 'R') ? RED : BLU;
        }
        
        // search min diags
        for (int row = 0; row <= n - k; ++row) for (int col = k - 1; col < n; ++col)
            if (board[row][col] != '.')
        {
            int z; for (z = 0; z < k && board[row + z][col - z] == board[row][col]; ++z);
            if (z == k) winner |= (board[row][col] == 'R') ? RED : BLU;
        }
        
        fprintf(stdout, "Case #%d: %s\n", i, winstr[winner]);
//        for (int row = 0; row < n; ++row)
//        {
//            strncpy(line, board[row], n);
//            fprintf(stdout, "%s\n", line);
//        };
//        fprintf(stdout, "\n");
    };
}

