#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

struct node{
    double first;
    int second;
    int ses;
};

bool cmp(node a,node b){
    if (fabs(a.first)<1e-6 && fabs(b.second)<1e-6) 
        return a.second<b.second;
    if (fabs(a.first-b.first)<1e-8){
        if (a.ses<b.ses) return true;
        if (a.ses>b.ses) return false;
        return a.second<b.second;
    }
    return (a.first>b.first);
}
node a[1200];
int n;

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        scanf("%d",&n);
        for (int i=1;i<=n;++i){
            a[i].second=i-1;
            scanf("%d",&a[i].ses);
            a[i].first=a[i].ses;
        }
        double p;
        for (int i=1;i<=n;++i){
            scanf("%lf",&p);
            a[i].first*=p;
        }
        sort(a+1,a+n+1,cmp);
        /*
        for (int i=1;i<=n;++i){
            printf("%.2f %d\n",a[i].first,a[i].second);
        }
        */
        printf("Case #%d:",++cas);
        for (int i=1;i<=n;++i) printf(" %d",a[i].second);
        puts("");
    }
    return 0;
}
