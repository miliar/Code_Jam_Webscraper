#include<iostream>
#include<cstdio>


using namespace std;

int main()
{
    int t,i,j,k;
    char ch;
    int countx=0,counto=0,countt=0,counte=0,flag=0,countie=0;
    scanf("%d",&t);
    scanf("%c",&ch);
    for(i=1;i<=t;i++)
    {
        flag=0;
        countx=0,counto=0,countt=0,counte=0,countie=0;
        char c[6][6];
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                scanf("%c",&c[j][k]);
                if(c[j][k]=='.')
                countie++;
            }
            scanf("%c",&ch);
        }
        for(j=0;j<4;j++)
        {
            countx=0,counto=0,countt=0,counte=0;
            for(k=0;k<4;k++)
            {
                if(c[j][k]=='.')
                counte++;
                else if(c[j][k]=='X')
                countx++;
                else if(c[j][k]=='O')
                counto++;
                else if(c[j][k]=='T')
                countt++;
            }
            if(countx==4 || (countt+countx)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(counto==4 || (countt+counto)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
        }
        
        for(j=0;j<4;j++)
        {
            countx=0,counto=0,countt=0,counte=0;
            for(k=0;k<4;k++)
            {
                if(c[k][j]=='.')
                counte++;
                else if(c[k][j]=='X')
                countx++;
                else if(c[k][j]=='O')
                counto++;
                else if(c[k][j]=='T')
                countt++;
            }
            if(countx==4 || (countt+countx)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(counto==4 || (countt+counto)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
        }
        countx=0,counto=0,countt=0,counte=0;
        for(j=0;j<4;j++)
        {
                if(c[j][j]=='.')
                counte++;
                else if(c[j][j]=='X')
                countx++;
                else if(c[j][j]=='O')
                counto++;
                else if(c[j][j]=='T')
                countt++;
        }
            if(countx==4 || (countt+countx)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(counto==4 || (countt+counto)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
            
            countx=0,counto=0,countt=0,counte=0;
        for(j=0;j<4;j++)
        {
                if(c[j][3-j]=='.')
                counte++;
                else if(c[j][3-j]=='X')
                countx++;
                else if(c[j][3-j]=='O')
                counto++;
                else if(c[j][3-j]=='T')
                countt++;
        }
        
        if(countx==4 || (countt+countx)==4)
            {
                printf("Case #%d: X won\n",i);
                goto abc;
            }
            else if(counto==4 || (countt+counto)==4)
            {
                printf("Case #%d: O won\n",i);
                goto abc;
            }
            
           if(countie==0)
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
