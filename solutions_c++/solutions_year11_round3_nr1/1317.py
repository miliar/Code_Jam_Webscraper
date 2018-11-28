#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large(1).in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j,k,l,t,kase=1,f,r,c;
    char b[109][109];
    scanf("%d",&t);
    while (t--)
    {
        f=0;
        scanf("%d %d",&r,&c);
        gets(b[0]);
        for (i=0;i<r;i++)
            gets(b[i]);
        for (i=0;i<r;i++)
        {
            for (j=0;j<c;j++)
            {
                if (b[i][j]=='#')
                {
                    if (b[i][j+1]=='#' && b[i+1][j]=='#' && b[i+1][j+1]=='#')
                    {
                        b[i][j]='/';
                        b[i][j+1]='\\';
                        b[i+1][j]='\\';
                        b[i+1][j+1]='/';
                    }
                    else
                    {
                        f=1;
                        break;
                    }
                }
            }
            if (f==1)
                break;
        }

        if (f==1)
        {
            printf("Case #%d:\n",kase++);
            printf("Impossible\n");
            continue;
        }
        printf("Case #%d:\n",kase++);
        for (i=0;i<r;i++)
            puts(b[i]);
    }
    return 0;
}
