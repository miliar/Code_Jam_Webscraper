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
int main() {
    int n, na, nb, t;
    scanf("%d", &n);
    REP(sd,n)
    {
        scanf("%d %d %d", &t, &na, &nb);
        vector<PI> a[2];
        REP(i,na)
        {
            int a1, a2, b1, b2;
            scanf("%d:%d %d:%d", &a1, &a2, &b1, &b2);
            a[0].push_back(PI(a1*60+a2, b1*60+b2));
        }
        REP(i,nb)
        {
            int a1, a2, b1, b2;
            scanf("%d:%d %d:%d", &a1, &a2, &b1, &b2);
            a[1].push_back(PI(a1*60+a2, b1*60+b2));
        }
        sort(a[0].begin(), a[0].end());
        sort(a[1].begin(), a[1].end());

        int res[2] = {0, 0};
        while (a[0].size() + a[1].size() > 0)
        {
            int strana = 0;
            int cas = -1;
            if (!a[0].empty()) cas = a[0][0].first;
            if (a[0].empty() || (!a[1].empty() && a[0][0] > a[1][0]))
            {
                strana = 1;
                cas = a[1][0].first;
            }
            res[strana]++;

            while (true)
            {
                bool ok = false;
                for (unsigned i = 0; i < a[strana].size(); i++) if (a[strana][i].first >= cas)
                {
                    ok = true;
                    cas = a[strana][i].second + t;
                    a[strana].erase(a[strana].begin() + i);
                    strana = 1-strana;
                    break;
                }
                if (!ok) break;
            }
        }
        cout << "Case #" << sd+1 << ": " << res[0] << " " << res[1] << endl;
    }
}
