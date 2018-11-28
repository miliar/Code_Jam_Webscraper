#include <iostream>
#include <vector>
using namespace std;

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    
    cout << fixed;
    cout.precision(7);
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        long double t;
        int X, S, R, N;
        vector< pair<int, int> > a;
        cin >> X >> S >> R >> t >> N;
        for (int i = 1; i <= N; ++i) {
            int l, r, w;
            cin >> l >> r >> w;
            a.push_back(make_pair(S + w, r - l));
            X -= r - l;
        }
        a.push_back(make_pair(S, X));
        sort(a.begin(), a.end());
        long double ret = 0;
        for (int i = 0; i < a.size(); ++i) {
            long double v = a[i].first, l = a[i].second;
            if (l / (v + R - S) <= t) {
                t -= l / (v + R - S);
                ret += l / (v + R - S);
            }else {
                ret += t;
                l -= t * (v + R - S);
                ret += l / v;
                t = 0;
            }
        }
        cout << "Case #" << t2 << ": " << ret << endl;
    }
    
    return 0;
}
