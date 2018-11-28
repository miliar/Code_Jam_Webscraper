#include <cstdio>
#include <cstring>
#include <cmath>
#define eps 1e-7
double pos[300],copy[300];
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,ca=0;
    int C,D;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&C,&D);
        int t=0;
        for(int i=1;i<=C;i++){
            int p,v;
            scanf("%d%d",&p,&v);
            for(int i=1;i<=v;i++){
                copy[t]=pos[t]=p;
                t++;
            }
        }
 //       printf("%d %d\n",C,D);
//        for(int i=0;i<t;i++)
//            printf("%d ",pos[i]);
//        puts("");
        double l=0,h=10000,mid;
        while(fabs(l-h)>eps){
            double mid=(l+h)/2;
            for(int i=0;i<t;i++)
                pos[i]=copy[i];
            pos[0]-=mid;
            int flag=0;
            for(int i=1;i<t;i++){
                double m=pos[i]-mid;
                if(m-pos[i-1]>=D) pos[i]=m;
                else {
                    m=pos[i-1]+D;
                    if(fabs(m-pos[i])>mid) {
                        flag=1;
                        break;
                    }
                    else pos[i]=m;
                }
            }
            if(flag) { l=mid;}
            else h=mid;
        }
        printf("Case #%d: %.12lf\n",++ca,l);
    }
}


