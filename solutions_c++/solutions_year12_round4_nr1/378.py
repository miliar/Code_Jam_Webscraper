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

const int N = 10360;
LL l[N], d[N], D;
int n;
LL dis[N];
bool vis[N];

int main() {
        int T; scanf("%d", &T);
        FOE(ca, 1, T) {
                scanf("%d", &n);
                FOR(i, 0, n) scanf("%lld%lld", d+i, l+i);
                scanf("%lld", &D);

                d[n++] = D; l[n-1] = 0;

                CLR(vis);
                memset(dis, -1, sizeof(dis));
                dis[0] = d[0];

                while (true) {
                        LL mx = 0, idx = -1;
                        FOR(i, 0, n) {
                                if (!vis[i] && dis[i] > mx) {
                                        mx  = dis[i];
                                        idx = i;
                                }
                        }
                        if (idx == -1) break;
//                      printf("idx=%d: %lld\n", idx, d[idx]);
                        vis[idx] = true;
                        FOR(k, 1, n) {
                                int j = idx + k;
                                if (j > n) break;
                                if (d[j] - d[idx] > dis[idx]) break;
                                LL ne = min(d[j] - d[idx], l[j]);
//                              LL ne = dis[idx] - (d[j] - d[idx]);
//                              ne = min(ne, l[j]);
                                if (ne < 0) break;
                                dis[j] = max(dis[j], ne);
                        }
                        FOR(k, 1, n) {
                                int j = idx - k;
                                if (j < 0) break;
                                if (d[idx] - d[j] > dis[idx]) break;
                                LL ne = min(d[idx] - d[j], l[j]);
//                              LL ne = dis[idx] - (d[idx] - d[j]);
//                              ne = min(ne, l[j]);
                                if (ne < 0) break;
                                dis[j] = max(dis[j], ne);
                        }
                }

                printf("Case #%d: %s\n", ca, (dis[n-1] >= 0 ? "YES" : "NO"));
        }
        return 0;
}
