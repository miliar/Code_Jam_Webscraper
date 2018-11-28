#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back

using namespace std;

char field[10][10];
int res;
int N[5][5][2][2];
int Deg[5][5], fl, c, r;

int main()
{
  int t, cnt, i, j, p;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    cerr<<"test #"<<cnt<<endl;
    memset(field,0,sizeof(field));
    res=0;
    scanf("%d%d ", &r, &c);
    for (i=0; i<r; i++)
      gets(field[i]);
    for (i=0; i<r; i++)
      for (j=0; j<c; j++)
      {
        if (field[i][j]=='|')
          N[i][j][0][0]=(i+1)%r, N[i][j][0][1]=j, N[i][j][1][0]=(i+r-1)%r, N[i][j][1][1]=j;
        if (field[i][j]=='-')
          N[i][j][0][0]=i, N[i][j][0][1]=(j+1)%c, N[i][j][1][0]=i, N[i][j][1][1]=(j+c-1)%c;
        if (field[i][j]=='\\')
          N[i][j][0][0]=(i+1)%r, N[i][j][0][1]=(j+1)%c, N[i][j][1][0]=(i+r-1)%r, N[i][j][1][1]=(j+c-1)%c;
        if (field[i][j]=='/')
          N[i][j][0][0]=(i+1)%r, N[i][j][0][1]=(j+c-1)%c, N[i][j][1][0]=(i+r-1)%r, N[i][j][1][1]=(j+1)%c;
      }
    for (p=0; p<(1<<r*c); p++)
    {
      memset(Deg,0,sizeof(Deg));
      for (i=0; i<r; i++)
        for (j=0; j<c; j++)
        {
          if ((p&(1<<(i*c+j)))!=0)
            Deg[N[i][j][0][0]][N[i][j][0][1]]++;
          else
            Deg[N[i][j][1][0]][N[i][j][1][1]]++;
        }
      for (fl=1, i=0; i<r; i++)
        for (j=0; j<c; j++)
          if (Deg[i][j]!=1)
            fl=0;
      res+=fl;
    }
    printf("Case #%d: %d\n", cnt, res);
  }
  return 0;
}
