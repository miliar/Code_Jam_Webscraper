/*
 * Author: ZaviOr
 * Created Time:  2011/6/4 23:41:55
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define for_each(I,V) for (typeof(V.begin()) I = V.begin(); I != V.end(); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
typedef long long LL;

int val[20][20];

int main() {
    freopen("B.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t++ < T) {
        int n, m, d;
        cin >> n >> m >> d;
        //out(n); out(m); out(d);
        REP(i, n) {
            REP(j, m) {
                char c;
                scanf(" %c", &c);
                //cerr << c;
                val[i][j] = d + (c - '0');
                //cerr << val[i][j] << " ";
            }
            //cerr << endl;
        }
        int ans = 0;
        REP(lx, n)
            REP(ly, m) {

                //if (lx == 1 && ly == 1) printf("AA");
                for (int sz = 3; lx + sz <= n && ly + sz <= m; ++sz) {
                    int rx = lx + sz, ry = ly + sz;
                    //if (lx == 1 && ly == 1) {out(rx); out(ry);}
                    double cx = (0.0 + rx - lx) / 2, cy = (0.0 + ry - ly) / 2, sumx = 0, sumy = 0;
                    FOR(i, lx, rx) {
                        FOR(j, ly, ry) {
                            //if (lx == 1 && ly == 1)       cerr << val[i][j] << " ";
                            if ((i == lx && j == ly) ||
                                    (i == lx && j == ry - 1) ||
                                    (i == rx - 1&& j == ly) ||
                                    (i == rx - 1 && j == ry - 1))
                                continue;
                            //out(i); out(j);
                            sumx += (0.5 + i - lx - cx) * val[i][j];
                            sumy += (0.5 + j - ly - cy) * val[i][j];
                        }
                        //if (lx == 1 && ly == 1)                        cerr << endl;
                    }
                    //if (lx == 1 && ly == 1) { out(sumx); out(sumy);}
                    if (fabs(sumx) < 1e-8 && fabs(sumy) < 1e-8 && sz > ans) {
                        //out(lx); out(ly); out(sumx); out(sumy);
                        ans = sz;
                    }
                }
            }
        printf("Case #%d: ", t);
        if (ans == 0)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
    return 0;
}

