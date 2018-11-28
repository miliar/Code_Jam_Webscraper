#include <stdio.h>
#include <math.h>

struct point {
  double x;
  double y;
  double z;
};

  double get_dist(point me, point pos) {
    return
      sqrt((me.x-pos.x)*(me.x-pos.x)+
	   (me.y-pos.y)*(me.y-pos.y)+(me.z-pos.z)*(me.z-pos.z));
 }

int main() {
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  int T;
  scanf("%d\n",&T);
  point me;
  me.x=me.y=me.z=0;
  for (int i=1;i<=T;++i) {
    int n;
    scanf("%d\n",&n);
    point pos;
    point vec;
    pos.x=pos.y=pos.z=0;
    vec.x=vec.y=vec.z=0;
    int x,y,z,dx,dy,dz;
    for (int j=0;j<n;++j) {
      scanf("%d %d %d %d %d %d\n",&x,&y,&z,&dx,&dy,&dz);
      pos.x+=x;pos.y+=y;pos.z+=z;
      vec.x+=dx;vec.y+=dy;vec.z+=dz;
    }
    point posn;
    posn.x=pos.x+vec.x;
    posn.y=pos.y+vec.y;
    posn.z=pos.z+vec.z;
    double dist1 = get_dist(me,pos);
    double dist2 = get_dist(me,posn);
    double dist3 = get_dist(pos,posn);
    point bestp = pos;
    double bestt = 0;
    double dmin = dist1;
    if (dist1 == 0) { bestt=0;dmin=dist1;} 
    else if (dist3 != 0 && dist1*dist1 + dist3*dist3 > dist2*dist2) {
      double td = (dist1*dist1 + dist3*dist3 - dist2*dist2)/(2*dist3);
      //      if (i==20) { printf("%f %f %f %f %f %f",pos.x,pos.y,pos.z,
      //			  vec.x,vec.y,vec.z);}
      //      if (i==20) { printf("%f %f\n",td,dist1);     }
	double distt = td;
	td /= dist1;
	//	if (i==20) { printf("%f %f\n",td);}
	double arg = 1-td*td;
	if (arg > 0) {
	dmin = sqrt(arg)*dist1;
	} else {
	  dmin = 0;	
	}
	//	if (i==20) { printf("%f %f\n",1-td*td,dmin);}      
	//      printf("%f\n",dmin);
	bestt = distt / sqrt(vec.x*vec.x+vec.y*vec.y+vec.z*vec.z);
	//	if (i==20) { printf("%f\n",bestt);}
	//      bestp.x = pos.x + bestt*dx;
	//      bestp.y = pos.y + bestt*dy;
	//      bestp.z = pos.z + bestt*dz;
    }
    dmin /= n;
    printf("Case #%d: %.8f %.8f\n",i,dmin,bestt);
  }
  return 0;
}
