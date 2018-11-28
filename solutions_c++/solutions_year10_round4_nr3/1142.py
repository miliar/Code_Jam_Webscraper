/*
    2010  Round 2 -
    Bacteria
    small
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

    int C, R, x1, y1, x2, y2;
    int map[101][101], alive;

int main(){
    scanf("%d",&C);
    for(int z=1;z<=C;++z){
        scanf("%d",&R);
        memset(map,0,sizeof(map));
        alive = 0;
        for(int i=0;i<R;++i){
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            for(int j=x1;j<=x2;++j)
                for(int k=y1;k<=y2;++k){
                    if(map[j][k]==0){
                        ++alive;
                        //printf("c %d %d\n",,j);
                    }
                    map[j][k] = 1;
                }
        }
        int ans = 0;
        while(alive>0){
            for(int i=100;i>=1;--i){
                for(int j=100;j>=1;--j){
                    if(map[i-1][j]==1 && map[i][j-1]==1){
                        if(map[i][j]==0){
                            ++alive;
                        }
                        map[i][j] = 1;
                    }
                    if(map[i-1][j]==0 && map[i][j-1]==0){
                        if(map[i][j]==1){
                            --alive;
                        }
                        map[i][j] = 0;
                    }
                }
            }
            ++ans;
        }
        printf("Case #%d: %d\n",z,ans);
    }
}
