#include<cstdio>

char s[10][10];

int main(){
    int cas,tt=0,i,j,sum;
    bool flag,owin,xwin;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    while(cas--){
        for(i=1;i<=4;++i)scanf("%s",s[i]+1);
        //for(i=1;i<=4;++i)puts(s[i]+1);
        flag=0;
        for(i=1;i<=4;++i)
            for(j=1;j<=4;++j)if(s[i][j]=='.')flag=1;
        owin=xwin=0;
        for(i=1;i<=4;++i){
            sum=0;
            for(j=1;j<=4;++j)if(s[i][j]=='O'||s[i][j]=='T')++sum;
            if(sum==4)owin=1;
        }
        for(j=1;j<=4;++j){
            sum=0;
            for(i=1;i<=4;++i)if(s[i][j]=='O'||s[i][j]=='T')++sum;
            if(sum==4)owin=1;
        }
        sum=0;
        for(i=1;i<=4;++i)if(s[i][i]=='O'||s[i][i]=='T')++sum;
        if(sum==4)owin=1;
        sum=0;
        for(i=1;i<=4;++i)if(s[i][5-i]=='O'||s[i][5-i]=='T')++sum;
        if(sum==4)owin=1;
        //
        for(i=1;i<=4;++i){
            sum=0;
            for(j=1;j<=4;++j)if(s[i][j]=='X'||s[i][j]=='T')++sum;
            if(sum==4)xwin=1;
        }
        for(j=1;j<=4;++j){
            sum=0;
            for(i=1;i<=4;++i)if(s[i][j]=='X'||s[i][j]=='T')++sum;
            if(sum==4)xwin=1;
        }
        sum=0;
        for(i=1;i<=4;++i)if(s[i][i]=='X'||s[i][i]=='T')++sum;
        if(sum==4)xwin=1;
        sum=0;
        for(i=1;i<=4;++i)if(s[i][5-i]=='X'||s[i][5-i]=='T')++sum;
        if(sum==4)xwin=1;
        printf("Case #%d: ",++tt);
        if(owin)puts("O won");
        else if (xwin)puts("X won");
        else if (flag)puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}
