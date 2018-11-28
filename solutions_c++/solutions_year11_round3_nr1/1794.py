//kunal10
//Program for Prob1 - SQTiles

#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    int i,j,k,t,count,r,c,flag;
    char s[51][51];
    scanf("%d",&t);
    j=1;
    while(j<=t)
    {
        scanf("%d %d",&r,&c);
        flag=0;
        for(i=0;i<r;i++){scanf("%s",&s[i]);}
        for(i=0;i<r;i++)
        {
            for(k=0;k<c;k++)
            {
                if(s[i][k]=='#')
                {
                    if(i==r-1 || k==c-1){flag=1;}
                    else if(s[i][k+1]=='#' && s[i+1][k]=='#' && s[i+1][k+1]=='#')
                    {
                        s[i][k]='/';
                        s[i][k+1]='\\';
                        s[i+1][k]='\\';
                        s[i+1][k+1]='/';
                    }
                    else
                    {
                        flag=1;
                    }
                }
            }
            if (flag==1){break;}
        }
        printf("Case #%d:\n",j);
        if(flag==1){printf("Impossible\n");}
        else
        {
            for(i=0;i<r;i++){
                for(k=0;k<c;k++)
                    {printf("%c",s[i][k]);}
                printf("\n");
            }

        }
        j++;
    }

    return 0;
}

