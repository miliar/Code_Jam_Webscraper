#include <cstdio>
#include <cstring>

int g[1001];
int u[1001];
int next[1001];
long long total[1001];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q,n,i,j;
    long long r,k;
    scanf("%d",&q);
    for(int test=1;test<=q;test++){
        scanf("%lld%lld%d",&r,&k,&n);
        for(i=0;i<n;i++)scanf("%d",&g[i]);
        for(i=0;i<1001;i++)u[i]=0;
        for(i=0;i<1001;i++)next[i]=0;
        u[0]=1;
        total[0]=0;
        int c=0;
        int subt;
        int per;
        long long ans=0;
        while(1){
            subt=0;
            for(j=0;j<n && subt+g[(c+j)%n]<=k;j++)subt+=g[(c+j)%n];
            total[c]=subt;
            if(u[(c+j)%n]!=0){
                next[c]=(c+j)%n;
                break;
            }
            u[(c+j)%n]=u[c]+1;
            next[c]=(c+j)%n;
            c=(c+j)%n;
        }
        c=0;
        for(i=0;i<r;i++){
            ans+=total[c];
            c=next[c];
        }
//        long long ans2=0;
//        c=0;
//        for(i=0;i<r;i++){
//            subt=0;
//            for(j=0;j<n && subt+g[(c+j)%n]<=k;j++)subt+=g[(c+j)%n];
//            c=(c+j)%n;
//            ans2+=subt;
//        }
//        if(ans!=ans2)printf("FAIL! ans2=%lld\n",ans2);
        printf("Case #%d: %lld\n",test,ans);
    }

    return 0;
}
