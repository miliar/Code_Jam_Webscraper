#include <iostream>

using namespace std;

int h, w;

int  map[105][105];
char res[105][105];

/*
 *        (0, 1)
 * (1, 0) (1, 1) (1, 2)
 *        (2, 1)
 */

int  dir[4][2] = {
    {-1,  0}, // North
    { 0, -1}, // West
    { 0,  1}, // East
    { 1,  0}  // South
};

char start;

void search(int r, int c, char * flag)
{
    int best_dir = 4;
    int alt = map[r][c];

    // find a direction
    for (int i = 0; i < 4; i++)
    {
        int r2 = r+dir[i][0];
        int c2 = c+dir[i][1];

        if (r2 >= 0 && r2 < h && 
            c2 >= 0 && c2 < w && 
            map[r2][c2] < alt)
        {
            alt = map[r2][c2];
            best_dir = i;
        }
    }

    if (best_dir < 4)
    {
        // continue search
        int r2 = r+dir[best_dir][0];
        int c2 = c+dir[best_dir][1];

        if (res[r2][c2] != '0')
        {
            *flag = res[r2][c2];
        }
        else
        {
            search(r2, c2, flag);
        }
    }
    else
    {
        // find sink
        *flag = start++;
    }
    res[r][c] = *flag;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int caseNo, i, r, c;

    scanf("%d", &caseNo);

    for (i = 1; i <= caseNo; i++)
    {
        scanf("%d %d", &h, &w);
        for (r = 0; r < h; r++)
        {
            for (c = 0; c < w; c++)
            {
                scanf("%d", &map[r][c]);
                res[r][c] = '0';
            }
        }
        
        start = 'a';

        for (r = 0; r < h; r++)
        {
            for (c = 0; c < w; c++)
            {
                char temp;
                if (res[r][c] == '0')
                    search(r, c, &temp);
            }
        }

        // output res.
        printf("Case #%d:\n", i);

        for (r = 0; r < h; r++)
        {
            printf("%c", res[r][0]);
            for (c = 1; c < w; c++)
            {
                printf(" %c", res[r][c]);
            }
            putchar('\n');
        }

    }

    return 0;
}
