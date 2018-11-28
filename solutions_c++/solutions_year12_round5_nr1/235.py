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

struct omg {
    int l;
    int p;
    int i;
    bool operator <(const omg& a) const {
        return (p == a.p) ? (i < a.i) : (p > a.p);
    }
};

int main() {
    int T;
    cin >> T;
    for (int z = 1; z <= T; ++z) {
        cout << "Case #" << z << ":";
        int N;
        cin >> N;
        omg wtf[N];
        for (int i = 0; i < N; ++i) {
            cin >> wtf[i].l;
            wtf[i].i = i;
        }for (int i = 0; i < N; ++i) {cin >> wtf[i].p;}
        sort(wtf, wtf+N);
        for (int i = 0; i < N; ++i) {
            cout << ' ' << wtf[i].i;
        }
        cout << endl;
    }
}