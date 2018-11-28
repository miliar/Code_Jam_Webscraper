#include <stdio.h>
#include <cmath>
#include <algorithm>
using namespace std;

int n,i, ncase;
double ans;
struct node{
    double x,y,r;
}dd[10];

int main() {
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
  
    scanf("%d", &ncase);
    for (int icase=1; icase<=ncase; ++icase) {
        scanf("%d", &n);
        for(i=0; i<n; i++)
            scanf("%lf%lf%lf", &dd[i].x, &dd[i].y, &dd[i].r);
        if(n == 1){
            ans = dd[0].r;
        }
        else if(n == 2){
            ans = max(dd[1].r, dd[0].r);
        }
        else{
            ans = 1e30;
            double tmp;
            tmp = max((sqrt((dd[0].x-dd[1].x)*(dd[0].x-dd[1].x)+(dd[0].y-dd[1].y)*(dd[0].y-dd[1].y))+dd[1].r+dd[0].r)/2,dd[2].r);
            if (ans > tmp) ans = tmp;
            tmp = max((sqrt((dd[2].x-dd[1].x)*(dd[2].x-dd[1].x)+(dd[2].y-dd[1].y)*(dd[2].y-dd[1].y))+dd[1].r+dd[2].r)/2,dd[0].r);
            if (ans > tmp) ans = tmp;
            tmp = max((sqrt((dd[0].x-dd[2].x)*(dd[0].x-dd[2].x)+(dd[0].y-dd[2].y)*(dd[0].y-dd[2].y))+dd[2].r+dd[0].r)/2,dd[1].r);
            if (ans > tmp) ans = tmp;
        }
        printf("Case #%d: %.10f\n", icase, ans);
    }
    return 0;
}

