#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

int tc,n;
double x,y,z,vx,vy,vz;
double mind,mint;
int main(){
	int i,j,k;
	int ax,ay,az,bx,by,bz;
	FILE *in=fopen("in.txt","r");
	FILE *out=fopen("out.txt","w");

	fscanf(in,"%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		x=y=z=vx=vy=vz=0;
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++){
			fscanf(in,"%d %d %d %d %d %d",&ax,&ay,&az,&bx,&by,&bz);
			x+=ax;
			y+=ay;
			z+=az;
			vx+=bx;
			vy+=by;
			vz+=bz;
		}
		x/=n;
		y/=n;
		z/=n;
		vx/=n;
		vy/=n;
		vz/=n;
		if (vx*vx+vy*vy+vz*vz!=0){
			mint=(vx*x+vy*y+vz*z)/(vx*vx+vy*vy+vz*vz);
			if (mint<0) mint=-mint; else mint=0;
		}else{
			mint=0;
		}
		double xt,yt,zt;
		xt=x+vx*mint;
		yt=y+vy*mint;
		zt=z+vz*mint;
		mind=xt*xt+yt*yt+zt*zt;
		mind=sqrt(mind);
		fprintf(out,"Case #%d: %f %f\n",tcc,mind,mint);
	}
	return 0;
}