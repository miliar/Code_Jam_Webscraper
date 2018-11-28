#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t;


char s[5][5];


bool dot()
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(s[i][j]=='.')
                return 1;
        }
    }
    return 0;
}

bool solve(int x)
{
    int i,j;
    char col;
    if(x==1)
        col='O';
    else
        col='X';
    for(i=0;i<4;i++)
    {
        int flag1=0;
        int flag2=0;
        for(j=0;j<4;j++)
        {
            if(s[i][j]==col||s[i][j]=='T')
                flag1++;
            if(s[j][i]==col||s[j][i]=='T')
                flag2++;
        }
        if(flag1==4||flag2==4)
            return 1;
    }
    int flag3=0;
    int flag4=0;
    
    for(i=0;i<4;i++)
    {
        if(s[i][i]==col||s[i][i]=='T')
            flag3++;
        if(s[i][3-i]==col||s[i][3-i]=='T')
            flag4++;
        if(flag3==4||flag4==4)
            return 1;
    }
    return 0;
}

//O-->1  X-->-1

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_out1.txt","w",stdout);
    
    int i,j;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        printf("Case #%d: ",tt);
        for(i=0;i<4;i++){
            scanf("%s",s[i]);    
        }
        int flag=0;
        if(solve(1)==1)
            flag=1;
        if(solve(-1)==1)
            flag=-1;
        if(flag==1)
            printf("O won\n");
        if(flag==-1)
            printf("X won\n");
        if(flag==0)
        {
            if(dot())
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }
    }
    //system("pause");
    return 0;
}
