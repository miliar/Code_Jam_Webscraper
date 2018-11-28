#include<cstdio>
#include<algorithm>

using namespace std;

const double eps=1e-9;

int x,s,r,t,n,i,j;
int speed[1100000];
int b,e,w;
double ans,need;
int T=0;
int I=0;

int main(){
    scanf("%d",&T);
    while (T--){
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        for (i=0;i<x;++i){
            speed[i]=0;
        }
        for (i=0;i<n;++i){
            scanf("%d%d%d",&b,&e,&w);
            for (j=b;j<e;++j)
                speed[j]=w;
        }
        sort(speed,speed+x);
        double left=t;
        ans=0;
        for (i=0;i<x;++i){
            if (left>eps){
                need=1./(speed[i]+r);
                if (left>=need){
                    left-=need;
                    ans+=need;
                }
                else{
                    ans+=(1-left*(speed[i]+r))/(speed[i]+s)+left;
                    left=0;
                }
            }else{
                ans+=1./(speed[i]+s);
            }
        }
        printf("Case #%d: %.10lf\n",++I,ans);
    }
}
