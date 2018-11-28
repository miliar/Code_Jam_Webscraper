#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

void solve()
{
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        int n;
        scanf("%d", &n);
        int b = 0;
        vector<int> c;
        for (int i = 0; i < n; ++i) {
            int in;
            scanf("%d", &in);
            b ^= in;
            c.push_back(in);
        }
        if (b) {
            printf("Case #%d: NO\n", tci);
        } else {
            sort(c.begin(), c.end());
            printf("Case #%d: %d\n", tci, accumulate(c.begin() + 1, c.end(), 0));
        }
    }
}

int main()
{
    solve();
    return 0;
}

