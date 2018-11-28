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

#define REP(i,n) for(__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> PI;
void zlepsi(int &a, int b)
{
    a = max(a, b);
}
int main() {
    int t; scanf("%d", &t);
    REP(sd,t)
    {
        int n, m;
        scanf ("%d %d", &n, &m);
        bool a[n][m];
        REP(i,n)
        {
            char c[100];
            scanf("%s", c);
            REP(j,m) a[i][j] = (c[j] == '.');
        }

        int ma[n+1][1<<m];
        memset(ma, 0x00, sizeof(ma));
        vector<int> mno;
        REP(j,1<<m)
        {
            bitset<10> b(j);
            bool ok = true;
            REP(i,m-1) if (b[i] && b[i+1]) ok = false;
            if (ok) mno.push_back(j);
        }

        REP(k,n)
        {
            REP(j,mno.size())
            {
                bitset<10> b(mno[j]);
                REP(l,mno.size())
                {
                    bitset<10> c(mno[l]);
                    bool ok = true;
                    REP(i,m) if (!a[k][i] && c[i]) ok = false;
                    REP(i,m) if (c[i])
                    {
                        if (i > 0 && b[i-1]) ok = false;
                        if (i < m-1 && b[i+1]) ok = false;
                    }
                    if (ok) zlepsi(ma[k + 1][mno[l]], ma[k][mno[j]] +
                            c.count());
                }
            }
        }

        int res = 0;
        REP(j,mno.size()) zlepsi(res, ma[n][mno[j]]);
        printf("Case #%d: %d\n", sd+1, res);
    }
}
