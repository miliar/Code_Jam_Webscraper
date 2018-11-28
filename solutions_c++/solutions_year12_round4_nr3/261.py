#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define FORALL(a,b) for(typeof((b).begin()) a = (b).begin(); a != (b).end(); ++a)
#define FOR(i,a,b) for(int i = a; i < (int)(b); ++i)

typedef long long LL;

const double EPS = 1e-6;
const int INF = 1<<29;
const int N = 2010;

int x[N], n;
double h[N];

int main()
{
//    freopen("in.txt","r",stdin);
    freopen("C-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T, cas = 0;
    double dt;

    scanf("%d", &T);

    while (T--){
        scanf("%d", &n);
        for (int i = 1; i < n; ++i){
            scanf("%d", &x[i]);
//            printf("%d ", x[i]);
        }
//        putchar('\n');
        h[n] = h[n-1] = 10000.0;
//        h[n-1] = 0.9;
        bool flag = 1;
        for (int i = n-2; i >= 1 && flag; --i){
            int t = x[i];
            double tmp;
            double low = 0, upper = 1e99;
            for (int j = i+1; j <= n; ++j){
                if (j < t){
                    dt = h[j]-h[t];
                    tmp = h[t]+dt*(t-i)/(t-j);
                    if (low < tmp) low = tmp;
//                    if (upper > tmp) upper = tmp;
                }
                if (j > t){
                    dt = h[t]-h[j];
                    tmp = h[j]+dt*(j-i)/(j-t);
//                    if (low < tmp) low = tmp;
                    if (upper > tmp) upper = tmp;

                }
            }
//            printf("low = %.4lf, upper = %.4lf\n", low, upper);
            if (low > upper+EPS) flag = 0;
            if (upper > 1e98) upper = low+1;
            if (low < 0.0001) low = upper-1;
            h[i] = (low+upper)*0.5;
        }
        printf("Case #%d: ", ++cas);
        int BASE = 100;
        if (!flag) puts("Impossible");
        else{
            for (int i = 1; i <= n; ++i) printf("%d ", (int)(h[i]*BASE));
            putchar('\n');
        }
    }

    return 0;
}
