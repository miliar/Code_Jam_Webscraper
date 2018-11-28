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
    int t; scanf("%d", &t);
    char c[100000], d[100000];
    REP(sd,t)
    {
        int k; scanf("%d", &k);
        fgets(c, 100000, stdin);
        fgets(c, 100000, stdin);
        int n = strlen(c)-1;

        vector<int> a(k);
        REP(i,k) a[i] = i;

        int res = n+1;
        do {
            for (int j = 0; j < n; j += k)
            {
                REP(i,k)
                    d[j + a[i]] = c[j + i];
            }

            char e = '0';
            int s = 0;
            REP(i,n)
            {
                if (d[i] != e)
                {
                    s++;
                    e = d[i];
                }
            }
            res = min(res, s);
        } while (next_permutation(a.begin(), a.end()));
        printf("Case #%d: %d\n", sd+1, res);
    }
}
