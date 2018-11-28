#include<stdio.h>
#include<string>
#include<iostream>
#include<string.h>
using namespace std;
int nx[10],no[10],nCases,full,won;
string inpLine;
int main (void)
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d",&nCases);
    for(int i=1;i<=nCases;i++)
    {
        memset(nx,0,sizeof(nx));
        memset(no,0,sizeof(nx));
        full=1;
        won=0;
        for(int j=0;j<4;j++)
        {
            cin>>inpLine;
            for(int k=0;k<4;k++)
            {
                if(inpLine[k]=='.')
                {
                    full=0;
                }
                if(inpLine[k]=='X')
                {
                    nx[j]++;
                    nx[k+4]++;
                    if(j==k)
                    {
                        nx[8]++;
                    }
                    if(j+k==3)
                    {
                        nx[9]++;
                    }
                }
                if(inpLine[k]=='O')
                {
                    no[j]++;
                    no[k+4]++;
                    if(j==k)
                    {
                        no[8]++;
                    }
                    if(j+k==3)
                    {
                        no[9]++;
                    }
                }
                if(inpLine[k]=='T')
                {
                    nx[j]++;
                    nx[k+4]++;
                    no[j]++;
                    no[k+4]++;
                    if(j==k)
                    {
                        nx[8]++;
                        no[8]++;
                    }
                    if(j+k==3)
                    {
                        nx[9]++;
                        no[9]++;
                    }
                }
            }
        }
        for(int j=0;j<10;j++)
        {
            if(nx[j]==4&&won==0)
            {
                printf("Case #%d: X won",i);
                won=1;
            }
            if(no[j]==4&&won==0)
            {
                printf("Case #%d: O won",i);
                won=1;
            }
        }
        if((!won)&&(!full))
        {
            printf("Case #%d: Game has not completed",i);
        }
        else if(!won)
        {
            printf("Case #%d: Draw",i);
        }
        printf("\n");
    }
    return 0;
}
