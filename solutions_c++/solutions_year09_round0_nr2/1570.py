#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX = 105, dr [] = {-1, 0, 0, 1}, dc [] = {0, -1, 1, 0};

int T, H, W, alt [MAX][MAX];
pair <int, int> flow [MAX][MAX];
bool seen [MAX][MAX];
char label [MAX][MAX];

inline bool valid (int r, int c)
{
    return r >= 0 && r < H && c >= 0 && c < W;
}

pair <int, int> solve (int r, int c)
{
    if (flow [r][c].first != -1)
        return flow [r][c];

    int bestr = -1, bestc = -1, least = 100;

    for (int d = 0; d < 4; d++)
    {
        int nr = r + dr [d], nc = c + dc [d];

        if (valid (nr, nc) && alt [nr][nc] < least)
        {
            bestr = nr;
            bestc = nc;
            least = alt [nr][nc];
        }
    }

    if (alt [r][c] <= least)
        return flow [r][c] = make_pair (r, c);
    else
        return flow [r][c] = solve (bestr, bestc);
}

int main ()
{
    scanf ("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        memset (seen, false, sizeof (seen));
        memset (flow, -1, sizeof (flow));
        scanf ("%d %d", &H, &W);

        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
                scanf ("%d", &alt [i][j]);

        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
                solve (i, j);

        char next = 'a';
        printf ("Case #%d:\n", t);

        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
            {
                if (!seen [flow [i][j].first][flow [i][j].second])
                {
                    seen [flow [i][j].first][flow [i][j].second] = true;
                    label [i][j] = label [flow [i][j].first][flow [i][j].second] = next++;
                }
                else
                    label [i][j] = label [flow [i][j].first][flow [i][j].second];

                printf ("%c%c", label [i][j], j < W - 1 ? ' ' : '\n');
            }
    }

    return 0;
}
