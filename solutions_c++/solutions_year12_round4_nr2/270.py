#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

#define MAX_N 10005
#define X first
#define Y second

int r[1005], x[1005], y[1005];
bool used[1005];

int main()
{
    freopen("probB.in", "r", stdin);
    int T;
    cin >> T;
    for (int __ = 0; __ < T; ++__) {
        int n;
        int width;
        int height;

        cin >> n >> width >> height;

        vector< pair<int, int> > ss;
        for (int i = 0; i < n; ++i) {
            cin >> r[i];
            ss.push_back(make_pair(r[i], i));
        }
        sort(ss.begin(), ss.end(), greater< pair<int, int> >());
        memset(used, 0, sizeof(used));

        int bottom      = INT_MIN;
        int last_bottom = INT_MIN;
        int right       = INT_MIN;
        int total       = 0;
        while (total < n) {
            bool ok = false;
            for (int j = 0; j < n; ++j)
                if (!used[ss[j].Y] && right + r[ss[j].Y] <= width) {
                    int idx = ss[j].Y;
                    used[idx] = true;
                    x[idx] = max(0, right + r[idx]);
                    y[idx] = max(0, last_bottom + r[idx]);
                    // printf("%d %d %d %d %d\n", x[idx], y[idx], idx, right + r[ss[j].Y], width);
                    right = x[idx] + r[idx];
                    bottom = max(bottom, y[idx] + r[idx]);

                    ++total;
                    ok = true;
                }

            if (!ok) {
                last_bottom = bottom;
                right = INT_MIN;
            }
        }

        printf("Case #%d:", __+1);
        for (int i = 0; i < n; ++i)
            printf(" %d %d", x[i], y[i]);
        puts("");
    }
    return 0;
}

