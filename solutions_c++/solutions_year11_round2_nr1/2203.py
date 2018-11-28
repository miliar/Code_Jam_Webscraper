#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

typedef long long ll;

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, N;
    char ch[120][120] = {0};
    double wp[120], owp[120], oowp[120];
    scanf("%d",&T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d",&N);
        REP(i,N) scanf("%s", &ch[i]);
        int tot[120] = {0}, win[120] = {0};
        REP(i,N) {
            REP(j,N) {
                if (ch[i][j] != '.') ++tot[i];
                if (ch[i][j] == '1') ++win[i];
            }
            wp[i] = (double)win[i]/tot[i];
        }
        REP(i,N) {
            double sum = 0;
            REP(j,N) {
                if (ch[i][j] == '0')
                    sum += (double)(win[j] - 1) / (tot[j] - 1);
                else if (ch[i][j] == '1')
                    sum += (double)win[j] / (tot[j] - 1);
            }
            owp[i] = (double)sum/tot[i];
        }
        REP(i,N) {
            double sum = 0;
            REP(j,N) {
                if (ch[i][j] != '.')
                    sum += owp[j];
            }
            oowp[i] = (double)sum/tot[i];
        }
        printf("Case #%d:\n", tc);
        REP(i,N) cout << .25 * oowp[i] + .5 * owp[i] + .25 * wp[i] << endl;
    }
    return 0;
}
