
// Tomasz Kulczynski
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for (int i=0;i<(n);++i)
#define FOR(i,a,b) for (VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(e,v) for(VAR(e,(v).begin());e!=(v).end();++e)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)(a).size())
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int obroc(int x, int m) {
    return x % 10 * m + x / 10;
}

int licz(int n, int m, int B) {
    int ret = 0;
    for(int x = obroc(n, m); x != n; x = obroc(x, m))
        if(x > n && x <= B)
            ret++;
    return ret;
}

int main() {
    int tt, cas = 0;
    scanf("%d",&tt);
    while(tt--) {
        int a, b;
        scanf("%d %d",&a,&b);
        int c = a, m = 1;
        while(c >= 10) m*=10, c /= 10;
        int ret = 0;
        FOR(n, a, b) ret += licz(n, m, b);
        printf("Case #%d: %d\n",++cas,ret);
    }
    return 0;
}
