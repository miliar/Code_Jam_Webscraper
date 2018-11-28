#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
char a[5][5];
int main()
{
 int t,i,j,cas;
 bool xw,ow,flag;
 scanf("%d",&t);
 for(cas=1;cas<=t;cas++)
 {
           flag=0;xw=0;ow=0;
        for(i=0;i<4;i++)
        {
                        cin>>a[i];
                        if(flag!=1 && (a[i][0]=='.' || a[i][1]=='.' || a[i][2]=='.' || a[i][3]=='.'))
                        flag=1;
        } 
        for(i=0;i<4;i++)
        if((a[i][0]=='X' || a[i][0]=='T') && (a[i][1]=='X'|| a[i][1]=='T') && (a[i][2]=='X' || a[i][2]=='T') && (a[i][3]=='X'|| a[i][3]=='T'))
        xw=1;
        if(!xw && !ow)
        for(i=0;i<4;i++)
        if((a[i][0]=='O' || a[i][0]=='T') && (a[i][1]=='O'|| a[i][1]=='T') && (a[i][2]=='O' || a[i][2]=='T') && (a[i][3]=='O'|| a[i][3]=='T'))
        ow=1;
        if(!xw && !ow)
        for(i=0;i<4;i++)
        if((a[0][i]=='X' || a[0][i]=='T') && (a[1][i]=='X'|| a[1][i]=='T') && (a[2][i]=='X' || a[2][i]=='T') && (a[3][i]=='X'|| a[3][i]=='T'))
        xw=1;
        if(!xw && !ow)
        for(i=0;i<4;i++)
        if((a[0][i]=='O' || a[0][i]=='T') && (a[1][i]=='O'|| a[1][i]=='T') && (a[2][i]=='O' || a[2][i]=='T') && (a[3][i]=='O'|| a[3][i]=='T'))
        ow=1;
        if(!xw && !ow)
        if((a[0][0]=='X' || a[0][0]=='T') && (a[1][1]=='X'|| a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X'|| a[3][3]=='T'))
        xw=1;
        if(!xw && !ow)
        if((a[0][0]=='O' || a[0][0]=='T') && (a[1][1]=='O'|| a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O'|| a[3][3]=='T'))
        ow=1;
        if(!xw && !ow)
        if((a[0][3]=='X' || a[0][3]=='T') && (a[1][2]=='X'|| a[1][2]=='T') && (a[2][1]=='X' || a[2][1]=='T') && (a[3][0]=='X'|| a[3][0]=='T'))
        xw=1;
        if(!xw && !ow)
        if((a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O'|| a[1][2]=='T') && (a[2][1]=='O' || a[2][1]=='T') && (a[3][0]=='O'|| a[3][0]=='T'))
        ow=1;
        if(flag==0 && xw==0 && ow==0)
        printf("Case #%d: Draw\n",cas);
        else if(xw==1)
        printf("Case #%d: X won\n",cas);
        else if(ow==1)
        printf("Case #%d: O won\n",cas);
        else if(flag==1 && xw==0 && ow==0)
        printf("Case #%d: Game has not completed\n",cas);
 }
        
return 0;
}
