#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cmath>

using namespace std;

int move(int from, int to)
{
    return abs(to - from);
}

void solve()
{
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        int n;
        scanf("%d", &n);
        int pa = 1;
        int pb = 1;
        int ta = 0;
        int tb = 0;
        for (int i = 0; i < n; ++i) {
            char ch;
            int p;
            scanf(" %c%d", &ch, &p);
            if ('O' == ch) {
                ta += move(pa, p);
                ta = max(ta, tb) + 1;
                pa = p;
            } else {
                tb += move(pb, p);
                tb = max(ta, tb) + 1;
                pb = p;
            }
        }
        printf("Case #%d: %d\n", tci, max(ta, tb));
    }
}

int main()
{
    solve();
    return 0;
}
