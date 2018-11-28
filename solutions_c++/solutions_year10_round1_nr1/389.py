#include <stdio.h>
#include <vector>
#include <string.h>

using namespace std;

bool lookup(char board[50][50], char symbol, int K, int N)
{
    // Line lookup
    for (int i = 0; i < N; ++i)
    {
        int count = 0;

        for (int j = 0; j < N; ++j)
        {
            if (board[i][j] == symbol)
            {
                ++count;
                if (count == K) return true;
            }
            else
            {
                count = 0;
            }
        }
    }

    // Column lookup
    for (int j = 0; j < N; ++j)
    {
        int count = 0;

        for (int i = 0; i < N; ++i)
        {
            if (board[i][j] == symbol)
            {
                ++count;
                if (count == K) return true;
            }
            else
            {
                count = 0;
            }
        }
    }

    // Diagonal (3-->1) lookup
    for (int i = 0; i < N; ++i)
    {
        int count = 0;

        for (int j = 0; j <= i; ++j)
        {
            if (board[i - j][j] == symbol)
            {
                ++count;
                if (count == K) return true;
            }
            else
            {
                count = 0;
            }
        }
    }

    for (int j = 0; j < N; ++j)
    {
        int count = 0;

        for (int i = N - 1; i >= j; --i)
        {
            if (board[i][j + (N - 1 - i)] == symbol)
            {
                ++count;
                if (count == K) return true;
            }
            else
            {
                count = 0;
            }
        }
    }

    // Diagonal (4-->2) lookup
    for (int i = 0; i < N; ++i)
    {
        int count = 0;

        for (int j = 0; j <= N - i - 1; ++j)
        {
            if (board[i + j][j] == symbol)
            {
                ++count;
                if (count == K) return true;
            }
            else
            {
                count = 0;
            }
        }
    }

    for (int j = 0; j < N; ++j)
    {
        int count = 0;

        for (int i = 0; i <= N - j - 1; ++i)
        {
            if (board[i][i + j] == symbol)
            {
                ++count;
                if (count == K) return true;
            }
            else
            {
                count = 0;
            }
        }
    }

    return false;
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t)
    {
        int N, K;
        scanf("%d %d", &N, &K);

        char board[51][51];

        for (int i = 0; i < N; ++i)
        {
            scanf("%s", board[i]);
        }

        #ifdef DEBUG
        for (int i = 0; i < N; ++i)
        {
            char buffer[51];
            strncpy(buffer, board[i], N);
            buffer[N] = '\0';
            puts(buffer);
        }
        puts("");
        #endif

        char rotatedBoard[50][50];
        vector<char> rotatedBoardRows[50];

        // O(N**2)
        for (int j = 0; j < N; ++j)
        {
            for (int i = 0; i < N; ++i)
            {
                char symbol = board[N-j-1][i];
                if (symbol == 'R' || symbol == 'B')
                {
                    rotatedBoardRows[j].push_back(symbol);
                }
            }
        }

        // Gravity
        for (int j = 0; j < N; ++j)
        {
            int blankCount = N - rotatedBoardRows[j].size();

            for (int blank = 0; blank < blankCount; ++blank)
            {
                rotatedBoard[blank][j] = '.';
            }

            for (int i = blankCount; i < N; ++i)
            {
                rotatedBoard[i][j] = rotatedBoardRows[j][i - blankCount];
            }
        }

        // Debug
        #ifdef DEBUG
        for (int i = 0; i < N; ++i)
        {
            char buffer[51];
            strncpy(buffer, rotatedBoard[i], N);
            buffer[N] = '\0';
            puts(buffer);
        }
        #endif


        // Lookup
        bool redSuccessful = lookup(rotatedBoard, 'R', K, N);
        bool blueSuccessful = lookup(rotatedBoard, 'B', K, N);

        if (!redSuccessful && !blueSuccessful)
        {
            printf("Case #%d: Neither\n", t);
        }
        else if (redSuccessful && !blueSuccessful)
        {
            printf("Case #%d: Red\n", t);
        }
        else if (!redSuccessful && blueSuccessful)
        {
            printf("Case #%d: Blue\n", t);
        }
        else if (redSuccessful && blueSuccessful)
        {
            printf("Case #%d: Both\n", t);
        }
    }
}
