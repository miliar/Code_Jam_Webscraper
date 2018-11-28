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
#include <cassert>
#include <cctype>
using namespace std;

#define rep(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define trav(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<double, double> pdd;
typedef pair<int, int> pii;
typedef vector<int> vi;
int main()
{
    int tt; scanf("%d", &tt);
    rep(sd,0,tt)
    {
        int n, w, l;
        scanf("%d %d %d", &n, &w, &l);

        vector<pii> r(n);
        rep(i,0,n)
        {
            scanf("%d", &r[i].first);
            r[i].second = i;
        }

        sort(r.begin(), r.end());
        reverse(r.begin(), r.end());
        vector<pii> res(n);

        int line = -r[0].first, nline = r[0].first;
        int last = -r[0].first;
        rep(i,0,n)
        {
            if (last + r[i].first > l)
            {
                last = -r[i].first;
                line = nline;
                nline = line + 2 * r[i].first;
            }

            res[i].first = line + r[i].first;
            if (res[i].first < 0)
                res[i].first = 0;
            assert(res[i].first <= w);
            res[i].second = last + r[i].first;
            last = res[i].second + r[i].first;
        }

        printf("Case #%d:", sd+1);
        vector<pii> real(n);
        rep(i,0,n)
            real[r[i].second] = res[i];
        rep(i,0,n)
            cout << " " << real[i].first << " " << real[i].second;
        cout << endl;
    }
}
