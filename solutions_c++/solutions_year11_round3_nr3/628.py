#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <list>
#include <cctype>

using namespace std;

void solve()
{
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        int N, L, H;
        scanf("%d%d%d", &N, &L, &H);
        vector<int> a;
        for (int i = 0; i < N; ++i) {
            int in;
            scanf("%d", &in);
            a.push_back(in);
        }
        printf("Case #%d: ", tci);
        bool ok = false;
        for (int i = L; i <= H; ++i) {
            ok = true;
            for each (int x in a) {
                if ((i % x) && (x % i)) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                printf("%d\n", i);
                break;
            }
        }
        if (!ok) {
            puts("NO");
        }
    }
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    solve();
    return 0;
}