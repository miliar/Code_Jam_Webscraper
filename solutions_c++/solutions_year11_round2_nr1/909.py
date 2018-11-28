#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <queue>
#include <bitset>
#include <utility>
#include <list>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define rep(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
int main() {
    int tt; scanf("%d", &tt);
    rep(sd,0,tt)
    {
        int n; scanf("%d", &n);
        char g[100][102];
        rep(i,0,n) scanf("%s", g[i]);
        vector<double> wp(n), owp(n, 0), oowp(n, 0);
        vi poc(n);
        rep(i,0,n)
        {
            poc[i] = n - count(g[i], g[i] + n, '.');
            wp[i] = count(g[i], g[i] + n, '1') / double(poc[i]);
        }

        rep(i,0,n)
        {
            rep(j,0,n) if (g[i][j] != '.')
                owp[i] += (wp[j] * poc[j] - (g[i][j] == '0')) / double(poc[j] - 1);
            owp[i] /= poc[i];
        }
        rep(i,0,n)
        {
            rep(j,0,n) if (g[i][j] != '.')
                oowp[i] += owp[j];
            oowp[i] /= poc[i];
        }

        printf("Case #%d:\n", sd+1);
        rep(i,0,n)
            printf("%.9lf\n", wp[i] / 4 + owp[i] / 2 + oowp[i] / 4);
    }
}
