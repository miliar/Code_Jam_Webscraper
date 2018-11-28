#include<stdio.h>
char s[100][100];
int main()
{
    int i,j,n,m,k,l,p,o;
    scanf("%d",&p);
    for(o=1;o<=p;o++)
    {
        scanf("%d%d\n",&n,&m);
        for(i=1;i<=n;i++)
        {
           for(j=1;j<=m;j++)
            scanf("%c",&s[i][j]);
           if(o!=p||i!=n) getchar();
        }
        k=1;
        for(i=1;i<n;i++)
         {
           for(j=2;j<=m;j++)
            if(s[i][j]=='#'&&s[i][j-1]=='#')
            {
             if(s[i+1][j]=='#'&&s[i+1][j-1]=='#')
             {
                s[i][j]='\\';
                s[i][j-1]='/';
                s[i+1][j]='/';
                s[i+1][j-1]='\\';
             }
             else  k=0;
             if(k==0) break;
            }
           if(k==0) break;
         }
        for(i=1;i<=n;i++)
         for(j=1;j<=m;j++)
          if(s[i][j]=='#') k=0;
        printf("Case #%d: \n",o);
        if(k==0) printf("Impossible\n");
        else 
        {
            for(i=1;i<=n;i++)
            {
               for(j=1;j<=m;j++)
                printf("%c",s[i][j]);
               printf("\n");
            }
        } 
    }
}
