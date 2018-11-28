#include <iostream>
using namespace std;

int T,R,ans,x1,x2,y1,y2,tmp;
bool grid[2][150][150],cur,pre;

void swap(int x){
    if(x == 1){
        x1 = (x1^x2);
        x2 = (x1^x2);
        x1 = (x1^x2);
    }
    else{
        y1 = (y1^y2);
        y2 = (y1^y2);
        y1 = (y1^y2);
    }
}

inline bool grow(int i, int j){
    return (grid[pre][i-1][j] && grid[pre][i][j-1]);
}

inline bool die(int i, int j){
    return (!grid[pre][i-1][j] && !grid[pre][i][j-1]);
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    scanf("%d", &T);
    for(int cn = 1;cn<=T;++cn){
        memset(grid, 0, sizeof(grid));
        ans = 0;
        cur = 0; pre = 1;
        scanf("%d", &R);
        for(int i=0;i<R;++i){
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            if(x1>x2) swap(1);
            if(y1>y2) swap(2);
            for(int j=x1;j<=x2;++j)
                for(int k=y1;k<=y2;++k) grid[pre][j][k] = 1;
        }
        while(1){
            memset(grid[cur],0,sizeof(grid[cur]));
            tmp = 0;
            for(int i=1;i<=100;++i)
                for(int j=1;j<=100;++j) tmp|=grid[pre][i][j];
            if(!tmp) break;
            ++ans;
            for(int i=1;i<=100;++i)
                for(int j=1;j<=100;++j)
                    if(!grid[pre][i][j]){
                        if(grow(i,j)) grid[cur][i][j] = 1;
                    }
                    else if(grid[pre][i][j]){
                        if(!die(i,j)) grid[cur][i][j] = 1;
                    }
            pre = !pre; cur = !cur;
        }
        printf("Case #%d: %d\n", cn, ans);
    }   
 //   system("pause");
}
            
            
            
            
            
            
            
            
            
            
            
            
            
