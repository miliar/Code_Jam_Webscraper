#include<stdio.h>

int t,r,c;

char map[100][100];

bool solve(){
     for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(map[i][j]=='#'){
                    if(i+1<r&&j+1<c){
                        if((map[i][j+1]=='#')&&(map[i+1][j]=='#')&&(map[i+1][j+1]=='#')){
                            map[i][j]='/';
                            map[i][j+1]='\\';
                            map[i+1][j]='\\';
                            map[i+1][j+1]='/';
                        }else{
                            return false;
                        }
                    }else{
                        return false;
                    }
                }
            }
        }
        return true;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(int o=1;o<=t;o++){
        scanf("%d %d",&r,&c);
        for(int i=0;i<r;i++){
            scanf("%s",map[i]);
        }

        printf("Case #%d:\n",o);
        if(solve()){
            for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    printf("%c",map[i][j]);
                }
                printf("\n");
            }
        }else{
            printf("Impossible\n");
        }
    }
    return 0;
}
