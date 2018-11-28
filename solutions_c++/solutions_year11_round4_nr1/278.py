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

const double pi = 3.1415926535;
const double eps = 1e-6;

struct TE {
    double l, r, v;
}E[110000];
bool cmp(TE a, TE b)
{
    return a.v < b.v;
}
double x, s, r, t;
int n;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T, ca = 0;
    for (scanf("%d", &T); T; T--) {
        scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
        double res = x;
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf%lf", &E[i].l, &E[i].r, &E[i].v);
            res -= E[i].r - E[i].l;
        }
        sort(E, E + n, cmp);
        double ans = 0;
        if (res <= t * r)  
            ans += res / r, t -= ans;
        else {
            ans += t + (res - r * t) / s;
            t = 0;
        }
        double del = 0;
        for (int i = 0; i < n; i++)
            if (E[i].r - E[i].l <= t * (r + E[i].v)) {
                del = (E[i].r - E[i].l) / (r + E[i].v);
                ans += del, t -= del;
            } else {
                ans += t + (E[i].r - E[i].l - t * (r + E[i].v)) / (s + E[i].v);
                t = 0;
            }
        printf("Case #%d: %.9lf\n", ++ca, ans);
    }
}
