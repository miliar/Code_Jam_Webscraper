#include<cstdio>

int main(){
        int t;
        scanf("%d",&t);
        for (int x=1;x<=t;++x){
                int n,k;
                scanf("%d%d",&n,&k);
                int MOD=(1<<n);
                if ((k%MOD)==(MOD-1)) printf("Case #%d: ON\n",x);
                else printf("Case #%d: OFF\n",x);
        }
        return 0;
}
