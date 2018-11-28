#include <iostream>
#include <cstdio>
using namespace std;

char map[52][52];

int main()
{
    int t,r,c,i,j,num=0,flag;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        num++;
        scanf("%d%d",&r,&c);
        for(i=0;i<r;i++)
            scanf("%s",map[i]);
        for(i=0,flag=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(map[i][j]!='#')
                    continue;
                else
                {
                    if(map[i][j+1]!='#' || map[i+1][j]!='#' || map[i+1][j+1]!='#' || j+1>=c || i+1>=r)
                    {
                        flag=1;
                        break;
                    }
                    else
                    {
                        map[i][j]=map[i+1][j+1]='/';
                        map[i][j+1]=map[i+1][j]='\\';
                        j++;
                    }
                }
            }
            if(flag)
                break;
        }
        printf("Case #%d:\n",num);
        if(flag)
            printf("Impossible\n");
        else
        {
            for(i=0;i<r;i++)
                printf("%s\n",map[i]);
        }
    }
    return 0;
}