#include <stdio.h>
#include <string.h>
#include <math.h>
#define eps (1e-5)

int n;
struct node {
	double x,y,z,vx,vy,vz;
	
	void clear() {
		x = y = z = vx = vy = vz = 0.000000;
	}
} point[510],mass,Q;

int main() {
	int t,i,j,c=0;
	double Time;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf%lf%lf%lf",&point[i].x,&point[i].y,&point[i].z,&point[i].vx,&point[i].vy,&point[i].vz);
		mass.clear();
		for(i=0;i<n;i++) {
			mass.x += point[i].x;
			mass.y += point[i].y;
			mass.z += point[i].z;
			mass.vx += point[i].vx;
			mass.vy += point[i].vy;
			mass.vz += point[i].vz;
		}
		mass.x /= (double)n;
		mass.y /= (double)n;
		mass.z /= (double)n;
		mass.vx /= (double)n;
		mass.vy /= (double)n;
		mass.vz /= (double)n;
		//printf("%.8lf %.8lf %.8lf %.8lf %.8lf %.8lf\n",mass.x,mass.y,mass.z,mass.vx,mass.vy,mass.vz);
		
		printf("Case #%d: ",++c);
		if(mass.vx == 0 && mass.vy == 0 && mass.vz == 0) {
			printf("%.8lf 0.00000000\n",(double)sqrt(mass.x*mass.x+mass.y*mass.y+mass.z*mass.z));
			continue;
		}
		
		Time = -(mass.x*mass.vx+mass.y*mass.vy+mass.z*mass.vz)/(mass.vx*mass.vx+mass.vy*mass.vy+mass.vz*mass.vz);
		Q.x = mass.x+mass.vx*Time;
		Q.y = mass.y+mass.vy*Time;
		Q.z = mass.z+mass.vz*Time;
		
		if(Time <= 0.00000000) {
			printf("%.8lf 0.00000000\n",(double)sqrt(mass.x*mass.x+mass.y*mass.y+mass.z*mass.z));
			continue;
		}
		printf("%.8lf %.8lf\n",(double)sqrt(Q.x*Q.x+Q.y*Q.y+Q.z*Q.z),Time);
	}
	
	return 0;
}
