#include <stdio.h>
#include <string.h>

char s[100][100];

int main()
{
    int cas;
    int n,m;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++) scanf("%s",s[i]);
        for(int i=0;i<n-1;i++)
         for(int j=0;j<m-1;j++)
          if (s[i][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j]=='#'&&s[i+1][j+1]=='#')
          {
              s[i][j]='/';s[i][j+1]='\\';
              s[i+1][j]='\\';s[i+1][j+1]='/';
          }
        bool flag=1;
        for(int i=0;i<n;i++)
         for(int j=0;j<m;j++)
          if (s[i][j]=='#') flag=0;
        printf("Case #%d:\n",ll);
        if (!flag)puts("Impossible");
        else for(int i=0;i<n;i++) puts(s[i]);
    }
    return 0;
}


