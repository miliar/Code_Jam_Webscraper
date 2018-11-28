#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
  //clock_t begin,end;
  //begin=clock();
  freopen("ac1.in","r",stdin);
  freopen("ac1.out","w",stdout);
  int t,to=0;
  scanf("%d",&t);
  while(t--)
  {
    to++;
    int n,m,i,j;
    scanf("%d%d\n",&n,&m);
    char a[100][100];
    for(i=0;i<=90;i++)
    {
      for(j=0;j<=90;j++)
        a[i][j]=' ';
    }
    char ro;
    for(i=0;i<n;i++)
    {
      for(j=0;j<m;j++)
        {
          scanf("%c",&a[i][j]);
          //printf("%d %d=%c",i,j,a[i][j]);
        }
      scanf("%c",&ro);
    }
    bool ok=0;
    for(i=0;i<n;i++)
    {
      for(j=0;j<m;j++)
      {
        if(a[i][j]=='#')
        {
          //printf("orson\n");
          a[i][j]='/';
          if(a[i][j+1]=='#') a[i][j+1]='\\';
            else {ok=1;break;}
          if(a[i+1][j]=='#') a[i+1][j]='\\';
            else {ok=1;break;}
          if(a[i+1][j+1]=='#') a[i+1][j+1]='/';
            else {ok=1;break;}
        }
      }
      if(ok==1) break;
    }
    printf("Case #%d:\n",to);
    if(ok==1) printf("Impossible\n");
    else
    {
      for(i=0;i<n;i++)
      {
        for(j=0;j<m;j++)
          printf("%c",a[i][j]);
        printf("\n");
      }
    }
  }
  //end=clock();
  return 0;
}
