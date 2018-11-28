#include <stdio.h>
char mat[100][100];
int row,col;
void resuelve(){
    scanf("%d %d ",&row,&col);
    for(int i=0;i<row;i++){
        scanf(" %s",mat[i]);
    }
    for(int i=0;i<(row-1);i++){
        for(int j=0;j<(col-1);j++){
            if( mat[i][j]=='#'){
                if( mat[i][j] != '#' ||
                    mat[i+1][j] != '#' ||
                    mat[i][j+1] != '#' ||
                    mat[i+1][j+1] != '#'){
                    printf("Impossible\n");
                    return;
                }
                mat[i][j] = '/';
                mat[i+1][j] = '\\';
                mat[i][j+1] = '\\';
                mat[i+1][j+1] = '/';
                    
            }
        }
    }
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            if( mat[i][j] == '#'){
                printf("Impossible\n");
                return;                
            }
        }
    }
    for(int i=0;i<row;i++){
        printf("%s\n",mat[i]);
    }
}
int main(){
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d:\n",i);
        resuelve();
    }
    return 0;
}
