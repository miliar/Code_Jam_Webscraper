#include <iostream>
#include <vector>
using namespace std;

int d[1000000];

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        long long l, t, n, c;
        cin >> l >> t >> n >> c;
        int b[c];
        for (int i = 0; i < c; i++)
            cin >> b[i];
        //int d[n];
        for (int i = 0; i < n; i++)
            d[i] = b[i % c];
        // calculate the remaining distances
        t /= 2;
        int p = 0;
        long long dist = 0;
        while (p < n && t > 0) {
            if (d[p] <= t) {
                t -= d[p];
                dist += d[p];
                d[p] = 0;
                p++;
            } else {
                d[p] -= t;
                dist += t;
                t = 0;
            }
        }
        dist *= 2;
        vector<int> v;
        for (int i = p; i < n; i++)
            v.push_back(d[i]);
        sort(v.begin(), v.end());
        int i;
        for (i = v.size() - 1; i >= 0 && v.size() - 1 - i < l; i--) {
            dist += v[i];
        }
        for (; i >= 0; i--)
            dist += v[i] * 2;
        cout << "Case #" << cc << ": " << dist << "\n";
    }
}
