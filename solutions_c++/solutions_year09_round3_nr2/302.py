#include <stdio.h>
#include <math.h>

int main(){
	int Cases, Case;
	int N;
	double x,y,z,vx,vy,vz;
	double xt,yt,zt,vxt,vyt,vzt;
	scanf("%d",&Cases);
	for(Case = 1;Case<=Cases;Case++){
		scanf("%d",&N);	
		x=y=z=vx=vy=vz=0;
		for(int i = 0;i<N;i++){
			scanf("%lf %lf %lf %lf %lf %lf",&xt,&yt,&zt,&vxt,&vyt,&vzt);
			x+=xt;
			y+=yt;
			z+=zt;
			vx+=vxt;
			vy+=vyt;
			vz+=vzt;
		}
		x/=(double)N;
		y/=(double)N;
		z/=(double)N;
		vx/=(double)N;
		vy/=(double)N;
		vz/=(double)N;
		//printf("(%lf, %lf, %lf) com v (%lf, %lf, %lf)\n",x,y,z,vx,vy,vz);
		double d = sqrt(x*x+y*y+z*z);

		double vm = (vx*vx+vy*vy+vz*vz);
		double prod = (x*vx+y*vy+z*vz);
		//printf(" prod = %lf\n",prod);
		double px = -vx*prod/vm;
		double py = -vy*prod/vm;
		double pz = -vz*prod/vm;
		//printf("a projecao e' (%lf,%lf,%lf)\n",px,py,pz);
		double t = (px)/vx;
	//	printf("t preliminar = %lf\n",t);
		double dist = sqrt((px+x)*(px+x)+(py+y)*(py+y)+(pz+z)*(pz+z));
		if(t<0 || vm == 0){ t = 0;
			dist = d;
		}
		printf("Case #%d: %0.8lf %0.8lf\n",Case, dist,t);

	}
	return 0;
}
