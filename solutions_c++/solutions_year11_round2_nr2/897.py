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
typedef pair<int, int> PI;
typedef vector<int> vi;
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
int main() {
    int tt; scanf("%d", &tt);
    rep(sd,0,tt)
    {
        int n, d;
        scanf("%d %d", &n, &d);
        vi v(n), p(n);
        vi pos;
        rep(i,0,n)
        {
            scanf("%d %d", &p[i], &v[i]);
            rep(k,0,v[i])
                pos.push_back(p[i]);
        }

        double res = 1e20;
        rep(t,0,1000)
            rep(i,0,pos.size())
            {
                double posl = -1e20;
                double prejde = t / 2.;
                bool ok = true;
                rep(j,0,i+1)
                {
                    if (posl + d > pos[j] + prejde + 1e-6)
                        ok = false;
                    posl = max(pos[j] - prejde, posl + d);
                }
                double tat = posl;

                posl = 1e20;
                for (int j = pos.size() - 1; j > i; j--)
                {
                    if (posl - d < pos[j] - prejde + 1e-6)
                        ok = false;
                    posl = min(pos[j] + prejde, posl - d);
                }
                if (tat + d - 1e-6 > posl)
                    ok = false;
                if (ok)
                    res = min(res, prejde);
                /*
                if (t == 2 && ok)
                {
                    cout << i << " " << prejde << endl;
                    break;
                }
                */
            }

        printf("Case #%d: %.9lf\n", sd+1, res);
    }
}
