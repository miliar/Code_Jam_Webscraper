#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main()
{
    int tst;
    cin >> tst;
    for(int iter = 0; iter < tst; ++iter) {
        int n, w, h;
        cin >> n >> w >> h;
        vector<pair<int, int> > r(n);
        for(int i = 0; i < n; ++i) {
            cin >> r[i].first;
            r[i].second = i;
        }
        sort(r.begin(), r.end());
        reverse(r.begin(), r.end());
        vector<pair<int, int> > ans(n);
        int x = 0;
        bool firstX = true;
        for(int i = 0; i < n;) {
            int d = 0;
            int sr = r[i].first;
            if (!firstX) x += sr;
            int y = 0;
            bool firstY = true;
            while (i < n && y <= h) {
                int cr = r[i].first;
                if (!firstY) y += cr;
                if (y > h) break;
                ans[r[i].second] = make_pair(x, y);
                y += cr;
                firstY = false;
                ++i;
            }
            firstX = false;
            x += sr;
        }
        printf("Case #%d:", iter + 1);
        for(int i = 0; i < n; ++i) printf(" %d %d", ans[i].first, ans[i].second);
        printf("\n");
    }
    return 0;
}
