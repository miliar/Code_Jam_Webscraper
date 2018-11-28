#include <iostream>
#include <deque>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

void run() {
    long long N, Pd, Pg;
    cin >> N >> Pd >> Pg;
    if (Pg == 0 || Pg == 100) {
        if (Pd == Pg) cout << "Possible" << endl;
        else cout << "Broken" << endl;
        return;
    }
    FOR(D,1,N) {
        long long Wt = D * Pd;
        if ((Wt % 100) == 0) {
            cout << "Possible" << endl;
            return;
        }
    }
    cout << "Broken" << endl;
}

int main() {
    int kase;
    cin >> kase;
    FOR(k,1,kase) {
        cout << "Case #" << k << ": ";
        run();
    }
    return 0;
}
