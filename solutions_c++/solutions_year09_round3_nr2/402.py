#include <stdio.h>
#include <math.h>

double p[500][3];
double v[500][3];

int main()
{
	double vm[3], pm[3];
	double A, B, C;
	double delta, t, d;
	int T, c, n, i;
	double N;
	scanf("%d",&T);
	c=1;
	while(T--){
		scanf("%d",&n);
		vm[0]=vm[1]=vm[2]=0; pm[0]=pm[1]=pm[2]=0;
		for(i=0;i<n;i++){
			scanf("%lf %lf %lf %lf %lf %lf",&p[i][0],&p[i][1],&p[i][2],&v[i][0],&v[i][1],&v[i][2]);
			pm[0]+=p[i][0]; pm[1]+=p[i][1]; pm[2]+=p[i][2];
			vm[0]+=v[i][0]; vm[1]+=v[i][1]; vm[2]+=v[i][2];
		}
		N=n;
		pm[0]/=N; pm[1]/=N; pm[2]/=N;
		vm[0]/=N; vm[1]/=N; vm[2]/=N;
		C=pm[0]*pm[0]+pm[1]*pm[1]+pm[2]*pm[2];
		B=2.0*(pm[0]*vm[0]+pm[1]*vm[1]+pm[2]*vm[2]);
		A=vm[0]*vm[0]+vm[1]*vm[1]+vm[2]*vm[2];
		delta=B*B-4.0*A*C;
		
		//printf("%lf %lf %lf\n",pm[0],pm[1],pm[2]);
		//printf("%lf %lf %lf\n",vm[0],vm[1],vm[2]);
		//printf("%lf %lf %lf %lf\n",A,B,C,delta);
		if(fabs(A)<1e-6){ 
			t=-1.0;
			if(B > 1e-6  && B < -1e-6){  t=-C/B; d=0;} 
			if(t<1e-6){ t=0; d=sqrt(C); } 
		}else{
			if(delta>=0.0){
				t=(-B-sqrt(delta))/(2.0*A);
				if(t<1e-10) t=(-B+sqrt(delta))/(2.0*A);
				d=0;
				if(t<1e-10){
					t=0;
					d=sqrt(C);
				}
			}else{
				d=-delta/(4.0*A);
				t=-B/(2.0*A);
				if(t<1e-10){t=0; d=sqrt(C); }
				else d=sqrt(d);
			}
		}
		
		printf("Case #%d: %.8lf %.8lf\n",c, d,t);
		c++;
	}
	
	return 0;
}

