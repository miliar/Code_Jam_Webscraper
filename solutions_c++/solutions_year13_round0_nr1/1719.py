#include<iostream>
#include<vector>
#include<string.h>
#include<set>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
typedef long long int ll;
char ar[4][4];
bool chck(char c)
{
    bool ok;
    int i,j;
    // Row chck
    for(i=0;i<4;i++)
    {
        ok=true;
        for(j=0;j<4;j++)
        {
            if(ar[i][j]==c || ar[i][j]=='T');
            else
            {
                ok=false;
                break;
            }
        }
        if(ok)
        return true;
    }
    //Col chck
    for(i=0;i<4;i++)
    {
        ok=true;
        for(j=0;j<4;j++)
        {
            if(ar[j][i]==c || ar[j][i]=='T');
            else
            {
                ok=false;
                break;
            }
        }
        if(ok)
        return true;
    }
    //Diag Chck
    ok=true;
    for(i=0;i<4;i++)
    {
        if(ar[i][i]==c || ar[i][i]=='T');
        else
        {
            ok=false;
            break;
        }
    }
    if(ok==true)
    return true;
    ok=true;
    int co=3,r=0;
    for(i=0;i<4;i++)
    {
        if(ar[r][co]==c || ar[r][co]=='T');
        else
        {
            ok=false;
            break;
        }
        r++;
        co--;
    }
    if(ok==true)
    return true;

    return false;

}
int main()
{
   int t,i,j,n,test;
   freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);
   cin>>t;
   for(test=1;test<=t;test++)
   {
       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           cin>>ar[i][j];
       }
       bool xb=chck('X');
       bool xo=chck('O');
       if(xb)
       {
           printf("Case #%d: X won\n",test);
           continue;
       }
       else if(xo)
       {
           printf("Case #%d: O won\n",test);
           continue;
       }
       else
       {
           bool left=false;
           for(i=0;i<4;i++)
           {
               for(j=0;j<4;j++)
               {
                   if(ar[i][j]=='.')
                   {
                       left=true;
                       break;
                   }
               }
           }
           if(left)
           {
               printf("Case #%d: Game has not completed\n",test);
           }
           else
           {
               printf("Case #%d: Draw\n",test);
           }
       }
   }


   return 0;
}
