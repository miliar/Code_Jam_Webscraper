#include<cstdio>
#include<cstring>
const int N=10;
char str[N][N];
bool check(char ch){
    //行
    int i,j;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(str[i][j]!=ch&&str[i][j]!='T') break;
        }
        if(j>=4) return true;
        for(j=0;j<4;j++){
            if(str[j][i]!=ch&&str[j][i]!='T') break;
        }
        if(j>=4) return true;
    }
    for(i=0;i<4;i++)
    if(str[i][i]!=ch&&str[i][i]!='T') break;
    if(i>=4) return true;

    for(i=0;i<4;i++)
    if(str[i][3-i]!=ch&&str[i][3-i]!='T') break;
    if(i>=4) return true;

    return false;

}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.cpp","w",stdout);
    int T,n,m,i,j,k,cas=1;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",cas++);
        bool over=true;
        for(i=0;i<4;i++){
             scanf("%s",str[i]);
             for(j=0;j<4;j++)
             if(str[i][j]=='.') over=false;
        }
        if(check('X')) puts("X won");
        else if(check('O')) puts("O won");
        else if(over) puts("Draw");
        else puts("Game has not completed");
    }
    return 0;
}
