#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
using namespace std;

int T, C, D, P[1010101];
int N;

bool check_ok(double det)
{
    double last = -(1LL<<60);
    for(int i = 0; i < N; i++){
        if(P[i]+det < last+D) return false;
        last = max(last+D, P[i]-det);
    }
    return true;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        scanf("%d%d", &C, &D);
        N = 0;
        for(int i = 0 ;i < C; i++){
            int p, v;
            scanf("%d%d", &p, &v);
            while(v--){
                P[N++] = p;
            }
        }
        sort(P, P+N);
        double low = 0, up = 1LL<<60, mid, ans = -1;
        while(low + 1e-8 < up){
            mid = (low+up)/2;
            if(check_ok(mid)) up = mid, ans = mid;
            else low = mid;
        }
        printf("Case #%d: %.10lf\n", cas, ans);
    }
    return 0;
}
