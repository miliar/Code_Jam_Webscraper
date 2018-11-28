#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <functional>

using namespace std;

typedef long long ll;

struct V {
    int l, d;
    int ml;
};

int main() {
    int T;
    cin >> T;
    for (int z = 1; z <= T; ++z) {
        cout << "Case #" << z << ": ";
        int N;
        cin >> N;
        V vines[N];
        for (int i = 0; i < N; ++i) {
            cin >> vines[i].d >> vines[i].l;
            vines[i].ml = -1;
        }
        int D;
        cin >> D;
        vines[0].ml = vines[0].d;
        for (int i = 1; i < N; ++i) {
            for (int j = 0; j < i; ++j) {
                // can get from j to i?
                if (vines[j].ml < 0) continue;
                if (vines[j].d + vines[j].ml >= vines[i].d) {
                    int L = min(vines[i].l, vines[i].d - vines[j].d);
                    //cout << j << " to " << i << ":" << L << endl;
                    vines[i].ml = max(vines[i].ml, L);
                }
            }
            //cout << vines[i].ml << endl;
        }
        bool ok = false;
        for (int i = 0; i < N; ++i) {
            if (vines[i].ml < 0) continue;
            if (D >= vines[i].d - vines[i].ml && D <= vines[i].d + vines[i].ml) {
                ok = true;
            }
        }
        cout << (ok ? "YES" : "NO") << endl;
    }
}