#include <cstdio>
using namespace std;

int tot,n,m,a;

int main(){
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%d%d",&n,&m,&a);
        bool t=false;
        printf("Case #%d: ",cases+1);
        for (int x1=0;x1<=n;++x1){
            for (int y1=0;y1<=m;++y1){
                for (int x2=0;x2<=n;++x2){
                    for (int y2=0;y2<=m;++y2)
                        if (x1*y2-x2*y1==a){
                            printf("0 0 %d %d %d %d\n",x1,y1,x2,y2);
                            t=true;
                            break;
                        }
                    if (t) break;
                }
                if (t) break;
            }
            if (t) break;
        }
        if (t) continue;
        printf("IMPOSSIBLE\n");
    }
    return 0;
}
