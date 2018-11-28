#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <cassert>
using namespace std;

typedef long long LL;

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int n;
        LL a, b, c, d, x0, y0, m;
        cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;

        LL points[3][3];
        fill(points[0], points[0] + 9, 0);
        LL x = x0, y = y0;
        for (int i = 0; i < n; ++i) {
            ++points[x % 3][y % 3];
            x = (a * x + b) % m;
            y = (c * y + d) % m;
        }

        vector<pair<int, int> > vp;
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < 3; ++j)
                vp.push_back(make_pair(i, j));

        LL ans = 0;
        for (int i = 0; i < 9; ++i)
            for (int j = i + 1; j < 9; ++j)
                for (int k = j + 1; k < 9; ++k) {
                    int x1 = vp[i].first;
                    int y1 = vp[i].second;
                    int x2 = vp[j].first;
                    int y2 = vp[j].second;
                    int x3 = vp[k].first;
                    int y3 = vp[k].second;

                    int p = (x1 + x2 + x3) % 3;
                    int q = (y1 + y2 + y3) % 3;
                    if (p != 0 || q != 0) continue;
                    ans += points[x1][y1] * points[x2][y2] * points[x3][y3];
                }

        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j) {
                if (i == j) continue;

                int x1 = vp[i].first;
                int y1 = vp[i].second;
                int x2 = vp[j].first;
                int y2 = vp[j].second;

                int p = (x1 + x1 + x2) % 3;
                int q = (y1 + y1 + y2) % 3;
                if (p != 0 || q != 0) continue;

                LL p1 = points[x1][y1];
                LL p2 = points[x2][y2];
                if (p1 == 0) continue;
                ans += (p1 * (p1 - 1)) / 2 * p2;
            }

        for (int i = 0; i < 9; ++i) {
            int x1 = vp[i].first;
            int y1 = vp[i].second;

            LL p = points[x1][y1];
            if (p < 2) continue;
            ans += (p * (p - 1) * (p - 2)) / 6;
        }

        cout << "Case #" << cs + 1 << ": " << ans << '\n';
    }

    return 0;
}
