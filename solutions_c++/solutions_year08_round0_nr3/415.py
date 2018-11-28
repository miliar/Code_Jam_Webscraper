#include<cstdio>
#include<cmath>
//#include<conio.h>

#define dist(x, y) sqrt(x*x+y*y)
#define find(x) sqrt(R*R-x*x)

double f, R, t, r, g, A, B, p[6][2];
int n;

double ar(){
	double ans=0.0;
	for(int i=n-1, j=0; j<n; i=j++)
		ans+=(p[i][0]+p[j][0])*(p[i][1]-p[j][1])/2.0;
	if(ans<0) ans=-ans;
	return ans;
}

void doit(double x){
	double y, d, tx, ty, theta=0.0, X=x;
	bool dia;
	for(int j=0; true; j++, n=0, theta=0.0, dia=false){
		//printf("trying new square\n");
        x=X; y=(2*r+g)*j+r+f;
        //printf("%lf, %lf\n", x, y);
		d=dist(x, y);
		if(R-d<1e-6) break;
		p[n][0]=x; p[n][1]=y;
		//printf("%lf %lf\n", p[n][0], p[n][1]); 
		n++;
		y+=g-2*f;
		d=dist(x, y);
		if(R-d>1e-6){
			p[n][0]=x; p[n][1]=y;
			//printf("%lf %lf\n", p[n][0], p[n][1]); 
			n++;
			x+=g-2*f;
			d=dist(x, y);
			if(R-d>1e-6){ 
				dia=true; p[n][0]=x; p[n][1]=y; 
				//printf("%lf %lf\n", p[n][0], p[n][1]); 
				n++;
			}
			else{
				tx=find(y);
				p[n][0]=tx; p[n][1]=y; 
				//printf("%lf %lf\n", p[n][0], p[n][1]); 
				n++;
				theta=atan(y/tx);
				//printf("theta 1 %lf\n", theta);
			}
		}
		else{
			ty=find(x);
			p[n][0]=x; p[n][1]=ty; 
			//printf("%lf %lf\n", p[n][0], p[n][1]);
			n++;
			theta=atan(ty/x);
			//printf("theta 2 %lf\n", theta);
			x+=g-2*f;
		}
		
		y-=g-2*f;
		d=dist(x, y);
		if(R-d>1e-6){
			if(!dia){
				ty=find(x);
				p[n][0]=x; p[n][1]=ty; 
				//printf("%lf %lf\n", p[n][0], p[n][1]);
				n++;
				theta-=atan(ty/x);
				//printf("theta 3 %lf\n", theta);
			}
            p[n][0]=x; p[n][1]=y;
			//printf("%lf %lf\n", p[n][0], p[n][1]);
			n++;
		}
		else{
            tx=find(y);
			p[n][0]=tx; p[n][1]=y; 
			//printf("ani %lf %lf\n", p[n][0], p[n][1]); 
			n++;
			theta-=atan(y/tx);
			//printf("theta 4 %lf\n", theta);
		}
		//printf("theta %lf\n", theta);
		B+=ar()+(theta-sin(theta))*R*R/2.0;
		//printf("%lf\n", B);
		//getch();
	}
	//getch();
	return;
}

int main(){
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
	int N;
	double x;
	scanf("%d", &N);
	//printf("%d\n", N);
	for(int k=1; k<=N; k++){
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		//printf("%f %f %f %f %f\n", f, R, t, r, g);
		if((g-2*f)<1e-6){ printf("Case #%d: %0.6f\n", k, 1.0); continue;}
		A=M_PI*R*R/4.0;
		//printf("A= %lf\n", A);
		R-=t+f;
		B=0.0; n=0;
		for(int i=0; true; i++){
			x=(2*r+g)*i+r+f;
			if(R-dist(x, r+f)<1e-6) break;
			doit(x);
		}
		//printf("B= %lf\n", B);
		printf("Case #%d: %0.6lf\n", k, (A-B)/A);
	}
	//getch();
	return 0;
}
