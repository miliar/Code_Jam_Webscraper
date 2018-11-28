#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

void convert(const vector<long long>& d, int ms, vector<long long>& r) {
    for (int i = 0; i < d.size(); i++)
        if (ms & (1<<i))
            r.push_back(d[i]);
}

void solve() {
    int n;
    cin >> n;
    vector<long long> r1, r2;

    vector<long long> d(n);
    for (int i = 0; i < n; ++i)
        cin >> d[i];
    vector< vector<int> > sum(n << 17);

    for (int ms = 1; ms < (1<<n); ms++) {
        int sm = 0;
        for (int i = 0; i < n; ++i) if (ms & (1<<i)) sm += d[i];
        sum[sm].push_back(ms);
    }

    for (int i = 0; i < sum.size() && !r1.size(); ++i) {
        for (int j = 0; j < sum[i].size() && !r1.size(); j++) for (int k = j + 1; k < sum[i].size(); k++)
            if ((sum[i][j] & sum[i][k]) == 0) {
                convert(d, sum[i][j], r1);
                convert(d, sum[i][k], r2);
                break;
            }
    }

    static int test = 0;
    cout << "Case #" << ++test << ":" << endl;
    
    if (r1.size() == 0) {
        cout << "Impossible" << endl;
        return;
    }
    
    for (int i = 0; i < r1.size(); i++) {
        if (i) cout << ' ';
        cout << r1[i];
    }
    cout << endl;
    for (int i = 0; i < r2.size(); i++) {
        if (i) cout << ' ';
        cout << r2[i];
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}
