#include <cstdio>
#include <cmath>
#include <cstring>

int fx[600],fy[600],fz[600];
int vx[600],vy[600],vz[600];
double x1,x2,yy1,y2,z1,z2,vvx,vvy,vvz;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int q;
	scanf("%d",&q);
	for(int k=1;k<=q;k++){
		int n,i;
		scanf("%d",&n);
		x1=x2=yy1=y2=z1=z2=vvx=vvy=vvz=0.0;
		for(i=0;i<n;i++){
			scanf("%d%d%d%d%d%d",&fx[i],&fy[i],&fz[i],&vx[i],&vy[i],&vz[i]);
			x1+=fx[i];
			yy1+=fy[i];
			z1+=fz[i];
			vvx+=vx[i];
			vvy+=vy[i];
			vvz+=vz[i];
		}
		vvx/=n;
		vvy/=n;
		vvz/=n;
		x1/=n;
		yy1/=n;
		z1/=n;
		if(fabs(vvx*vvx+vvy*vvy+vvz*vvz)<1e-8){
			double d=sqrt(x1*x1+yy1*yy1+z1*z1);
			printf("Case #%d: %.9lf %.9lf\n",k,d,0);
			continue;
		}
		double t=(vvx*x1+vvy*yy1+vvz*z1)/(vvx*vvx+vvy*vvy+vvz*vvz);
		t=-t;
		if(t<0)t=0;
		x1+=t*vvx;
		yy1+=t*vvy;
		z1+=t*vvz;
		double d=sqrt(x1*x1+yy1*yy1+z1*z1);
		printf("Case #%d: %.9lf %.9lf\n",k,d,t);
	}

	return 0;
}
