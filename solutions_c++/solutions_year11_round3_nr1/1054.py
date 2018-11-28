#include <stdio.h>
#include <stdlib.h>
int main()
{ 
    int t,T,R,C,i,j,flag;
    char ch[150][150],c;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%d%d%c",&R,&C,&c);
        for (i=0;i<R;i++)
            scanf("%s",ch[i]);
        printf("Case #%d:\n",t);
        flag=1;
        for (i=0;i<R&&flag;i++)
            for (j=0;j<C&&flag;j++)
                if (ch[i][j]=='#')
                {
                   if (i+1<R&&j+1<C&&ch[i+1][j]=='#'&&ch[i][j+1]=='#'&&ch[i+1][j+1]=='#')
                   {
                      ch[i][j]='/';
                      ch[i][j+1]='\\';
                      ch[i+1][j]='\\';
                      ch[i+1][j+1]='/';                                                             
                   } else flag=0;
                }
        if (flag==0) printf("Impossible\n");
        else
            for (i=0;i<R;i++,printf("\n"))
                for (j=0;j<C;j++) printf("%c",ch[i][j]);
    }
    return 0;
}
