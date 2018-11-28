#include <algorithm>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <map>
#include <numeric>
#include <set>
#include <vector>
#include <utility>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int N = 1000;
struct Type {
    int b, e, w;
    bool operator<(const Type &rhs) const {
        return b < rhs.b;
    }
    bool operator()(const Type &a, const Type &b) const {
        return a.w < b.w;
    }
} a[N];

int main()
{
    int cases, n;
    double t, X, S, R;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &n);
        for (int i = 0; i < n; i++)
            scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].w);
        sort(a, a+n);
        double res;
        double len = a[0].b + X-a[n-1].e;
        for (int i = 1; i < n; i++)
            len += a[i].b-a[i-1].e;
        double tmp = min(len/R, t);
        len -= tmp*R;
        t -= tmp;
        res = tmp + len/S;
        
        sort(a, a+n, Type());
        for (int i = 0; i < n; i++) {
            double tmp = min((a[i].e-a[i].b)/(a[i].w+R), t);
            t -= tmp;
            res += tmp+(a[i].e-a[i].b-tmp*(a[i].w+R))/(a[i].w+S);
        }

        printf("Case #%d: %.8lf\n", T, res);
    }
}
