#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
   freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\A-large.in", "r", stdin);
   freopen("D:OUTPUT.txt", "w", stdout);
    char a[60][60];
    int r,c;
    int test,pp;
    scanf("%d",&test);
    for (pp=1;pp<=test;pp++)
    {
        printf("Case #%d:\n",pp);
        int i,j;
        int ok=1;
        scanf("%d%d",&r,&c);
        for (i=1;i<=r;i++)
        scanf("%s",a[i]);
        for (i=1;i<=r;i++)
           for (j=0;j<c;j++)
              if (a[i][j]=='#')
              {
                  if (j+1==c||a[i][j+1]!='#'||i==r||a[i+1][j]!='#'||a[i+1][j+1]!='#')
                  {
                      ok=0;
                      break;
                  }
                  else
                  {
                      a[i][j]='/';
                      a[i+1][j]='\\';
                      a[i+1][j+1]='/';
                      a[i][j+1]='\\';
                  }
              }
            if (ok==0) printf("Impossible\n");
            else
             for (i=1;i<=r;i++)
             printf("%s\n",a[i]);
              }
    }
