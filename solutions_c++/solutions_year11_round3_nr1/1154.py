#include<iostream>
using namespace std;

int T,i,j,k,R,C,f;
char str[100][100];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (k=1;k<=T;k++)
    {
        scanf("%d%d\n",&R,&C);
        for (i=0;i<R;i++)
            gets(str[i]);
        f=1;
        printf("Case #%d:\n",k);
        for (i=0;i<R;i++)
        {
            for (j=0;j<C;j++)
                if (str[i][j]=='#')
                {
                   str[i][j]='/';
                   if (j+1<C && str[i][j+1]=='#')
                      str[i][j+1]='\\';
                   else
                   {
                       f=0;
                       j=C;i=R;
                   }
                   if (i+1<R && str[i+1][j]=='#')
                      str[i+1][j]='\\';
                   else
                   {
                       f=0;
                       j=C;i=R;
                   }
                   if (i+1<R && j+1<C && str[i+1][j+1]=='#')
                      str[i+1][j+1]='/';
                   else
                   {
                       f=0;
                       j=C;i=R;
                   }
                }
        }
        if (f)
        {
            for (i=0;i<R;i++)
                puts(str[i]);   
        }
        else
        {
            puts("Impossible");
        }
    }
}
