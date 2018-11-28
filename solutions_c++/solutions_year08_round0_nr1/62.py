#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

const int INF = 0x40000000;

int main() {

    int nCases;
    cin >> nCases;

    REP(iCase, nCases) {

        int m;
        cin >> m >> ws;

        map<string,int> names;
        REP(i, m) {
            string s;
            getline(cin, s);
            names[s] = i;
        }

        int n;
        cin >> n >> ws;

        vector<int> v(n);
        REP(i, n) {
            string s;
            getline(cin, s);
            v[i] = names[s];
        }

        vector<int> cur(m, 0);
        REP(t, n) {
            int x = v[t];
            REP(i, m) if (i != x)
                cur[i] <?= cur[x] + 1;
            cur[x] = INF;
            /*
            REP(i, m)
                cout << cur[i] << " ";
            cout << endl;
            */
        }

        int res = *min_element(ALLOF(cur));

        cout << "Case #" << iCase+1 << ": " << res << endl;

    }

    return 0;
}
