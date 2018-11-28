#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
char s[111][111];
int main()
{
    int i,j,k,n,m,T,p=0;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
        p++;
       scanf("%d%d",&n,&m);
       getchar();
       for (i=0;i<n;i++)
       gets(s[i]);
       bool flag=false;
       for (i=0;i<n;i++)
       {
           for (j=0;j<m;j++)
           {
               if (s[i][j]=='#')
               {
                  if (i==n-1||j==m-1) {flag=true; break;}
                  if (s[i+1][j]!='#'||s[i][j+1]!='#'||s[i+1][j+1]!='#'){flag=true;break;}
                  s[i][j]='/';
                  s[i][j+1]='\\';
                  s[i+1][j]='\\';
                  s[i+1][j+1]='/';
               }
           }
           if (flag) break;
       }
       printf("Case #%d:\n",p);
       if (flag) {puts("Impossible");}
       else
       {
          for (i=0;i<n;i++)
          cout<<s[i]<<endl;
       }
    }
}
