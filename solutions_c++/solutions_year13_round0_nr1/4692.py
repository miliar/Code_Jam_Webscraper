#include<stdio.h>
char s[4][4];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        int sp=0,ans=0;
        for(int i=0;i<4;i++){
            scanf("%s",s[i]);
            for(int j=0;j<4;j++)if(s[i][j]=='.')sp++;
        }
        int cnto,cntx,cntt;
        for(int i=0;i<4;i++){
            cnto=0,cntx=0,cntt=0;
            for(int j=0;j<4;j++){
                switch(s[i][j]){
                    case'O':cnto++;break;
                    case'X':cntx++;break;
                    case'T':cntt++;break;
                }
            }
            if(cnto==4||cnto==3&&cntt==1){
                ans=1;break;
            }
            if(cntx==4||cntx==3&&cntt==1){
                ans=2;break;
            }
            cnto=0,cntx=0,cntt=0;
            for(int j=0;j<4;j++){
                switch(s[j][i]){
                    case'O':cnto++;break;
                    case'X':cntx++;break;
                    case'T':cntt++;break;
                }
            }
            if(cnto==4||cnto==3&&cntt==1){
                ans=1;break;
            }
            if(cntx==4||cntx==3&&cntt==1){
                ans=2;break;
            }
        }
        if(!ans){
            cnto=0,cntx=0,cntt=0;
            for(int i=0;i<4;i++){
                switch(s[i][i]){
                    case'O':cnto++;break;
                    case'X':cntx++;break;
                    case'T':cntt++;break;
                }
            }
            if(cnto==4||cnto==3&&cntt==1)ans=1;
            else if(cntx==4||cntx==3&&cntt==1)ans=2;
        }
        if(!ans){
            cnto=0,cntx=0,cntt=0;
            for(int i=0;i<4;i++){
                switch(s[i][3-i]){
                    case'O':cnto++;break;
                    case'X':cntx++;break;
                    case'T':cntt++;break;
                }
            }
            if(cnto==4||cnto==3&&cntt==1)ans=1;
            else if(cntx==4||cntx==3&&cntt==1)ans=2;
        }
        if(!ans)ans=sp?4:3;
        printf("Case #%d: ",t);
        switch(ans){
            case 1:puts("O won");break;
            case 2:puts("X won");break;
            case 3:puts("Draw");break;
            case 4:puts("Game has not completed");break;
        }
    }
    return 0;
}
