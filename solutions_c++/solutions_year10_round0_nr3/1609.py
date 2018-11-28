#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long lint;

lint d[1010];
int e[1010];
lint v[1010];

lint r, k, ans;
int n;

inline int next(int x) {
    return (x+1) % n;
}

int main() {
    int z;
    cin >> z;
    for(int ca = 1; ca <= z; ++ ca) {
        cin >> r >> k >> n;
        for(int i=0; i<n; ++i) {
            cin >> d[i];
        }
        for(int i=0; i<n; ++i) {
            lint val = d[i];
            int j = next(i);
            while(val + d[j] <= k && j != i) {
                val += d[j];
                j = next(j);
            }
            e[i] = j;
            v[i] = val;
        }
        ans = 0;
        int pos = 0;
        while(r --) {
            ans += v[pos];
            pos = e[pos];
        }
        cout << "Case #" << ca << ": " << ans << endl;
    }
    return 0;
}
