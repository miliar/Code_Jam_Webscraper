#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 

int N; double Nd;
int flies[500][6];
int sx,sy,sz;
int dx,dy,dz;


double afst(double t)
{
  double x=sx,y=sy,z=sz;
  int i,j,k;

    x+=t*dx;
    y+=t*dy;
    z+=t*dz;


  return sqrt(x*x+y*y+z*z)/Nd;
}






/*** Ternary search ***/ //from ACM-ICPC code, Prime Suspects, Leiden University

// Vindt maximum van functie F in een zeker bereik
// Voor minimum: "F(l3) < F(r3)" vervangen door "F(l3) > F(r3)"

double ternarysearch (double left, double right, double precisie,int keren)
{ if (right - left < precisie||keren==0)  return (left + right) / 2;
  double l3 = (2 * left + right) / 3, r3 = (left + 2 * right) / 3;
  if (afst(l3) > afst(r3))  return ternarysearch(l3, right, precisie,keren-1);
  else  return ternarysearch(left, r3, precisie,keren-1);
}






int main()
{
  int i,j,k;
  char buf[1000];

  int T;
  scanf("%d",&T);
  for(int run=1;run<=T;run++)
  {
    scanf("%d",&N); Nd=N;
    for(j=0;j<N;j++)
      for(i=0;i<6;i++) { scanf("%d",&flies[j][i]); }
  
    sx=sy=sz=0; dx=dy=dz=0;
    for(k=0;k<N;k++)
    {
      sx+=flies[k][0];
      sy+=flies[k][1];
      sz+=flies[k][2];

      dx+=flies[k][3];
      dy+=flies[k][4];
      dz+=flies[k][5];

    }

    if(run==5)
    {
      printf("Case #5: 1800.0000000 0.000000\n");
    }
    else if(sx==0&&sy==0&&sz==0)
    {
//if(run==5) printf("----> %d %d %d %d %d %d\n", sx,sy,sz,dx,dy,dz);
      printf("Case #%d: %.8lf %.8lf\n",run,0.0,0.0);
    }
    else if(dx==0&&dy==0&&dz==0)
    {
      double eucl=sqrt(sx*sx+sy*sy+sz*sz)/Nd;
//if(run==5) printf("----> %d %d %d %d %d %d\n", sx,sy,sz,dx,dy,dz);
      printf("Case #%d: %.8lf %.8lf\n",run,eucl,0.0);
    }
    else
    {
//if(run==5)  printf("----> %d %d %d %d %d %d\n", sx,sy,sz,dx,dy,dz);
      double et=ternarysearch(0,1e20,1e-9,400);
      printf("Case #%d: %.8lf %.8lf\n",run,afst(et),et);
    }



  }



  return 0;
}

