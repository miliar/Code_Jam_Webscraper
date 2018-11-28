
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX = 32768;
const int INF = 1 << 20;

int g [MAX];
int c [MAX];
int leaf [MAX];
bool isleaf [MAX];
int best [MAX][2];

int main ()
{
    int tests;
    scanf ("%d", &tests);
    for (int t = 1; t <= tests; ++t)
    {
        memset (best, 0x3f, sizeof (best));
        int m, v;
        scanf ("%d %d", &m, &v);
        for (int i = 1; i <= (m - 1) / 2; ++i)
            scanf ("%d %d", &g [i], &c [i]);
        for (int i = (m - 1) / 2 + 1; i <= m; ++i)
        {
            scanf ("%d", &leaf [i]);
            best [i][leaf [i]] = 0;
            isleaf [i] = true;
        }
        
        for (int j = (m - 1) / 2; j >= 1; --j)
        {
            int a = 2 * j;
            int b = 2 * j + 1;
            
            for (int k1 = 0; k1 < 2; ++k1)
                for (int k2 = 0; k2 < 2; ++k2)
                {
                    if (best [a][k1] > INF) continue;
                    if (best [b][k2] > INF) continue;
                    
                    if (g [j] == 0)
                    {
                        best [j][k1 | k2] = min (best [j][k1 | k2], best [a][k1] + best [b][k2]);
                        if (c [j])
                            best [j][k1 & k2] = min (best [j][k1 & k2], best [a][k1] + best [b][k2] + 1);
                    }
                    else
                    {
                        best [j][k1 & k2] = min (best [j][k1 & k2], best [a][k1] + best [b][k2]);
                        if (c [j])
                            best [j][k1 | k2] = min (best [j][k1 | k2], best [a][k1] + best [b][k2] + 1);
                    }
                }
        }
        
        int ans = best [1][v];
        printf ("Case #%d: ", t);
        if (ans > INF)
            printf ("IMPOSSIBLE\n");
        else
            printf ("%d\n", ans);
    }
    return 0;
}
