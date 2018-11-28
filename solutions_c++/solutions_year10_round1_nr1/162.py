#pragma comment(linker, "/STACK:100000000")  

#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;
char b[55][55];
int a[55][55];
char c[75][75];

int dx[]={0,1,-1,1};
int dy[]={1,1,1,0};


int get(int t, int k)
{
  for (int i=10; i<=10+n; i++)
    for (int j=10; j<=10+n; j++)
      if (c[i][j]==t)
        for (int d=0; d<4; d++)
        {
          int tx=i, ty=j, cur=0;
          while (c[tx+dx[d]][ty+dy[d]]==c[i][j])
            tx+=dx[d], ty+=dy[d], cur++;
          if (cur>=k-1)
            return 1;
        }
  return 0;
}

int main(void)
{
   //freopen("A-small-attempt0.in", "r", stdin);
   //freopen("A-small-attempt0.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      //fprintf(stderr, "Case #%d: \n", tn+1);

      int k;
      printf("Case #%d: ", tn+1);
      scanf("%d%d\n", &n, &k);
      for (int i=0; i<n; i++)
        gets(b[i]);

      for (int i=0; i<n; i++)
        for (int j=0; j<n; j++)
          a[j][n-i-1]=b[i][j];

      memset(c, '.', sizeof(c));
      for (int j=0; j<n; j++)
      {
        int k=n-1;
        for (int i=n-1; i>=0; i--)
          if (a[i][j]!='.')
            a[k--][j]=a[i][j];
        while (k!=-1)
          a[k--][j]='.';
      }
      for (int i=0; i<n; i++)
        for (int j=0; j<n; j++)
          c[10+i][10+j]=a[i][j];

      int f1=get('B', k), f2=get('R', k);
      if (f1 && f2)
        puts("Both");
      if (f1 && !f2)
        puts("Blue");
      if (!f1 && f2)
        puts("Red");
      if (!f1 && !f2)
        puts("Neither");
   }
   return 0;
}
