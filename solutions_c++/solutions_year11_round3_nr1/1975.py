#include <stdio.h>
char map[100][100];
int r,c;
int check(int i,int j){
    if(i<r-1&&j<c-1){
        if(map[i+1][j]=='#'&&map[i+1][j+1]=='#'&&map[i][j+1]=='#') return 1;
        return 0;
    }else return 0;
}
int scan(){
int i,j;
             for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(map[i][j]=='#'){
                    if(check(i,j)==0){
                    return 0;
                    } else{
                           map[i][j]='/';
                    map[i+1][j]='\\';
                    map[i][j+1]='\\';
                    map[i+1][j+1]='/';
             
                    }
                }
            }
        }

    return 1;
}
main(){
       freopen("Out.txt","w",stdout);
       int T,i,TC=1;
    scanf("%d",&T);   
    while(T--){
        scanf("%d%d",&r,&c);
        for(i=0;i<r;i++) scanf("%s",map[i]);
        printf("Case #%d:\n",TC++);
        if(scan()){
            for(i=0;i<r;i++) printf("%s\n",map[i]);
            
        }else printf("Impossible\n");
    }
    return 0;
}
