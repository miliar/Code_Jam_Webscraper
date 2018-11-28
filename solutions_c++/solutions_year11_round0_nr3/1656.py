#include<cstdio>
#define INF (1<<29)

int n,t;
int ans;

int main(){
    scanf("%d",&t);
    for (int ca=1;ca<=t;++ca){
        ans=INF;
        scanf("%d",&n);
        int test=0,sum=0;
        for (int i=0;i<n;++i){
            int x;
            scanf("%d",&x);
            if (x<ans) ans=x;
            test^=x; sum+=x;
        }
        if (test == 0) printf("Case #%d: %d\n",ca,sum-ans);
        else printf("Case #%d: NO\n",ca);
    }
    return 0;
}
