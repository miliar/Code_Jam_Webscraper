#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>

using namespace std;
char a[4][4];
int main()
{
    int i,j,flag,t,k,or1,od,oc,xd,xc,xr;
    scanf("%d",&t);
    k=1;
    while(k<=t)
    {
         scanf("%s",a[0]);
         scanf("%s",a[1]);
         scanf("%s",a[2]);
         scanf("%s",a[3]);
         flag=0;
         for(i=0;i<4;i++)
         {
                or1=xr=oc=xc=0;
                for(j=0;j<4;j++)
                {
                      if(a[i][j]=='O')
                      or1++;
                      else if(a[i][j]=='X')
                      xr++;
                      else if(a[i][j]=='T'){or1++;xr++;}
                      if(a[j][i]=='O')
                      oc++;
                      else if(a[j][i]=='X')
                      xc++;
                      else if(a[j][i]=='T'){oc++;xc++;}
                }
                if(or1==4||oc==4)flag=1;
                else if(xr==4||xc==4)flag=2;
         }      
         if ((a[0][0] == 'X' || a[0][0] == 'T') && (a[1][1] == 'X' || a[1][1] == 'T')&&(a[2][2] == 'X' || a[2][2] == 'T') && (a[3][3] == 'X' || a[3][3] == 'T'))
         flag=2;
         else if ((a[0][0] == 'O' || a[0][0] == 'T') && (a[1][1] == 'O' || a[1][1] == 'T')&&(a[2][2] == 'O' || a[2][2] == 'T') && (a[3][3] == 'O' || a[3][3] == 'T'))
         flag=1;
         //if(or1==4||oc==4)flag=1;
         //else if(xr==4||xc==4)flag=2;
         if ((a[0][3] == 'X' || a[0][3] == 'T') && (a[1][2] == 'X' || a[1][2] == 'T')&&(a[2][1] == 'X' || a[2][1] == 'T') && (a[3][0] == 'X' || a[3][0] == 'T'))
         flag=2;
         else if ((a[0][3] == 'O' || a[0][3] == 'T') && (a[1][2] == 'O' || a[1][2] == 'T')&&(a[2][1] == 'O' || a[2][1] == 'T') && (a[3][0] == 'O' || a[3][0] == 'T'))
         flag=1;
         if(!flag)
         for(i=0;i<4;i++)
         for(j=0;j<4;j++)
         if(a[i][j]=='.')
         {flag=3;break;}
         if(flag==1)
         printf("Case #%d: O won\n",k);
         else if(flag==2)
         printf("Case #%d: X won\n",k);
         else if(flag==0)
         printf("Case #%d: Draw\n",k);
         else if(flag==3)
         printf("Case #%d: Game has not completed\n",k);
         k++;
    }
    return 0;
}
