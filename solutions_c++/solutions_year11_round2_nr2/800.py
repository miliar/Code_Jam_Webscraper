#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
struct pt{
       int w, ren;
};
vector<pt> f;
int n, d;
int ok(double time) {
    double zuo = -1000000000000000000000000000000.0;
    for (int j = 0; j < n; ++j) {
        double xx = f[j].w;
        if (xx + time < zuo + d - 0.0000000001) return 0;
        if ((f[j].ren-1) * d * 1.00  > time * 2) return 0;
        double t = f[j].w - time;
        zuo = zuo + d;
        if (t > zuo + 0.0000000001) zuo = t; 
        zuo = zuo + (f[j].ren-1) * d* 1.00;
        if (zuo > f[j].w + time + 0.000000001) return 0;
    }
    return 1;
}
bool cmp(pt x, pt y) {
     return (x.w < y.w);
}
int main() {
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int tcas = 1; tcas <= cas; ++tcas) {
            
        f.clear();
        scanf("%d%d", &n, &d);
        for (int j = 1; j <= n; ++j) {
            pt x;
            scanf("%d%d", &x.w, &x.ren);
            f.push_back(x);
        }        
        sort(f.begin(), f.end(), cmp);
        double right = 100000000000000000000.0, left = 0;
        while ( right - left > 0.00000000001 ) {
            if (ok((right+left)/2 ) ) right = (right+left)/2; else left = (right+left)/2;
        }
        printf("Case #%d: %lf\n", tcas, right);
    }   
    return 0;
}
