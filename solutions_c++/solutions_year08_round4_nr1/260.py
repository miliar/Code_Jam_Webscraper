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
    a = min(a, b);
}
int main() {
    int t; scanf("%d", &t);
    REP(sd,t)
    {
        int m, v; scanf("%d %d", &m, &v);
        vector<int> type(m+5), val(m+5);
        vector<bool> change(m+5, false);
        int pol = (m-1)/2;
        FOR(i,1,pol+1)
        {
            int ch;
            scanf("%d %d", &type[i], &ch);
            change[i] = ch;
        }
        FOR(i,pol+1,m+1)
        {
            scanf("%d", &val[i]);
            type[i] = 2;
        }

        vector<int> mi1(m+5, 12345678), mi0 = mi1;
        for (int i=m; i>=1; i--)
        {
            if (type[i] == 2)
            {
                if (val[i] == 0) mi0[i] = 0;
                else mi1[i] = 0;
            }
            else
            {
                int chAND = 123456;
                if (type[i] == 1) chAND = 0;
                else if (change[i] == true) chAND = 1;
                
                int chOR = 123456;
                if (type[i] == 0) chOR = 0;
                else if (change[i] == true) chOR = 1;

                zlepsi(mi0[i], min(mi0[2*i], mi0[2*i+1]) + chAND);
                zlepsi(mi0[i], mi0[2*i] + mi0[2*i+1] + chOR);

                zlepsi(mi1[i], mi1[2*i] + mi1[2*i+1] + chAND);
                zlepsi(mi1[i], min(mi1[2*i], mi1[2*i+1]) + chOR);
            }
        }

        int res = 12345678;
        if (v == 1) res = mi1[1];
        else res = mi0[1];
        printf("Case #%d: ", sd+1);
        if (res > m + 5) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
}
