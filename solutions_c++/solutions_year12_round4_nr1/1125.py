#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

inline double sqr(const double &x){
    return x*x;
}
int f[15000], a[14000][2];
int T, n, m;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int cs=1; cs<=T; ++cs){
        scanf("%d",&n);
        for(int i=0;i<n; ++i)
            scanf("%d%d",&a[i][0], &a[i][1]);
        scanf("%d",&m);

        memset(f, 0, sizeof(f));
        f[0] = a[0][0];
        int flag = 0;
        if (f[0]+f[0]>=m) flag = 1;
        for(int i=0; i<n; ++i)
            for(int j=i+1; f[i]>=a[j][0]-a[i][0] && j<n; ++j){
                f[j] = max(f[j],min( a[j][1],a[j][0]-a[i][0]));

                           //     max(sqrt(f[i]*f[i]-sqr(a[j][0]-a[i][0])), f[i])));
                if (f[j]+a[j][0]>=m) flag = 1;
                if (flag==1) break;
            }
        if(f[n-1] + a[n-1][0]+1e-7>=m) flag = 1;
        printf("Case #%d: ", cs);
        if(flag) puts("YES"); else puts("NO");
    }
    return 0;
}
