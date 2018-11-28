
#include <stdio.h>

#include<string>
#include<map>
#include <math.h>


using namespace std;


typedef struct _point {
  
  double x;
  double y;
  double z;

} point;



main() {

  
  int T;

  
  scanf("%d",&T);
  
  
  
  for (int t = 1; t <= T; t++) {

    int N;

    point pos[1000];
    point vel[1000];

    scanf("%d",&N);

    for (int n = 0; n < N; n++) {
      scanf("%lf %lf %lf %lf %lf %lf",&pos[n].x,&pos[n].y,&pos[n].z,
	    &vel[n].x,&vel[n].y,&vel[n].z);
    }
    
    point center;
    point centerv;
    center.x = center.y = center.z = 0;
    centerv.x = centerv.y = centerv.z = 0;
    for (int n = 0; n < N; n++) {
      center.x += pos[n].x;
      center.y += pos[n].y;
      center.z += pos[n].z;
      centerv.x += vel[n].x;
      centerv.y += vel[n].y;
      centerv.z += vel[n].z;

    }    
    // dont forget to divide by N !
    
    center.x /= N;
    center.y /= N;
    center.z /= N;
    centerv.x /= N;
    centerv.y /= N;
    centerv.z /= N;

    double tmin = 0.0;
    if (     (centerv.x * centerv.x + 
	      centerv.y * centerv.y + 
	      centerv.z * centerv.z) > 0) {
      
      tmin = -( center.x * centerv.x  +
		       center.y * centerv.y  +
		       center.z * centerv.z ) /
	(centerv.x * centerv.x + 
	 centerv.y * centerv.y + 
	 centerv.z * centerv.z);
    }

    if (tmin < 0.00000001) tmin = 0.0;
    
    point posmin;
    posmin.x = center.x + centerv.x * tmin;
    posmin.y = center.y + centerv.y * tmin;
    posmin.z = center.z + centerv.z * tmin;

    double dmin = sqrt(posmin.x * posmin.x + posmin.y * posmin.y
		       + posmin.z * posmin.z);
    
    
    if (dmin < 0.00000001) dmin = 0.0;
    
    printf("Case #%d: %.8lf %.8lf\n",t,dmin,tmin);

  }





}
