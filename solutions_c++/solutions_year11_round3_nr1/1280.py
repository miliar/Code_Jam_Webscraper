#include <stdio.h>

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, R, C, i, j;
    scanf("%d", &T);
    for(int k=1; k<=T; k++){
        scanf("%d %d", &R, &C);
        char tile[60][60];
        for(i=0; i<R; i++)
            scanf("%s", tile[i]);
        printf("Case #%d:\n", k);
        for(i=0; i<R; i++){
            for(j=0; j<C; j++){
                if(tile[i][j]=='#' && (i==R-1 || j==C-1)) break;
                if(tile[i][j]=='#' && tile[i+1][j]=='#' && tile[i][j+1]=='#' && tile[i+1][j+1]=='#'){
                    tile[i][j] = '/';
                    tile[i+1][j+1] = '/';
                    tile[i+1][j] = '\\';
                    tile[i][j+1] = '\\';
                }else if(tile[i][j]=='#') break;
            }
            if(j<C){
                printf("Impossible\n");
                break;
            }
        }
        if(i==R){
            for(i=0; i<R; i++){
                for(j=0; j<C; j++) printf("%c", tile[i][j]);
                printf("\n");
            }
        }
    }
    return 0;
}
