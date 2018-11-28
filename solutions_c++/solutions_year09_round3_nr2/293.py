#include <cstdio>
#include <cmath>
using namespace std;

int main(){
   int t,T,n,i;
   double x0,y0,z0,x,y,z,dmin,tmin;
   scanf("%d", &T);
   for (t=1;t<=T;t++){
      scanf("%d",&n);
      int a,b,c,d,e,f;
      x0=y0=z0=x=y=z=0;
      for (i=0; i<n; i++) {
	 scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f);
	 x0+=a;
	 y0+=b;
	 z0+=c;
	 x+=d;
	 y+=e;
	 z+=f;
      }
      if (x!=0 || y!=0 || z!=0) {
	 tmin = - (x*x0 + y*y0 + z*z0);
	 if (tmin<0) {
	    tmin=0;
	 } else {
	    tmin /= (x*x + y*y + z*z);
	 }
	 dmin=(x0+x*tmin)*(x0+x*tmin) + (y0+y*tmin)*(y0+y*tmin) + (z0+z*tmin)*(z0+z*tmin);
	 dmin/=(n*n);
      } else {
	 tmin=0;
	 dmin=x0*x0+y0*y0+z0*z0;
	 dmin/=(n*n);
      }
      dmin=sqrt(dmin);
      printf("Case #%d: %.8lf %.8lf\n",t,dmin,tmin);
   }
   return 0;
}
