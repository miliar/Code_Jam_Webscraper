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

class walkway {
public:
    int b, e, w, d;
    walkway(int bb, int ee, int ww) : b(bb), e(ee), w(ww) {
        d = e - b;
    }
    bool operator<(const walkway& rhs) const {
        return b < rhs.b;
    }
};

class wy {
public:
    int b, e, w, d;
    wy(int bb, int ee, int ww) : b(bb), e(ee), w(ww) {
        d = e - b;
    }
    bool operator<(const wy& rhs) const {
        return w < rhs.w;
    }
};

void run() {
    int X, S, R, t, N;
    cin >> X >> S >> R >> t >> N;
    vector<walkway> mm;
    REP(i,N) {
        int B, E, w;
        cin >> B >> E >> w;
        mm.push_back(walkway(B, E, w + S));
    }
    sort(mm.begin(), mm.end());
    int len = mm.size();
    if (mm[0].b > 0) {
        mm.push_back(walkway(0, mm[0].b, S));
    }
    int next = 0;
    REP(i,len) {
        if (i == len - 1) next = X;
        else next = mm[i + 1].b;
        if (mm[i].e < next) {
            mm.push_back(walkway(mm[i].e, next, S));
        }
    }
    sort(mm.begin(), mm.end());
    vector<wy> mm1;
    REP(i,mm.size()) {
        mm1.push_back(wy(mm[i].b, mm[i].e, mm[i].w));
    }
    sort(mm1.begin(), mm1.end());
    double ret = 0.0, tmp = t;
    int dis = X;
    REP(i,mm1.size()) {
        double dd = min(mm1[i].d, dis);
        double ts = mm1[i].w + R - S;
        double tt = dd / ts;
        if (tt >= tmp) {
            ret += tmp;
            ret += (dd - ts * tmp) / mm1[i].w;
            tmp = 0;
        } else {
            ret += tt;
            tmp -= tt;
        }
        dis -= min(mm1[i].d, dis);
        if (dis == 0) break;
    }
    //printf("%.9lf\n", ret);
    cout << setprecision(9) << ret << endl;
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
