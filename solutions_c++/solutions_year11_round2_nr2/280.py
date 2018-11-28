#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

pair<int,int> V[210];

void solve(int cas){
    int D,C;
    int i,p,v;
    double low,high,mid;
    scanf("%d%d",&C,&D);
    for (i=0;i<C;i++){
        scanf("%d%d",&p,&v);
        V[i].first=p;
        V[i].second=v;
    }
    sort(V,V+C);
    low = 0.0;
    high = 1.0*D*2e6;
    while (low+1e-8<high){
        mid = (low+high)/2;
        if (low+1e-8>=mid) break;
        if (mid+1e-8>=high) break;
//        printf("%lf\n",mid);
        double lp = -1e12;
        double np;
        int c;
        int flag = 1;
        for (i=0;i<C;i++){
            int cc = V[i].second;
            int vv = V[i].first;
            for (c=0;c<cc;c++){
                np = lp+D;
                if (np<vv-mid) np = vv-mid;
                else if (np>vv+mid){
                    flag = 0;
                    break;
                }
                if (flag == 0) break;
                lp = np;
            }
        }
        if (flag) high = mid;
        else low = mid;
    }
    printf("Case #%d: %.8lf\n", cas, mid);
}

int main(){
    int t,cas;
    scanf("%d",&t);
    for (cas=1;cas<=t;cas++) solve(cas);
    return 0;
}

