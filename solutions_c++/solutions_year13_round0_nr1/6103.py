#include<iostream>
#include<cstdio>
 
 
using namespace std;
 
int main()
{
    int t,i,j,k;
    char ch;
    int gintix=0,gintio=0,gintit=0,gintie=0,symbol=0,gintiie=0;
    scanf("%d",&t);
    scanf("%c",&ch);
    for(i=1;i<=t;i++)
    {
        symbol=0;
        gintix=0,gintio=0,gintit=0,gintie=0,gintiie=0;
        char c[6][6];
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                scanf("%c",&c[j][k]);
                if(c[j][k]=='.')
                gintiie++;
            }
            scanf("%c",&ch);
        }
        for(j=0;j<4;j++)
        {
            gintix=0,gintio=0,gintit=0,gintie=0;
            for(k=0;k<4;k++)
            {
                if(c[j][k]=='.')
                gintie++;
                else if(c[j][k]=='X')
                gintix++;
                else if(c[j][k]=='O')
                gintio++;
                else if(c[j][k]=='T')
                gintit++;
            }
            if(gintix==4 || (gintit+gintix)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(gintio==4 || (gintit+gintio)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
        }
        
        for(j=0;j<4;j++)
        {
            gintix=0,gintio=0,gintit=0,gintie=0;
            for(k=0;k<4;k++)
            {
                if(c[k][j]=='.')
                gintie++;
                else if(c[k][j]=='X')
                gintix++;
                else if(c[k][j]=='O')
                gintio++;
                else if(c[k][j]=='T')
                gintit++;
            }
            if(gintix==4 || (gintit+gintix)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(gintio==4 || (gintit+gintio)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
        }
        gintix=0,gintio=0,gintit=0,gintie=0;
        for(j=0;j<4;j++)
        {
                if(c[j][j]=='.')
                gintie++;
                else if(c[j][j]=='X')
                gintix++;
                else if(c[j][j]=='O')
                gintio++;
                else if(c[j][j]=='T')
                gintit++;
        }
            if(gintix==4 || (gintit+gintix)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(gintio==4 || (gintit+gintio)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
            
            gintix=0,gintio=0,gintit=0,gintie=0;
        for(j=0;j<4;j++)
        {
                if(c[j][3-j]=='.')
                gintie++;
                else if(c[j][3-j]=='X')
                gintix++;
                else if(c[j][3-j]=='O')
                gintio++;
                else if(c[j][3-j]=='T')
                gintit++;
        }
        
        if(gintix==4 || (gintit+gintix)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(gintio==4 || (gintit+gintio)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
            
           if(gintiie==0)
           {
               printf("Case #%d: Draw\n",i);
               goto abc;
           }
           else
           {
               printf("Case #%d: Game has not completed\n",i);
               goto abc;
           }
        
    abc:  
    scanf("%c",&ch);
    }
    return 0;
}