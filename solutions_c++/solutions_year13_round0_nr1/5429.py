#include<cstdio>
#include<cstring>
using namespace std;
char ma[5][5];
int flag;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("text.out","w",stdout);
    int T,ca=1;
    int i,j;
    int outcome;
    char x;
    scanf("%d",&T);
    while(T--)
    {
        for(i=0;i<4;i++)
        scanf("%s",ma[i]);
        flag=0;
        outcome=0;
        for(i=0;i<4;i++){
            if(i==0){
                    for(j=0;j<4;j++)
                    if(ma[i+j][j]!='T')break;
                    x=ma[i][j];
                    if(ma[i][j]=='.')flag=1;
                    for(;j<4;j++)
                    if(x!=ma[i+j][j]&&ma[i+j][j]!='T')break;
                    if(j==4){
                        if(x=='O')outcome=1;
                        else if(x=='X')outcome=2;
                    }
            }
            if(i==3){
                    for(j=0;j<4;j++)
                    if(ma[i-j][j]!='T')break;
                    x=ma[i-j][j];
                    if(x=='.')flag=1;
                    for(;j<4;j++)
                    if(x!=ma[i-j][j]&&ma[i-j][j]!='T')break;
                    if(j==4){
                        if(x=='O')outcome=1;
                        else if(x=='X')outcome=2;
                    }
            }
            for(j=0;j<4;j++)
            if(ma[i][j]!='T')break;
            x=ma[i][j];
            if(x=='.'){flag=1;continue;}
            for(;j<4;j++)
            if(x!=ma[i][j]&&ma[i][j]!='T')break;
            if(j==4){
                if(x=='O')outcome=1;
                else if(x=='X')outcome=2;
                break;
            }
        }
        for(j=0;j<4;j++){
            for(i=0;i<4;i++)
            if(ma[i][j]!='T')break;
            x=ma[i][j];
            if(x=='.'){flag=1;continue;}
            for(i++;i<4;i++)
            if(x!=ma[i][j]&&ma[i][j]!='T')break;
            if(i==4){
                if(x=='O')outcome=1;
                else if(x=='X')outcome=2;
                break;
            }
        }
        printf("Case #%d: ",ca++);
        if(outcome==0){
            if(flag)printf("Game has not completed\n");
            else puts("Draw");
        }
        else if(outcome==1)puts("O won");
        else if(outcome==2)puts("X won");
    }
    return 0;
}
