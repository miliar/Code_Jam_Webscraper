#include<stdio.h>
#include<string.h>
char s[10][10];
int main(){
    int t,k,i,j,O,X,T,S;
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    while(scanf("%d",&t)!=EOF){
        for(k=1;k<=t;k++){
            printf("Case #%d: ",k);
            O=0,X=0,T=0,S=0;
            memset(s,0,sizeof(s));
            for(i=0;i<4;i++){
                scanf("%s",s[i]);
            }

            for(i=0;i<4;i++){
                O=0,X=0,T=0;
                for(j=0;j<4;j++){
                    if(s[i][j]=='.') S+=1;
                    if(s[i][j]=='X') X+=1;
                    if(s[i][j]=='O') O+=1;
                    if(s[i][j]=='T') T+=1;
                }
                if(O+T==4){
                    puts("O won");
                    goto go;
                }
                if(X+T==4){
                    puts("X won");
                    goto go;
                }
            }
            for(i=0;i<4;i++){
                O=0,X=0,T=0;
                for(j=0;j<4;j++){
                    if(s[j][i]=='.') S+=1;
                    if(s[j][i]=='X') X+=1;
                    if(s[j][i]=='O') O+=1;
                    if(s[j][i]=='T') T+=1;
                }
                if(O+T==4){
                    puts("O won");
                    goto go;
                }
                if(X+T==4){
                    puts("X won");
                    goto go;
                }
            }
            for(i=1;i<2;i++){
                O=0,X=0,T=0;
                for(j=0;j<4;j++){
                    if(s[j][j]=='.') S+=1;
                    if(s[j][j]=='X') X+=1;
                    if(s[j][j]=='O') O+=1;
                    if(s[j][j]=='T') T+=1;
                }
                if(O+T==4){
                    puts("O won");
                    goto go;
                }
                if(X+T==4){
                    puts("X won");
                    goto go;
                }
            }
            for(i=1;i<2;i++){
                O=0,X=0,T=0;
                for(j=0;j<4;j++){
                    if(s[j][3-j]=='.') S+=1;
                    if(s[j][3-j]=='X') X+=1;
                    if(s[j][3-j]=='O') O+=1;
                    if(s[j][3-j]=='T') T+=1;
                }
                if(O+T==4){
                    puts("O won");
                    goto go;
                }
                if(X+T==4){
                    puts("X won");
                    goto go;
                }
            }
            if(S==0)
                puts("Draw");
            else
                puts("Game has not completed");
            go:;
        }
    }
}
