#include <cstdio>
#include <algorithm>
using namespace std;

const int N=105;

int As[N],At[N];
int Bs[N],Bt[N];
int t,a,b;

int main(){
    int cas,ic;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        int i,j;
        scanf("%d%d%d",&t,&a,&b);
        for(i=0;i<a;i++){
            int h,m;
            scanf("%d%*c%d",&h,&m);
            As[i]=h*60+m;
            scanf("%d%*c%d",&h,&m);
            At[i]=h*60+m;
        }
        for(i=0;i<b;i++){
            int h,m;
            scanf("%d%*c%d",&h,&m);
            Bs[i]=h*60+m;
            scanf("%d%*c%d",&h,&m);
            Bt[i]=h*60+m;
        }
        sort(At,At+a);
        sort(Bs,Bs+b);
        sort(As,As+a);
        sort(Bt,Bt+b);
        int ansa,ansb;
        ansa=a;
        ansb=b;
        j=0;
        for(i=0;i<b&&j<a;i++){
            if(At[j]+t<=Bs[i]){
                ansb--;
                j++;
            }
        }
        j=0;
        for(i=0;i<a&&j<b;i++){
            if(Bt[j]+t<=As[i]){
                ansa--;
                j++;
            }
        }
        printf("Case #%d: %d %d\n",ic,ansa,ansb);
    }
    return 0;
}
