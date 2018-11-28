#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const int N = 2036;
LL W, L;
LL r[N];
int n;
LL x[N], y[N]; // center
LL rr[N];

LL Abs(LL x) { return x < 0 ? -x : x; }

pii p[N];

bool chk(int i) {
        if (x[i] < 0 || x[i] > W || y[i] < 0 || y[i] > L) {
                return false;
        }

        FOR(j, 0, i) {
                LL dx = Abs(x[i] - x[j]);
                LL dy = Abs(y[i] - y[j]);
                if (dx < r[i]+r[j] && dy < r[i]+r[j]) {
                        return false;
                }
        }
        return true;
}

int main() {
        int T; scanf("%d", &T);
        FOE(ca, 1, T) {
                scanf("%d%lld%lld", &n, &W, &L);
                FOR(i, 0, n) scanf("%lld", r+i);

                FOR(i, 0, n) {
                        rr[i] = r[i];
                        p[i] = pii(r[i], i);
                }
                sort(r, r+n);
                reverse(r, r+n);

                sort(p, p+n);
                reverse(p, p+n);

                x[0] = y[0] = 0;
                FOR(i, 1, n) {
                        bool so = false;
                        FOR(j, 0, i) {
                                FOR(iter, 0, 2) {
                                        LL &a = x[i], &b = y[i];
                                        if (iter == 0) {
                                                a = x[j] - r[j] + r[i];
                                                b = y[j] + r[j] + r[i];
                                        } else {
                                                a = x[j] + r[j] + r[i];
                                                b = y[j] - r[j] + r[i];
                                        }
                                        a = max(a, 0LL);
                                        b = max(b, 0LL);
                                        if (chk(i)) {
                                //              printf("%d %d\n", i, j);
                                                so = true;
                                                goto HERE;
                                        }
                                }
                        }
HERE: ;
          if (!so) puts(".");
                }

                printf("Case #%d:", ca);
//              FOR(i, 0, n) printf(" %lld %lld", x[i], y[i]);
//              puts("");

                LL fx[N], fy[N];
                FOR(i, 0, n) {
                        fx[ p[i].y ] = x[i];
                        fy[ p[i].y ] = y[i];
                }
                FOR(i, 0, n) printf(" %lld %lld", fx[i], fy[i]);
                puts("");

                FOR(i, 0, n) FOR(j, i+1, n) {
                        LL dx = Abs(fx[i]-fx[j]);
                        LL dy = Abs(fy[i]-fy[j]);
                        LL sr = rr[i]+rr[j];
                        if (dx < sr && dy < sr) puts(".");
                }
        }
        return 0;
}
