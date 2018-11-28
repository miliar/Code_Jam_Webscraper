#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>
#include <set>
#include <sstream>
#include <stack>

#define mp make_pair
#define eps 1e-10

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, NT, x, s, r, t, n;
    int i, j;
    int b, e, w;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cin>>x>>s>>r>>t>>n;
        double cur=0;
        double ct=0.0;
        double tl = t;
        int d[128];
        memset(d, 0, sizeof(d));
        d[0] = x;
        for(i=0; i<n; ++i) {
            cin>>b>>e>>w;
            d[w] += e-b;
            d[0] -= e-b;
        }
        for(i=0; i<128; ++i) {
            double tn = 1.0*d[i] / (r+i);
            if (tl >= tn) {
                tl -= tn;
                ct += tn;
            } else {
                ct += tl;
                double left = d[i] - (r+i)*tl;
                tn = left / (s+i);
                ct += tn;
                tl = 0.0;
            }
        }
        printf("Case #%d: %.8lf\n", T, ct);
    }
    return 0;
}
