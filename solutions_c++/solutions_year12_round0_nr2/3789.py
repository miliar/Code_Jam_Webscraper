#include <stdio.h>
#include <iostream>
using namespace std;

int abs(int a)
{
  if (a<0)
    return -a;
  return a;
};


int max3(int a, int b, int c)
{
  if (a>=b && a>=c)
    return a;
  if (b>=a && b>=c)
    return b;
  return c;
};

int main()
{
  int n,S,p,T;

  cin >> T;

  bool flag1[40][20];
  bool flag2[40][20];

  for (int a=0;a<40;++a)
    for (int b=0;b<20;++b)
    {
      flag1[a][b] = false;
      flag2[a][b] = false;
    };


  for (int a=0; a<=10; ++a)
    for (int b=0; b<=10; ++b)
      for (int c=0; c<=10; ++c)
        if ( abs(a-b)<=1 && abs(b-c)<=1 && abs(c-a)<=1)
          for (int d=0;d<=max3(a,b,c);++d)
            flag1[a+b+c][d] = true;
        else if ( abs(a-b)<=2 && abs(b-c)<=2 && abs(c-a)<=2)
          for (int d=0;d<=max3(a,b,c);++d)
            flag2[a+b+c][d] = true;

  for (int i1=1;i1<=T;++i1)
  {
    int i,j,k,l,m;
    cin >> n >> S >> p;
    int total[200];

    for (i = 0;i < n; ++i)
      cin >> total[i];

    int f[200][200];
    
    for (k = 0; k < 200;++k)
      f[0][k] = 0;

    if (flag1[total[0]][p])
      f[0][0] = 1;
    
     if (flag2[total[0]][p])
      f[0][1] = 1;

    for (i=1; i<n; ++i)
      for (j=0; j<=S; ++j)
      {
        f[i][j] = f[i-1][j];
        if (total[i]>=2 && total[i]<=28 && f[i-1][j-1]>f[i-1][j])
          f[i][j] = f[i-1][j-1];

        if ( flag1[total[i]][p] && f[i-1][j]+1>f[i][j])
          f[i][j] = f[i-1][j]+1;
        
        if ( flag2[total[i]][p] && j>0 && f[i-1][j-1]+1>f[i][j])
          f[i][j] = f[i-1][j-1]+1;
      };

    printf("Case #%d: %d\n", i1, f[n-1][S]);  
  };
};


