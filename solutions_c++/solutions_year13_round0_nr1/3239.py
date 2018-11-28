#include<stdio.h>
int t;
char x[10][10];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    int i,j,k,cx,co,cb,status;
    for(k=1;k<=t;k++){
        for(i=0;i<4;i++){
            scanf("%s",x[i]);
        }
        status=0;
        for(i=0;i<4;i++){
            cx=0;
            co=0;
            cb=0;
            for(j=0;j<4;j++){
                if(x[i][j]=='O'||x[i][j]=='T') co++;
                if(x[i][j]=='X'||x[i][j]=='T') cx++;
                if(x[i][j]=='.') cb++;
            }
            if(cb!=0) status=3;
            if(co==4) status=1;
            if(cx==4) status=2;
            //printf("> %d %d %d %d\n",cx,co,cb,status);
            if(status==1||status==2) break;
        }
        if(!status||status==3){
            for(j=0;j<4;j++){
                cx=0;
                co=0;
                cb=0;
                for(i=0;i<4;i++){
                    if(x[i][j]=='O'||x[i][j]=='T') co++;
                    if(x[i][j]=='X'||x[i][j]=='T') cx++;
                    if(x[i][j]=='.') cb++;
                }
                if(cb!=0) status=3;
                if(co==4) status=1;
                if(cx==4) status=2;
            //printf("> %d %d %d %d\n",cx,co,cb,status);
            if(status==1||status==2) break;
            }
            if(!status||status==3){
                cx=0;
                co=0;
                for(i=0;i<4;i++){
                    if(x[i][i]=='O'||x[i][i]=='T') co++;
                    if(x[i][i]=='X'||x[i][i]=='T') cx++;
                }
                if(co==4) status=1;
                if(cx==4) status=2;
            //printf("> %d %d %d %d\n",cx,co,cb,status);
                if(!status||status==3){
                    cx=0;
                    co=0;
                    for(i=0;i<4;i++){
                        if(x[i][3-i]=='O'||x[i][3-i]=='T') co++;
                        if(x[i][3-i]=='X'||x[i][3-i]=='T') cx++;
                    }
                    if(co==4) status=1;
                    if(cx==4) status=2;
            //printf("> %d %d %d %d\n",cx,co,cb,status);
                }
            }
        }
        printf("Case #%d: ",k);
        //printf("%d\n",status);
        if(status==0) printf("Draw\n");
        else if(status==1) printf("O won\n");
        else if(status==2) printf("X won\n");
        else if(status==3) printf("Game has not completed\n");
    }
    
    
    
    
    scanf(" ");
    return 0;
}
