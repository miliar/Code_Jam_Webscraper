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
int kol[110][1010];
int main() {
    int n; scanf("%d", &n);
    string ss;
    REP(sd,n)
    {
        int s, q; scanf("%d", &s);
        getline(cin, ss);
        vector<string> names(s);
        map<string, int> a;
        REP(i,s)
        {
            getline(cin, names[i]);
            a[names[i]] = i;
        }

        scanf("%d", &q);
        getline(cin, ss);
        REP(i,s+2) REP(j,q+2) kol[i][j] = q + 47;
        vector<string> query(q);
        REP(i,q) getline(cin, query[i]);

        REP(i,s) kol[i][0] = 0;
        REP(i,q)
        {
            int ind = -1;
            if (a.count(query[i])) ind = a[query[i]];
            REP(j,s)
                if (j != ind) kol[j][i+1] = kol[j][i];
            if (ind != -1)
                REP(j,s) if (j != ind)
                    kol[j][i+1] = min(kol[j][i+1], kol[ind][i] + 1);
        }

        int res = q + 47;
        REP(i,s) res = min(kol[i][q], res);
        cout << "Case #" << sd + 1 << ": " << res << endl;
    }
}
