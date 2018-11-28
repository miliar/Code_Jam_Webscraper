#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int r, k, n;
        cin >> r >> k >> n;
        vector<int> g(n);
        for (int i = 0; i < n; ++i) {
            cin >> g[i];
        }
        map< int, pair<int, long long> > next;
        vector<long long> rem(1, 0);
        int s = 0;
        while (next.find(s) == next.end()) {
            int i;
            long long c = 0;
            for (i = 0; i < n; ++i) {
                if (c + g[(s + i) % n] > k) break;
                c += g[(s + i) % n];
            }
            next[s] = make_pair((s + i) % n, c);
            rem.push_back(rem.back() + c);
            s = (s + i) % n;
        }
        long long result = 0, onecycle = 0;
        for (int i = 0; i != s; i = next[i].first) { result += next[i].second; --r; }
        int cycle = 0;
        for (int i = s; !cycle || i != s; i = next[i].first) { onecycle += next[i].second; ++cycle; }
        result += onecycle * (r / cycle);
        r %= cycle;
        for (int i = s; r; --r, i = next[i].first) result += next[i].second;
        cout << "Case #" << (test + 1) << ": " << result << endl;
    }
}
