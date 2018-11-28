#include <cstdio>
#include <cstring>

using namespace std;

const int maxL = 64;

int R, C;
char maze[maxL][maxL];

bool isok(int x, int y)
{
    return x >= 0 && x < R && y >= 0 && y < C && maze[x][y] == '#';
}

int main()
{
    //freopen("A2.in", "r", stdin);
    //freopen("A2.out", "w", stdout);

    int cas;

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        scanf("%d %d", &R, &C);

        for(int i = 0; i < R; i++)
            scanf("%s", maze[i]);

        bool legal = true;
        for(int i = 0; i < R && legal; i++)
            for(int j = 0; j < C && legal; j++)
                if(maze[i][j] == '#')
                {
                    if(isok(i, j + 1) && isok(i + 1, j) && isok(i + 1, j + 1))
                    {
                        maze[i][j] = '/';
                        maze[i][j + 1] = '\\';
                        maze[i + 1][j] = '\\';
                        maze[i + 1][j + 1] = '/';
                    }
                    else legal = false;
                }

        printf("Case #%d:\n", cc + 1);
        if(!legal) printf("Impossible\n");
        else
        {
            for(int i = 0; i < R; i++)
                printf("%s\n", maze[i]);
        }
    }
    return 0;
}
