#include <iostream>
using namespace std;
int values[100];
int ans[256][101][3];
int D,I,M,N;
int get(int x, int y, int allow) {
    if (ans[x][y][allow]!=-1) return ans[x][y][allow];
    if (y==N) return ans[x][y][allow]=0;
    
    // case 1: remove this pixel
    
    int poss;
    
    poss = D + get(x,y+1,allow);
    if (ans[x][y][allow]==-1 || poss<ans[x][y][allow]) ans[x][y][allow]=poss;
    
    // case 2: change this pixel to z
    for (int z=0; z<256; z++) {
        if (abs(z-x)>M) continue;
        poss = abs(z-values[y]) + get(z,y+1,0);
        if (ans[x][y][allow]==-1 || poss<ans[x][y][allow]) ans[x][y][allow]=poss;
    }
    
    // case 3: insert a new pixel of x+M
    
    if ((allow==0 || allow==1) && x<255) {
        poss = I + get(min(255,x+M),y,1);
        if (ans[x][y][allow]==-1 || poss<ans[x][y][allow]) ans[x][y][allow]=poss;
    }
    
    // case 4: insert a new pixel of x-M
    
    if ((allow==0 || allow==2) && x>0) {
        poss = I + get(max(0,x-M),y,2);
        if (ans[x][y][allow]==-1 || poss<ans[x][y][allow]) ans[x][y][allow]=poss;
    }
    
    return ans[x][y][allow];
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        scanf("%d %d %d %d",&D,&I,&M,&N);
        for (int i=0; i<N; i++) {
            scanf("%d",&values[i]);
        }
        memset(ans,-1,256*101*3*sizeof(int));
        
        int best = -1;
        for (int i=0; i<256; i++) {
            int here = get(i,0,0);
            if (best==-1 || here<best) {
                best = here;
            }
        }
        printf("%d\n",best);
    }
}
