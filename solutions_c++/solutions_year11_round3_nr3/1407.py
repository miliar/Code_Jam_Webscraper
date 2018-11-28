#include<cstdio>
using namespace std;
int n, l, h, a[105];
bool check(int k){
    for(int i=0;i<n;i++){
        if(k%a[i] && a[i]%k) return false;
    }
    return true;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        printf("Case #%d: ",cas);
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        int ans = 0;
        for(int i=l;i<=h;i++){
            if(check(i)){ans=i;break;}
        }
        if(ans) printf("%d\n",ans);
        else puts("NO");
    }
}
