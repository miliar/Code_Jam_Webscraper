#include <iostream>
using namespace std;
const int MAXH = 100, MAXW = 100;
int h, w, m[MAXH + 2][MAXW + 2];
char label, a[MAXH + 1][MAXW + 1], g[MAXH + 1][MAXW + 1][MAXH + 1][MAXW + 1];
bool used[MAXH + 1][MAXW + 1];
void dfs(int j, int k)
{
    int p1, p2;
    a[j][k] = label;
    used[j][k] = true;
    for(p1 = 1; p1 <= h; p1++)
        for(p2 = 1; p2 <= w; p2++)
            if(!used[p1][p2] && g[j][k][p1][p2] == 1)
                dfs(p1, p2);
}
int main()
{
    freopen("inout.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    const int MAX_ALTITUDE = 9999;
    int t, i, j, k, d1, d2, l, n;
    cin >> t;
    for(i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ":" << endl;
        label = 'a';
        cin >> h >> w;
        for(j = 1; j <= h; j++)
            for(k = 1; k <= w; k++)
                for(l = 1; l <= h; l++)
                    for(n = 1; n <= w; n++)
                        g[j][k][l][n] = 0;
        for(j = 1; j <= h; j++)
            for(k = 1; k <= w; k++)
                used[j][k] = false;
        for(j = 0; j < h + 2; j++)
        {
            m[j][0] = MAX_ALTITUDE + 1;
            m[j][w + 1] = MAX_ALTITUDE + 1;
        }
        for(j = 0; j < w + 2; j++)
        {
            m[0][j] = MAX_ALTITUDE + 1;
            m[h + 1][j] = MAX_ALTITUDE + 1;
        }
        for(j = 1; j <= h; j++)
            for(k = 1; k <= w; k++)
                cin >> m[j][k];
        for(j = 1; j <= h; j++)
            for(k = 1; k <= w; k++)
            {
                d1 = j;
                d2 = k;
                if(m[d1][d2] > m[j - 1][k])
                {
                    d1 = j - 1;
                    d2 = k;
                }
                if(m[d1][d2] > m[j][k - 1])
                {
                    d1 = j;
                    d2 = k - 1;
                }
                if(m[d1][d2] > m[j][k + 1])
                {
                    d1 = j;
                    d2 = k + 1;
                }
                if(m[d1][d2] > m[j + 1][k])
                {
                    d1 = j + 1;
                    d2 = k;
                }
                if(d1 != j || d2 != k)
                {
                    g[j][k][d1][d2] = 1;
                    g[d1][d2][j][k] = 1;
                }
            }
        for(j = 1; j <= h; j++)
            for(k = 1; k <= w; k++)
                if(!used[j][k])
                {
                    dfs(j, k);
                    label++;
                }
        for(j = 1; j <= h; j++)
        {
            for(k = 1; k <= w; k++)
                cout << a[j][k] << " ";
            cout << endl;
        }
    }
    return 0;
}
