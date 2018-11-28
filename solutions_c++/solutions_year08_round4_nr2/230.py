
#include <cstdio>
#include <algorithm>
using namespace std;

int cross (int ax, int ay, int bx, int by, int cx, int cy)
{
    return ax * (by - cy) + bx * (cy - ay) + cx * (ay - by);
}
int main ()
{
    int C;
    scanf ("%d", &C);
    for (int t = 1; t <= C; ++t)
    {
        int n, m, a;
        scanf ("%d %d %d", &n, &m, &a);
        
        bool ok = false;
        int x3 = 0, y3 = 0;
        //for (int x3 = 0; x3 <= n; ++x3)
        //    for (int y3 = 0; y3 <= m; ++y3)
                for (int x1 = 0; x1 <= n; ++x1)
                    for (int y1 = 0; y1 <= m; ++y1)
                        for (int x2 = 0; x2 <= n; ++x2)
                            for (int y2 = 0; y2 <= m; ++y2)
                                if (abs (cross (x1, y1, x2, y2, x3, y3)) == a)
                                {
                                    ok = true;
                                    printf ("Case #%d: %d %d %d %d %d %d\n", t, x1, y1, x2, y2, x3, y3);
                                    goto ready;
                                }
        ready: ;
        if (!ok)
            printf ("Case #%d: IMPOSSIBLE\n", t);
    }
    return 0;
}