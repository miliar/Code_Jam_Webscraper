#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;
char a[60][60];
int n,m;
int main()
{
   bool work();
   int T;
   scanf("%d",&T);
   while (T--)
   {
      scanf("%d%d",&n,&m);
      for (int i=1;i<=n;i++)
         for (int j=1;j<=m;j++)
            cin>>a[i][j];
      static int id=0;
      printf("Case #%d:\n",++id);
      if (!work())
         printf("Impossible\n");
      else
         for (int i=1;i<=n;i++)
         {
            for (int j=1;j<=m;j++)
               printf("%c",a[i][j]);
            printf("\n");
         }
   }
   return(0);
}
bool work()
{
   bool check(int,int);
   for (int i=1;i<=n;i++)
      for (int j=1;j<=m;j++)
      {
         if (a[i][j]!='#')
            continue;
         if (check(i+1,j) && check(i,j+1) && check(i+1,j+1))
         {
            a[i][j]=a[i+1][j+1]='/';
            a[i+1][j]=a[i][j+1]='\\';
         }
         else
            return(false);
      }
   return(true);
}
bool check(int x,int y)
{
   return(x<=n && y<=m && a[x][y]=='#');
}
