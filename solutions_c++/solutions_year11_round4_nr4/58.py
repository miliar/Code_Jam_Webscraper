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
typedef pair<ll, ll> pll;

pll operator+(pll a, pll b) {
    return pll(a.first + b.first, a.second + b.second);
}

pll operator-(pll a, pll b) {
    return pll(a.first - b.first, a.second - b.second);
}

pll operator*(pll a, ll b) {
    return pll(a.first * b, a.second * b);
}

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

int ans = 0;

void fmaxtr(int v, set<int> & curthreat, set<int> & curown, vector<vi> & gr, vi & lev) {
    if (v == 1) {
        assert(curown.size() == lev[1]);
        ans = max(ans, int(curthreat.size()));
    }
    if (lev[v] >= lev[1])
        return;
    curthreat.erase(v);
    curown.insert(v);
    vi nowins;
    for (int i = 0; i < gr[v].size(); ++i) {
        if (!curown.count(gr[v][i]) && !curthreat.count(gr[v][i])) {
            curthreat.insert(gr[v][i]);
            nowins.push_back(gr[v][i]);
        }
    }
    for (int i = 0; i < nowins.size(); ++i) {
        if (lev[nowins[i]] == lev[v] + 1)
            fmaxtr(nowins[i], curthreat, curown, gr, lev);
    }
    for (int i = 0; i < nowins.size(); ++i) {
        curthreat.erase(nowins[i]);
    }
    curown.erase(v);
    curthreat.insert(v);
}

int main() {
    int tt;
    cin >> tt;
    for (int cn = 1; cn <= tt; ++cn) {
        int n,m;
        cin >> n >> m;
        vector<vi> gr(n);
        for (int i = 0; i < m; ++i) {
            int a,b;
            scanf("%d,%d", &a, &b);
            gr[a].push_back(b);
            gr[b].push_back(a);
        }
        vi q(1, 0);
        vi lev(n, 100000000);
        lev[0] = 0;
        vector<char> was(n);
        was[0] = 1;
        for (int i = 0; i < q.size(); ++i) {
            int curv = q[i];
            for (int j = 0; j < gr[curv].size(); ++j) {
                int nv = gr[curv][j];
                if (!was[nv]) {
                    was[nv] = 1;
                    q.push_back(nv);
                    lev[nv] = lev[curv] + 1;
                }
            }
        }
        ans = 0;
        assert(lev[1] < 100000);
        set<int> curthreat;
        set<int> curown;
        fmaxtr(0, curthreat, curown, gr, lev);
        printf("Case #%d: %d %d\n", cn, lev[1] - 1, ans);
    }
    return 0;
}
/*
int main() {
    int tt;
    cin >> tt;
    vector<char> seed(1010000, 1);
    seed[0] = 0;
    seed[1] = 0;
    vector<ll> pr;
    for (int i = 2; i < seed.size(); ++i) {
        if (seed[i]) {
            pr.push_back(i);
            //cout << i << endl;
            for (int j = i + i; j < seed.size(); j += i) {
                seed[j] = 0;
            }
        }
    }
    for (int cn = 1; cn <= tt; ++cn) {
        ll n;
        ll ans = 0;
        cin >> n;
        if (n >= 2)
            ans += 1;
        for (int i = 0; i < pr.size() && pr[i] < n; ++i) {
            int cnt = 0;
            ll cur = pr[i];
            for (; cur <= n; ++cnt, cur *= pr[i])
                ;
            assert(cnt >= 1);
            ans += cnt - 1;
        }
        printf("Case #%d: %lld\n", cn, ans);
    }
    return 0;
}
*/
/*
int main() {
    int tt;
    cin >> tt;
    for (int cn = 1; cn <= tt; ++cn) {
        int r, c, d;
        cin >> r >> c >> d;
        vector<vl> f(r + 1, vl(c + 1));
        vector<vector<pll> > cmv(r + 1, vector<pll> (c + 1));
        vector<vl> sums(r + 1, vl(c + 1));
        string s;
        for (int i = 0; i < r; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < c; ++j) {
                f[i + 1][j + 1] = (s[j] - '0') + d;
            }
        }
        for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j) {
                cmv[i][j] = cmv[i][j] + cmv[i - 1][j];
                sums[i][j] += sums[i - 1][j];

                cmv[i][j] = cmv[i][j] + cmv[i][j - 1];
                sums[i][j] += sums[i][j - 1];

                cmv[i][j] = cmv[i][j] - cmv[i - 1][j - 1];
                sums[i][j] -= sums[i - 1][j - 1];

                sums[i][j] += f[i][j];
                cmv[i][j] = cmv[i][j] + pll(i * 2, j * 2) * f[i][j];
            }
        }
        int ans = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                for (int k = 3; k <= min(c, r) && k + i <= r && k + j <= c; ++k) {
                    ll ci = i * 2 + k + 1;
                    ll cj = j * 2 + k + 1;
                    pll pc(ci, cj);
                    ll su = sums[i + k][j + k] - sums[i][j + k]
                            - sums[i + k][j] + sums[i][j];
                    pll cm = cmv[i + k][j + k] - cmv[i][j + k] - cmv[i + k][j]
                            + cmv[i][j];
                    cm = cm - pc * su;
                    for (int ii = i + 1; ii <= i + k; ii += k - 1)
                        for (int jj = j + 1; jj <= j + k; jj += k - 1)
                            cm = cm - (pll((ii) * 2, (jj) * 2) - pc)
                                    * f[ii][jj];
                    if (cm == pll(0, 0)) {
                        //cout << i << " " << j << " " << k << endl;
                        ans = max(ans, k);
                    }
                }
            }
        }
        printf("Case #%d: ", cn);
        if (ans)
            printf("%d\n", ans);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
*/
