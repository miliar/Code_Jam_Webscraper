#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main()
{
    int tst;
    cin >> tst;
    for(int iter = 0; iter < tst; ++iter) {
        int n;
        cin >> n;
        vector<int> d(n), l(n);
        for(int i = 0; i < n; ++i) {
            cin >> d[i] >> l[i];
        }
        int D;
        cin >> D;
        d.push_back(D);
        l.push_back(0);
        printf("Case #%d: ", iter + 1);
        int INF = 2 * D;
        vector<int> ans(n + 1, INF); 
        ans[0] = 0;
        //maxpos, start_pos
        deque<pair<int, int> > queue;
        for(int pos = 0; pos <= n; ++pos) {
            while (!queue.empty() && queue.front().first < d[pos]) queue.pop_front();
            if (ans[pos] == INF && queue.empty()) {
                continue;
            }
            if (!queue.empty()) {
                ans[pos] = max(queue.front().second, d[pos] - l[pos]);
            }
            //std::cerr << ans[pos] << " ";
            pair<int, int> newAdd(d[pos] + d[pos] - ans[pos], d[pos]);
            if (queue.empty()) {
                queue.push_back(newAdd);
                continue;
            }
            if (queue.back().first < newAdd.first) {
                queue.push_back(newAdd);
            }
        }
        //cerr << endl;
        printf("%s\n", ans[n] == INF ? "NO" : "YES");
    }
    return 0;
}
