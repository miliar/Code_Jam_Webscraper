#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#define eps 1e-8
using namespace std;
struct IN{
    int x,n;
}p[300];
int C,D;
bool solve(double x){
    double MX=-1e20;
    for (int i=0;i<C;i++){
        for (int j=0;j<p[i].n;j++){
            double cnt=1.0*p[i].x-x;
            if(MX+D>1.0*p[i].x-x){
                cnt=MX+D;
            }
            if (p[i].x+x<cnt) return false;
            MX = cnt;
        }
    }
    return true;
}
int main(){
    int cas;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cas);
    for (int ca=1;ca<=cas;ca++){
        scanf("%d%d",&C,&D);
        double sum = 0;
        double L = 0;
        double mid;
        for (int i=0;i<C;i++){
            scanf("%d%d",&p[i].x,&p[i].n);
            sum+=p[i].n;
        }
        double R = sum*D;
        double ans;
        int T = 100;
        while(R>L+eps){
            T--;
            if(T==0) break;
            mid=(L+R)/2.0;
            if(solve(mid)){
                ans = mid;
                R = mid-eps;
            }else L = mid+eps;
            //cout<<ans<<endl;
        }
        printf("Case #%d: %0.10lf\n",ca,ans);
    }
    return 0;
}
