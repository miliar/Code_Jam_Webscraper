#include<stdio.h>

int main(){
    int T,cnt ,r, c, i ,j;
    char map[51][51], used[51][51];
    cnt = 0;
    scanf("%d",&T);
    while(T--){
        cnt++;
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++)
            scanf("%s",map[i]);
        for(i=0;i<r;i++)
            for(j=0;j<c;j++){
                if(map[i][j] == '#'){
                    if(map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#' && j+1 < c && i+1 < r){
                        map[i][j] = '/', map[i][j+1] = '\\', map[i+1][j] = '\\', map[i+1][j+1] = '/';
                    }
                }
            }
        int m = 0;
        printf("Case #%d:\n",cnt);
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                if(map[i][j] == '#') m = 1;
        if(m) printf("Impossible\n");
        else{
            for(i=0;i<r;i++){
                printf("%s",map[i]);
                printf("\n");
            }
        }
    }
    return 0;
}
