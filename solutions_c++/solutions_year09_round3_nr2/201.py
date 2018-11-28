#include<cstdio>
#include<cmath>

using namespace std;

struct vect
{
 long double x,y,z;
};

vect operator+(vect a, vect b)
{
 vect c;
 c.x=a.x+b.x;
 c.y=a.y+b.y;
 c.z=a.z+b.z;
 return c;
}

vect operator-(vect a, vect b)
{
 vect c;
 c.x=a.x-b.x;
 c.y=a.y-b.y;
 c.z=a.z-b.z;
 return c;
}

vect operator*(vect a, long double b)
{
 vect c;
 c.x=a.x*b;
 c.y=a.y*b;
 c.z=a.z*b;
 return c;
}



vect itov(long double x, long double y, long double z)
{
 vect a;
 a.x=x;
 a.y=y;
 a.z=z;
 return a;
}

#define dot(u,v)   ((u).x * (v).x + (u).y * (v).y + (u).z * (v).z)
#define norm(v)    sqrt(dot(v,v))  // norm = length of vector
#define d(u,v)     norm(u-v)       // distance = norm of difference

void printv(vect a)
{
 printf("(%Lf %Lf %Lf)\n", a.x, a.y, a.z);
}

vect distPtoL( vect P,  vect P0, vect P1)
{
    vect v = P1 - P0;
    vect w = P - P0;

    long double c1 = dot(w,v);
    long double c2 = dot(v,v);
    long double b = c1 / c2;

    vect Pb = P0 + v*b;
    vect wyn;
    wyn.x=d(P, Pb);
    wyn.y=b;
    return wyn;
}

int main()
{
 int t,n;scanf("%d", &t);
 vect pos,cpos;
 vect vel,cvel;
 for(int q=0;q<t;++q)
 {
  cpos=itov(0,0,0);
  cvel=itov(0,0,0);
  scanf("%d", &n);
  for(int i=0;i<n;++i)
  {
   scanf("%Lf%Lf%Lf%Lf%Lf%Lf", &pos.x, &pos.y, &pos.z, &vel.x, &vel.y, &vel.z);
   cpos=cpos+pos;
   cvel=cvel+vel;
  }
  cpos=cpos*(1/(long double) n);
  cvel=cvel*(1/(long double) n);
 // printv(cpos);
 // printv(cvel);
  if(cvel.x==0 && cvel.y==0 && cvel.z==0) 
  {
   printf("Case #%d: %.8Lf %.8Lf\n", q+1, norm(cpos), 0);
  }
  else
  {
   vect wyn=distPtoL(itov(0,0,0), cpos, cpos+cvel);
   if(wyn.y<0)
   {
    wyn.x=norm(cpos);
    wyn.y=0;
   }
   printf("Case #%d: %.8Lf %.8Lf\n", q+1, wyn.x, wyn.y);
  }
 }

}
