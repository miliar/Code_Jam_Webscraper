#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <set>
#include <queue>
using namespace std;

#define MP make_pair
#define PB push_back
#define SS size()
#define all(x) (x).begin(), (x).end()
#define for0(a,b) for (int a = 0; a < (b); ++a)
#define for1(a,b) for (int a = 1; a < (b); ++a)

typedef long long LL;

#define EPS 1e-7


int main() {
    int t;
    cin >> t;

    for (int icase = 1; icase <= t; icase++) {
        LL r, k, n;
        cin >> r >> k >> n;
        vector<LL> gs(n);
        for0 (i, n)
            cin >> gs[i];

        vector<pair<int, LL> > starts(n);
        for0 (i, n) {
            LL sum = 0;
            int next_start = i;
            for0 (p, n) {
                int a = (i + p) % n;
                if (sum + gs[a] > k) {
                    next_start = a;
                    break;
                }
                sum += gs[a];
            }
            starts[i] = MP(next_start, sum);
        }

        LL total = 0;
        int current = 0;
        for0 (i, r) {
            total += starts[current].second;
            current = starts[current].first;
        }

        printf("Case #%d: %lld\n", icase, total);

    }

    return 0;
}
