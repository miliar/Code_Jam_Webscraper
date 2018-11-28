#include <cstdio>

int n,m,A;
int a1,b1,a2,b2;

bool sol(){
    int i,j;
    for(a1=0;a1<=n;a1++){
        for(b1=0;b1<=m;b1++){
            for(a2=0;a2<=n;a2++){
                for(b2=0;b2<=m;b2++){
                    if(a1*b2-a2*b1==A||a2*b1-a1*b2==A) return 1;
                }
            }
        }
    }
    return 0;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d%d%d",&n,&m,&A);
        if(sol()){
            printf("Case #%d: 0 0 %d %d %d %d\n",ic,a1,b1,a2,b2);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",ic);
        }
    }
    return 0;
}
