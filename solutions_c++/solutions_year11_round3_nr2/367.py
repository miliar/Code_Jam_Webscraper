#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn = 1100000;

int L, n, c;
long long res, t, dis[maxn], totl, tim[maxn], fst[maxn];
long long r1, r2;

class tnode {
public:
    long long vy, vn;
    long long times;
    int id;
};

int m;
tnode p[maxn * 2];

bool operator<(const tnode &a, const tnode &b) {
    return (a.vn - a.vy) > (b.vn - b.vy);
}

long long min(long long a, long long b) {
    return a < b ? a : b;
}

void solve() {
    res = 0;

    rep(i, c) {
        tim[i] = n / c;
    }
    rep(i, n%c) {
        tim[i]++;
    }
//    rep(i, c) cout << tim[i] << " "; cout << endl;
    totl = 0;
    fst[0] = 0;
    rep(i, c) {
        totl += dis[i];
        fst[i+1] = totl;
//        all += dis[i] * tim[i];
    }

    long long nt = (t / 2) / totl;
//    cout << nt << endl;
    rep(i, c) {
        long long tmp = min(nt, tim[i]);
        tim[i] -= tmp;
        res += dis[i] * 2 * tmp;
    }
    //cout << "res = " << res << endl;
    long long nr = (t / 2) % totl;

//    cout << nr << endl;
    m = 0;
    int ok = -1;
    rep(i, c) {
        if (nr >= dis[i]) {
            res += dis[i] * 2;
            tim[i]--;
        } else {
            ok = i;
            tnode node, node1;
            node.vy = nr * 2 + dis[i] - nr;
            node.vn = dis[i] * 2;
            node.times = 1;
            node.id = i;
            p[m++] = node;
            node1.id = i;
            node1.vy = dis[i];
            node1.vn = dis[i] * 2;
            node1.times = tim[i] - 1;
            p[m++] = node1;
            break;
        }
        nr -= dis[i];
    }
    rep(i, c) if (i != ok) {
        tnode node;
        node.vy = dis[i];
        node.vn = dis[i] * 2;
        node.times = tim[i];
        node.id = i;
        p[m++] = node;
    }
    sort(p, p + m);
    //rep(i, m) if (p[i].vy > p[i].vn) for(;;);
//    cout << res << " " << L << endl;
//    rep(i, m) cout << p[i].id << " " << p[i].vy << " " << p[i].vn << " " << p[i].times << endl;
    rep(i, m) if (p[i].times > 0) {
        if (L == 0) break;
        long long num = min(L, p[i].times);
        res += p[i].vy * num;
        p[i].times -= num;
        L -= num;
    }

    rep(i, m) res += p[i].vn * p[i].times;
    //res /= 2;
}

int main() {
    int cas;
    cin >> cas;
    for (int tt = 0; tt < cas; tt++) {
        cin >> L >> t >> n >> c;
        rep(i, c) cin >> dis[i];
        //printf("Case #%d: %d\n", tt + 1, res);
        solve();
        cout << "Case #" << tt + 1 << ": " << res << endl;
    }
    return 0;
}
