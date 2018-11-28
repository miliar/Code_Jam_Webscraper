#include <stdio.h>
#include <string>

int T, t = 1;
int R, C;
char pic[52][52];

bool canCover(int r, int c)
{
    if(pic[r + 1][c] == '#' && pic[r][c + 1] == '#' && pic[r + 1][c + 1] == '#' && pic[r][c] == '#')
        return true;
    return false;
}

void cover(int r, int c)
{
    pic[r][c] = pic[r + 1][c + 1] = '/';
    pic[r + 1][c] = pic[r][c + 1] = '\\';
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(scanf("%d", &T); T; --T)
    {
        int i, j;
        bool possible = true;

        scanf("%d%d", &R, &C);
        memset(pic, 0, sizeof(pic));
        for(i = 0; i < R; ++i)
            scanf("%s", pic[i]);

        for(i = 0; i < R; ++i)
        {
            for(j = 0; j < C; ++j)
            {
                if(pic[i][j] == '#')
                {
                    if(canCover(i, j))
                    {
                        cover(i, j);
                    }else
                    {
                        possible = false;
                        break;
                    }
                }
            }
            if(j < C)
                break;
        }
        printf("Case #%d:\n", t++);            
        if(!possible)
            printf("Impossible\n");
        else 
        {
            for(i = 0; i < R; ++i)
                printf("%s\n", pic[i]);
        }
    }
}