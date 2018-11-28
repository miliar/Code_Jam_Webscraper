#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 330;

bool has[MAXN][MAXN];

int main(){
    int t;
    scanf("%d",&t);
    
    for(int lp=1;lp<=t;++lp){
        for(int i=0;i<MAXN;++i){
            for(int j=0;j<MAXN;++j){
                has[i][j] = false;
            }
        }
        int r;
        scanf("%d",&r);
        for(int i=0;i<r;++i){
            int lx,ly,ux,uy;
            int hlx,hly,hux,huy;
            scanf("%d %d %d %d",&hlx,&hly,&hux,&huy);
            lx = min(hlx,hux);
            ux = max(hlx,hux);
            ly = min(hly,huy);
            uy = max(hly,huy);
            
            for(int x=lx;x<=ux;++x){
                for(int y=ly;y<=uy;++y){
                    has[x][y] = true;
                }
            }
            
        }
        
        int ret;
        for(ret=1;;++ret){
            bool fora = true;
            for(int x=MAXN-1;x>=1;--x){
                for(int y=MAXN-1;y>=1;--y){
                    if(has[x][y]){
                        has[x][y] = has[x-1][y] || has[x][y-1];
                        if(has[x][y]){
                            fora = false;
                        }
                    }
                    else{
                        has[x][y] = has[x-1][y] && has[x][y-1];
                    }
                }
            }
            for(int i=0;i<MAXN;++i){
                has[i][0] = false;
                has[0][i] = false;
            }
            
            if(fora){
                break;
            }
        }
        
        printf("Case #%d: %d\n",lp,ret);
    }
    
    return 0;
}