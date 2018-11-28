/*

This program can successfully run in BORLAND C++ BUILDER 6.
without file input/output in code.
you can run this program like this way(in WINDOWS command prompt):

p2.exe < inputfile.txt > outputfile.txt

And then take the outputfile.txt :)  

*/

#include <iostream>
using namespace std;

int T, H, W, Ti;
int map[110][110];
bool con[110][110][5];
bool vis[110][110];
int dx[5] = {0, -1, 0, 0, 1};
int dy[5] = {0, 0, -1, 1, 0};
char ans[110][110];
char ch;

void init()
{
    int i, j;

    for (i = 0; i < 110; i++)
        for (j = 0; j < 110; j++)
            map[i][j] = 20000;
    memset(con, 0, sizeof(con));
    memset(vis, 0, sizeof(vis));

    cin >> H >> W;
    for (i = 1; i <= H; i++)
        for (j = 1; j <= W; j++)
            cin >> map[i][j];
    
}

void dfs(int x, int y)
{
    int i;
    
    if (vis[x][y]) return;
    vis[x][y] = true;
    ans[x][y] = ch;
    for (i = 1; i <= 4; i++)
        if (con[x][y][i])
            dfs(x + dx[i], y + dy[i]);
}

void work()
{
    int i, j, k, x, y, a, b, min;

    for (i = 1; i <= H; i++)
        for (j = 1; j <= W; j++)
        {
            x = i;
            y = j;
            while (true)
            {
                if (vis[x][y]) break;
                vis[x][y] = true;
                min = 0;
                for (k = 1; k <= 4; k++)
                    if (map[x + dx[k]][y + dy[k]] < map[x + dx[min]][y + dy[min]])
                        min = k;
                            
                if (!min) break;
                con[x][y][min] = true;
                x += dx[min];
                y += dy[min];
                con[x][y][5 - min] = true;
            }
        }

    ch = 'a' - 1;
    memset(vis, 0, sizeof(vis));
    for (i = 1; i <= H; i++)
        for (j = 1; j <= W; j++)
            if (!vis[i][j])
            {
                ch++;
                dfs(i, j);
            }

    cout << "Case #" << Ti << ":" << endl;
    for (i = 1; i <= H; i++)
    {
        for (j = 1; j <= W; j++)
            cout << ans[i][j] << ' ';
        cout << endl;
    }
}

int main()
{
    cin >> T;
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }

  //  system("pause");
    return 0;
}
