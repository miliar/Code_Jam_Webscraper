#include<cstdio>
#include<cstring>

int a[1005];
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int cas,r=1;
    scanf("%d",&cas);
    while(cas--){
        int n;
        scanf("%d",&n);
        int res=0;
        for(int i=1; i<=n; i++) {
            scanf("%d",&a[i]);
            if(a[i]!=i) res++;
        }
        printf("Case #%d: %d.000000\n",r++,res);
    }
}
