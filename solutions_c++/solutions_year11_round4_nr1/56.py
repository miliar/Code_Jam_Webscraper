#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cstdlib>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>
#include <list>

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef set<int> si;
typedef vector<si> vsi;
typedef vector<vi> vvi;
typedef vector<long long> vl;
typedef vector<pii> vpii;
typedef pair<pii, int> piii;
typedef vector<piii> vpiii;
typedef pair<pii, pii> piiii;
typedef pair<int, double> pid;
typedef pair<pid, pii> pgavno;
typedef long long ll;
typedef pair<double, int> pdi;

double distf(pii a, pii b) {
    return sqrt((a.first * 1. - b.first) * (a.first * 1. - b.first) + (a.second
            * 1. - b.second) * (a.second * 1. - b.second));
}

int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };


int sign(int a) {
    if (a >= 0)
        return 1;
    return -1;
}

int p2(int a) {
    return a * a;
}

int getm() {
    int h, m;
    scanf("%d:%d", &h, &m);
    return h * 60 + m;
}

void putm(int m) {
    printf("%02d:%02d", m / 60, m % 60);
}

vector<int> packed, cur;

int bitcnt(int a) {
    int ans = 0;
    while (a) {
        ans += a & 1;
        a /= 2;
    }
    return ans;
}

vector<string> f;
char buf[2000];

bool ok = true;

int main() {
    int tt;
    cin >> tt;
    for (int cn = 1; cn <= tt; ++cn) {
        int x,s,r,T,n;
        cin >> x >> s >> r >> T >> n;
        double t = T;
        vector<pdi> v;
        for (int i = 0; i < n; ++i) {
            int b,e,w;
            cin >> b >> e >> w;
            x -= (e - b);
            v.push_back(pdi(w + s, e - b));
        }
        assert(x >= 0);
        v.push_back(pdi(s, x));
        sort(v.begin(), v.end());
        double ans = 0.;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i].second <= 0)
                continue;
            double ti = v[i].second * 1. / (r - s + v[i].first);
            double t1 = min(t, ti);
            double t2 = ti - t1;
            ans += ((v[i].second * t1) / ti) / (r - s + v[i].first);
            ans += ((v[i].second * t2) / ti) / (v[i].first);
            t -= t1;
        }
        printf("Case #%d: %.10lf\n", cn, ans);
    }
    return 0;
}
