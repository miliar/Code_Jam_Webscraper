#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int dx[8] = {1, -1, 1, -1, 1, -1, 0, 0};
int dy[8] = {1, -1, -1, 1, 0, 0, 1, -1};
int table[110][110];
int value[110][110];
int occup[110][110];
int ans;
int r, c;

void doit(int x, int y)
{
    if (x == r)
    {
        int i, j;
        for (i = 0; i < r; i++)
        {
            for (j = 0; j < c; j++)
            {
                occup[i][j] = 0;
            }
        }
        for (i = 0; i < r; i++)
        {
            for (j = 0; j < c; j++)
            {
                int nextx = (i + dx[value[i][j]] + r) % r;
                int nexty = (j + dy[value[i][j]] + c) % c;
                if (occup[nextx][nexty] != 0)
                    return;
                occup[nextx][nexty] = 1;
            }
        }
        ans++;
    }
    else
    {
        int nextx = x;
        int nexty = y + 1;
        if (nexty == c)
        {
            nextx++;
            nexty = 0;
        }
        value[x][y] = 2 * table[x][y];
        doit(nextx, nexty);
        value[x][y] = 2 * table[x][y] + 1;
        doit(nextx, nexty);
    }
}

int main()
{
    int teste, t;
    scanf("%d", &teste);

    for (t=0; t<teste; t++)
    {
        scanf("%d %d", &r, &c);
        int i, j;
        for (i = 0; i < r; i++)
        {
            char buffer[110];
            scanf("%s", buffer);
            for (j = 0; j < c; j++)
            {
                switch(buffer[j])
                {
                    case '|': table[i][j] = 2; break;
                    case '\\': table[i][j] = 0; break;
                    case '/': table[i][j] = 1; break;
                    case '-': table[i][j] = 3; break;
                }
            }
        }

        ans = 0;
        doit(0, 0);

        printf("Case #%d: %d\n", t+1, ans);
    }
    return 0;
}
