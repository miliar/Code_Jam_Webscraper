#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

void run() {
    int N;
    cin >> N;
    vector<int> mm(N), mv(N, 0);
    REP(i,N) {
        cin >> mm[i];
        --mm[i];
    }
    double res = 0;
    REP(i,N) {
        if (mv[i] == 1) continue;
        int cnt = 0;
        int now = mm[i];
        while (true) {
            ++cnt;
            mv[now] = 1;
            if (now == i) break;
            now = mm[now];
        }
        if (cnt >= 2) res += cnt;
    }
    cout << setprecision(9) << res << endl;
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
