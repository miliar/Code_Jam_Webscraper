#include <cstdio>
#include <vector>
#include <cstring>
#include <utility>
#include <map>
#include <algorithm>
using namespace std;

const double eps=1e-9;
vector<pair<int,int>> a;

double d;

bool gao(double t){
    double x=-1e30;
    for(int i=0;i<int(a.size());i++){
        x=max(x,a[i].first-t-d);
        x+=d*a[i].second;
        if(x>a[i].first+t) return false;
    }
    return true;
}

int main(){
    int cs,n;
    scanf("%d",&cs);
    FILE* fp=fopen("b.out","w");
    for(int t=1;t<=cs;t++){
        scanf("%d%lf",&n,&d);
        a.clear();
        for(int i=0;i<n;i++){
            int p,v;
            scanf("%d%d",&p,&v);
            a.push_back({p,v});
        }
        double lo=0,hi=2e12;
        int cnt=0;
        while(lo+eps<hi && cnt++<10000000){
            double m=(lo+hi)/2;
            if(gao(m)) hi=m; else lo=m;
        }
        double ans=(lo+hi)/2;
        fprintf(fp,"Case #%d: %.14f\n",t,ans);
        printf("Case %d done!\n",t);
    }
}
