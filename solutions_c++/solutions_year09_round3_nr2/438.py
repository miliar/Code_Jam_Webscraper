#include<stdio.h>
#include<algorithm>
#include<math.h>

using namespace std;


int t,tc;
int n;
double x,y,z,vx,vy,vz;
double tx,ty,tz,tvx,tvy,tvz;
double l,r,mid;
double res,ran;
double tp,tp2;
double an;
int i,j;
//double pi=atan(0.0);
double cp;
double v;
double dx,dy,dz;
double d;
double tr;
double a,c;

double cross(double tx,double ty,double tz, double tvx, double tvy, double tvz){
	double dx,dy,dz;
	dx=(ty*tvz - tvy*tz);
	dy=-1*(tx*tvz - tvx*tz);
	dz=(tx*tvy - tvx*ty);
	return 	sqrt((dx*dx) + (dy*dy) + (dz*dz));
}

int main(){
	freopen("cm1.in","r",stdin);
	freopen("cm1.out","w",stdout);
	scanf("%d",&t);
	for(tc=1;tc<=t;tc++){
		scanf("%d",&n);
		tx=0;ty=0;tz=0;
		tvx=0;tvy=0;tvz=0;
		for(i=0;i<n;i++){
			scanf("%lf %lf %lf %lf %lf %lf",&x,&y,&z,&vx,&vy,&vz);
			//printf("%lf %lf %lf %lf %lf %lf\n",x/n,y/n,z/n,vx/n,vy/n,vz/n);
			tx+=(x/n);
			ty+=(y/n);
			tz+=(z/n);
			tvx+=(vx/n);
			tvy+=(vy/n);
			tvz+=(vz/n);
		}
		//for(i=0;i<n;i++){printf("%lf %lf %lf %lf %lf %lf\n",x,y,z,vx,vy,vz);};
		//printf("%lf %lf %lf %lf %lf %lf\n",tx,ty,tz,tvx,tvy,tvz);
		l=0;
		r=1;
		res=r;
		//ran=pi;
		/*
		for(j=0;j<1000000;j++){
			mid = (l+r) /2;
			//tp=sqrt( ((tx+(tvx*mid))*(tx+(tvx*mid))) + ((ty+(tvy*mid))*(ty+(tvy*mid))) +((tz+(tvz*mid))*(tz+(tvz*mid))) );
			//tp2=sqrt( (((tvx*mid))*((tvx*mid))) + (((tvy*mid))*((tvy*mid))) +(((tvz*mid))*((tvz*mid))) );
			
		}*/
		cp=cross(tx,ty,tz,tvx,tvy,tvz);
		//cp=sqrt((dx*dx) + (dy*dy) + (dz*dz));
		v=sqrt( tvx*tvx + tvy*tvy + tvz*tvz );
		d=cp/v;
		/*
		dx=(ty*tvz - tvy*tz);
		dy=-1*(tx*tvz - tvx*tz);
		dz=(tx*tvy - tvx*ty);
		tr = cross(tx,ty,tz,dx/tvx,dy/tvy,dz/tvz)/d;
		*/
		c=sqrt( tx*tx + ty*ty + tz*tz );
		a= sqrt(c*c - (d*d));
		tr=a/v;
		double cek= sqrt( ((tx+(tvx*tr))*(tx+(tvx*tr))) + ((ty+(tvy*tr))*(ty+(tvy*tr))) +((tz+(tvz*tr))*(tz+(tvz*tr))) );
		
		if((fabs(v)<=1e-10)||(c-cek<0)){
			printf("Case #%d: %.8lf %.8lf\n",tc,c,0);
		}
		else{
			printf("Case #%d: %.8lf %.8lf\n",tc,d,tr);
		}
	}

	return 0;
}