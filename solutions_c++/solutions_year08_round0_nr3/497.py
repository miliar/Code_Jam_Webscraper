#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define PROBLEM "c"

typedef long long i64;
typedef unsigned long long u64;

#define PI acos(-1.0)
#define ZERO 1e-9
#define EPS 1e-14

inline int inside(double x,double y,double r) {
  return (r*r>x*x+y*y-ZERO);
}

double Z;

double find_area(double x,double y,double s,double r) {
  if(4*s*s/Z<EPS) return 0;
  int z=inside(x-s,y-s,r)+inside(x-s,y+s,r)+
        inside(x+s,y-s,r)+inside(x+s,y+s,r);
  if(!z) return 0;
  if(z==4) return 4*s*s;
  s*=0.5;
  return find_area(x-s,y-s,s,r)+find_area(x-s,y+s,s,r)+
         find_area(x+s,y-s,s,r)+find_area(x+s,y+s,s,r);
}

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    fprintf(stderr,"%d\n",tst);
    double f,R,t,r,g;
    scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
    r+=f; g-=2*f; t+=f;
    if(g<ZERO) {
      printf("Case #%d: 1.0\n",tst);
      continue;
    }
    int i,j;
    double s=0;
    Z=PI*R*R*0.25;
    for(i=0;;++i) {
      double x=r+g*0.5+i*(2*r+g);
      if(x-0.5*g>R-t-ZERO) break;
      for(j=0;;++j) {
        double y=r+g*0.5+j*(2*r+g);
        if(!inside(x-0.5*g,y-0.5*g,R-t)) break;
        s+=find_area(x,y,g*0.5,R-t);
      }
    }
    s=1-s/Z;
    printf("Case #%d: %0.20lf\n",tst,s);
  }

  return 0;
}
