#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000 + 1000;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

int solve() {
    int n, m;
    cin >> n >> m;
    VVI v;
    VI p;
    for (int i = 1; i <= n; i++) {
        p.PB(i);
    }
    v.PB(p);
    vector<int> a(m);
    vector<int> b(m);
    for (int i = 0; i < m; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    int KK = 8;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < v.size(); j++) {
            int ile = 0;
            int p1 = -1;
            int p2 = -1;
            for (int k = 0; k < v[j].size(); k++) {
                if (a[i] == v[j][k]) {
                    p1 = k;
                    ile++;
                }
                if (b[i] == v[j][k]) {
                    p2 = k;
                    ile++;
                }
            }
            if (ile == 2) {
                VI e1, e2;
                for (int k = 0; k < v[j].size(); k++) {
                    if (k <= p1 || k >= p2)
                        e1.PB(v[j][k]);
                    if (k >= p1 && k <= p2)
                        e2.PB(v[j][k]);
                }
                v.erase(v.begin() + j);
                v.PB(e1);
                v.PB(e2);
                KK = min(KK, (int)e1.size());
                KK = min(KK, (int)e2.size());
                break;
            }
        }
    }
    // check
    //cout << endl;
    //for (int i = 0; i < v.size(); i++) {
    //    for (int j = 0; j < v[i].size(); j++) {
    //        cout << v[i][j] << " ";
    //    }
    //    cout << endl;
    //}


    vector<int> kol(n);
    for (int kk = KK; kk >= 1; kk--) {
        int N = 1;
        for (int i = 0; i < n; i++)
            N *= kk;
        for (int i = 0; i < N; i++) {
            bool czy = true;
            int p = i;
            for (int j = 0; j < n; j++) {
                kol[j] = p % kk;
                p /= kk;
            }
            for (int j = 0; j < v.size(); j++) {
                vector<int> used(kk, 0);
                int ile = 0;
                for (int k = 0; k < v[j].size(); k++) {
                    int kolor = kol[v[j][k] - 1];
                    if (used[kolor] == 0) {
                        ile++;
                        used[kolor] = 1;
                    }
                }
                //cout << i << ' ' << j << ' ' << ile << endl;
                if (ile < kk) czy = false;
            }
            if (czy) {
                cout << kk << '\n';
                for (int i = 0; i < n; i++) {
                    cout << kol[i] + 1 << " ";
                }
                cout << endl;
                return 0;
            }
        }
    }
    assert(false);
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        cout << "Case #" << u << ": ";
        solve();
    }
}

