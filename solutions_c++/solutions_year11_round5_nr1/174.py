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
#define inf (1e9)
#define pb push_back

using namespace std;

struct point 
{
  long double x, y;
}A[2][110];

int l, u, g;
long double w;

long double mysqrt (long double a)
{
  //cerr<<a<<endl;
  if (a<=0.0)
    return 0.0;
  return sqrt(a);
}

int main()
{
  int t, cnt;
  long double s, ss, z, v, cx;
  long double ii;
  int i, j;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  scanf("%d", &t);
  for (cnt=1; cnt<=t; cnt++)
  {
    cerr<<"test #"<<cnt<<endl;
    printf("Case #%d:\n", cnt);
    s=0.0;
    cin>>w;
    scanf("%d%d%d", &l, &u, &g);
    for (i=0; i<l; i++)
      cin>>A[0][i].x>>A[0][i].y;
    for (i=0; i<u; i++)
      cin>>A[1][i].x>>A[1][i].y;
    A[0][l].x=inf, A[1][u].x=inf;
    z=A[1][0].y-A[0][0].y, v=(A[1][1].y-A[1][0].y)/A[1][1].x-(A[0][1].y-A[0][0].y)/A[0][1].x, cx=0.0;
    for (i=0, j=0; i<l-1 || j<u-1; )
    {
      //cerr<<i<<" "<<j<<" s="<<s<<" z="<<z<<" v="<<v<<" "<<cx<<endl;
      if (A[0][i+1].x<A[1][j+1].x)
      {
        s+=(A[0][i+1].x-cx)*(z+v*(A[0][i+1].x-cx)/2.0), z+=(A[0][i+1].x-cx)*v, cx=A[0][i+1].x;
        v+=(A[0][i+1].y-A[0][i].y)/(A[0][i+1].x-A[0][i].x);
        i++;
        v-=(A[0][i+1].y-A[0][i].y)/(A[0][i+1].x-A[0][i].x);
      }
      else
      {
        s+=(A[1][j+1].x-cx)*(z+v*(A[1][j+1].x-cx)/2.0), z+=(A[1][j+1].x-cx)*v, cx=A[1][j+1].x;
        v-=(A[1][j+1].y-A[1][j].y)/(A[1][j+1].x-A[1][j].x);
        j++;
        v+=(A[1][j+1].y-A[1][j].y)/(A[1][j+1].x-A[1][j].x);
      }
    }
    //cerr<<s<<endl;
    ss=s/((long double)g), ii=1.0, s=0.0;
    A[0][l].x=inf, A[1][u].x=inf;
    z=A[1][0].y-A[0][0].y, v=(A[1][1].y-A[1][0].y)/A[1][1].x-(A[0][1].y-A[0][0].y)/A[0][1].x, cx=0.0;
    for (i=0, j=0; i<l-1 || j<u-1; )
    {
      if (A[0][i+1].x<A[1][j+1].x)
      {
        while (s+(A[0][i+1].x-cx)*(z+v*(A[0][i+1].x-cx)/2.0)>=ss*ii && ii<((long double)g))
        {
          if (v!=0.0)
            printf("%.8lf\n", (double)(((-z+mysqrt(z*z-2.0*v*(s-ss*ii)))/v)+cx));
          else
            printf("%.8lf\n", ((double)(cx+(ss*ii-s)/z)));
          ii+=1.0;
        }
        s+=(A[0][i+1].x-cx)*(z+v*(A[0][i+1].x-cx)/2.0), z+=(A[0][i+1].x-cx)*v, cx=A[0][i+1].x;
        v+=(A[0][i+1].y-A[0][i].y)/(A[0][i+1].x-A[0][i].x);
        i++;
        v-=(A[0][i+1].y-A[0][i].y)/(A[0][i+1].x-A[0][i].x);
      }
      else
      {
        while (s+(A[1][j+1].x-cx)*(z+v*(A[1][j+1].x-cx)/2.0)>=ss*ii && ii<((long double)g))
        {
          if (v!=0.0)
            printf("%.8lf\n", (double)(((-z+mysqrt(z*z-2.0*v*(s-ss*ii)))/v)+cx));
          else
            printf("%.8lf\n", ((double)(cx+(ss*ii-s)/z)));
          ii+=1.0;
        }
        s+=(A[1][j+1].x-cx)*(z+v*(A[1][j+1].x-cx)/2.0), z+=(A[1][j+1].x-cx)*v, cx=A[1][j+1].x;
        v-=(A[1][j+1].y-A[1][j].y)/(A[1][j+1].x-A[1][j].x);
        j++;
        v+=(A[1][j+1].y-A[1][j].y)/(A[1][j+1].x-A[1][j].x);
      }
    }
  }
  return 0;
}
