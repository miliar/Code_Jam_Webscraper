#include <cstdio>
using namespace std;

int N, K;

char board[64][64];

void adjust()
{
    for(int j = 0; j < N; j++)
    {
        for(int i = 0; i < N - 1; i++)
        {
            int alc = 0;
            for(int k = i; k < N; k++)
                alc += (board[k][j] != '.');


            if(!alc)
                break;


            if(board[i][j] == '.')
            {
                for(int k = i; k < N - 1; k++)
                    board[k][j] = board[k + 1][j];

                i--;

                board[N - 1][j] = '.';
            }


        }
    }
}

void print()
{
    for(int i = 0; i < N; i++, printf("\n"))
        for(int j = 0; j < N; j++)
            printf("%c", board[i][j]);
}
int check()
{
    int ret = 0;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            if(board[i][j] != '.')
                for(int dx = -1; dx <= 1; dx++)
                    for(int dy = -1; dy <= 1; dy++)
                        if(dx || dy)
                        {
                            int d = 1;
                            while(true)
                            {
                                int x = i + (d) * dx;
                                int y = j + (d) * dy;

                                if(0 <= x && x < N && 0 <= y && y < N && board[x][y] == board[i][j])
                                    d++;
                                else
                                    break;
                            }
                            
                            if(d >= K)
                                ret |= (1 << (board[i][j] == 'R'));
                        }

    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);

      
        scanf("%d%d", &N, &K);
        for(int j = N - 1; j >= 0; j--)
            for(int i = N - 1; i >= 0; i--)
                scanf(" %c", &board[i][j]);

        adjust();
        int ret = check();

        if(ret == 0)
            printf("Neither\n");
        else if(ret == 3)
            printf("Both\n");
        else if(ret == 2)
            printf("Red\n");
        else
            printf("Blue\n");
        

    }

    return 0;
}
