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
#include <cstring>
using namespace std;

#define rep(i,a,b) for(int i=a; i<int(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> PI;
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
int mod = 100003;
template <class T> void plu(T &a, T b)
{
    a = (a + b) % mod;
}
const int MAX = 505;
int main() {
    int tt; scanf("%d", &tt);
    ll c[MAX][MAX+1];
    memset(c, 0x00, sizeof(c));
    rep(i,0,MAX)
    {
        c[i][0] = 1;
        rep(j,1,i+1) c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod;
    }

    ll p[MAX][MAX];
    memset(p, 0x00, sizeof(p));
    rep(i,2,MAX) p[i][1] = 1;
    rep(i,2,MAX) rep(j,2,i)
        rep(l,0,j) if (p[j][l])
            plu(p[i][j], p[j][l] * c[i - j - 1][j - l - 1] % mod);

    rep(sd,0,tt)
    {
        ll q = 0;
        int n; cin >> n;
        rep(i,0,n+1) q += p[n][i];
        printf("Case #%d: %lld\n", sd+1, q % mod);
    }
}
