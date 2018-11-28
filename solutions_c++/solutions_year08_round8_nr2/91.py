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
template <class T> void zlepsi(T &a, T b)
{
    a = max(a, b);
}
int main() {
    int tt; scanf("%d", &tt);
    REP(sd,tt)
    {
        int n; scanf("%d", &n);
        map<string, vector<PI> > col;
        REP(i,n)
        {
            string s; int a, b;
            cin >> s >> a >> b;
            col[s].push_back(PI(a, b));
        }

        vector<string> s;
        FOREACH(it,col) s.push_back(it->first);
        vector<vector<int> > kand;
        REP(i,s.size()) {
            vector<int> a(1, i);
            kand.push_back(a);
            REP(j,i)
            {
                a.push_back(j);
                kand.push_back(a);
                REP(k,j)
                {
                    a.push_back(k);
                    kand.push_back(a);
                    a.pop_back();
                }
                a.pop_back();
            }
        }

        int res = 100000;
        REP(i,kand.size())
        {
            vector<PI> b;
            vector<int> &y = kand[i];
            map<int, set<int> > pump;
            REP(j,y.size())
            {
                vector<PI> &o = col[s[y[j]]];
                REP(k,o.size())
                    pump[o[k].first].insert(o[k].second);
            }

            /*
            vector<int> kol(10010, 123456789);
            kol[1] = 0;
            REP(j,kol.size()) if (!pump[j].empty())
            {
                int kon = *pump[j].rbegin();
                for (int k = j; k <= kon; k++)
                    kol[k + 1] = min(kol[k + 1], kol[j] + 1);
            }
            if (kol[10001] == 4)
                res = min(res, kol[10001]);
            */

            multiset<int> a;
            int akt = 1, poc = 0;
            if (pump[1].empty()) continue;

            map<int, set<int> >::iterator it = pump.begin();
            while (true)
            {
                if (akt < it->first) { poc = 100000; break; }
                while (it != pump.end() && it->first <= akt)
                {
                    a.insert(*it->second.rbegin());
                    it++;
                }

                akt = *a.rbegin() + 1; poc++;
                if (akt > 10000) break;
                if (it == pump.end()) break;
            }

            if (akt > 10000)
                res = min(res, poc);
        }

        if (res < 100000)
            printf("Case #%d: %d\n", sd+1, res);
        else
            printf("Case #%d: IMPOSSIBLE\n", sd+1);
    }
}
