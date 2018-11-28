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
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> PI;
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
int main() {
    int tt; scanf("%d", &tt);
    REP(sd,tt)
    {
        int n, k;
        string p; cin >> p >> k;
        vector<string> r; p += '+';
        string w;
        REP(i,p.size())
        {
            if (p[i] == '+') { r.push_back(w); w = ""; }
            else w += p[i];
        }

        cin >> n;
        vector<string> s(n);
        REP(i,n) cin >> s[i];
        int mod = 10009;
        vector<int> res(k+1, 0);

        int o[n][26];
        memset(o, 0x00, sizeof(o));
        REP(i,n)
            REP(j,s[i].size()) o[i][s[i][j]-'a']++;
        FOR(j,1,k+1)
        {
            int moc = 1;
            REP(i,j) moc *= n;
            REP(i,moc)
            {
                int u = i;
                vector<int> e(26, 0);
                REP(l,j)
                {
                    int v = u % n;
                    REP(c,s[v].size()) e[s[v][c]-'a']++;
                    u /= n;
                }
                REP(l,r.size())
                {
                    ll ww = 1;
                    REP(oo,r[l].size())
                        ww = (ww * e[r[l][oo]-'a']) % mod;
                    res[j] = (res[j] + ww) % mod;
                }
            }
        }
        printf("Case #%d:", sd+1);
        FOR(i,1,k+1) printf(" %d", res[i]);
        printf("\n");
    }
}
