#include<cstdio>
int n,ac,x,t;
int main(){
    scanf("%d",&t);
    for (int z=1; z<=t; z++){
        scanf("%d",&n);
        ac=0;
        for (int i=1; i<=n; i++){
            scanf("%d",&x);
            if (x^i)++ac;
        }
        printf("Case #%d: %d.000000\n",z,ac);
    }
    return 0;    
}
