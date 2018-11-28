#include <cstdio>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum  <= T; testnum++)
    {
        int R, C;
        scanf("%d%d", &R, &C);

        char board[64][64] = {};

        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                scanf(" %c", &board[i][j]);

        bool flag = true;
        for(int i = 0; flag && i < R; i++)
            for(int j = 0; flag && j < C; j++)
                if(board[i][j] == '#')
                {
                    for(int a = 0; flag && a < 2; a++)
                        for(int b = 0; flag && b < 2; b++)
                            if(board[i + a][j + b] != '#')
                                flag = false;
                            else
                                board[i + a][j + b] = "/\\"[(a + b) % 2];
                }

        printf("Case #%d:\n", testnum);
        if(!flag)
            puts("Impossible");
        else
            for(int i = 0; i < R; i++, printf("\n"))
                for(int j = 0; j < C; j++)
                    printf("%c", board[i][j]);
    }
    return 0;
}
