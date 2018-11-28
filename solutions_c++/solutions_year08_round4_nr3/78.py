#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define inf 1000000000
#define eps 1e-7
#define lim 1001
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,n,i;
int X[lim],Y[lim],Z[lim],P[lim];

bool possible(double x1,double y1,double z1,double p1,double x2,double y2,double z2,double p2)
{
  return p2>=(fabs(x1-x2)+fabs(y1-y2)+fabs(z1-z2))/p1;
}
bool sat(double k)
{
  double xmin,xmax,ymin,ymax,zmin,zmax,x1,y1,z1,x2,y2,z2,x,y,z;
  int i,j;
  bool f=1;
  
  xmin=-inf;
  xmax=inf;
  ymin=-inf;
  ymax=inf;
  zmin=-inf;
  zmax=inf;
  for(i=0;i<n;i++)
    for(j=i+1;j<n;j++)
    {
      x=(double) (X[i]*P[j]+X[j]*P[i])/(P[i]+P[j]);
      y=(double) (Y[i]*P[j]+Y[j]*P[i])/(P[i]+P[j]);
      z=(double) (Z[i]*P[j]+Z[j]*P[i])/(P[i]+P[j]);
	  if(!possible(X[i],Y[i],Z[i],P[i],x,y,z,k) || !possible(X[j],Y[j],Z[j],P[j],x,y,z,k))
        return 0;
	}
  return 1;
}
double bs(double i,double j)
{
  double k;
  
  if(fabs(i-j)<eps)
    return i;
  k=(i+j)/2;
  if(sat(k))
    return bs(i,k);
  else
    return bs(k,j);
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d",&n);
	for(i=0;i<n;i++)
	  scanf("%d %d %d %d",&X[i],&Y[i],&Z[i],&P[i]);
    printf("Case #%d: %.6lf\n",c+1,bs(0,inf));
  }
  return 0;
}
