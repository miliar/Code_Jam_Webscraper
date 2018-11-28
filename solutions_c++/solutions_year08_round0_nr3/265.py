#include <stdio.h>
#include <iostream.h>
#include <math.h>
#include <assert.h>

const double PPI=2*acos(0);
double f,R,t,r,g;

double circ(double t){
	return t/2*R*R-.5*R*R*sin(t);
}

double circ1(double x1, double y1, double x2, double y2){
	return circ((atan(y2/x2)-atan(y1/x1)));
}

int inside(double x, double y){
	if (x*x+y*y<R*R) return 1;
	return 0;
}

double px[5],py[5];
int pn;

double polyarea(){
	int i;
	double area=0;
	for (i=0; i<pn; i++){
		//    printf("|| %.2lf %.2lf\n",px[i],py[i]);
		area+=(px[i]*py[(i+1)%pn]-py[i]*px[(i+1)%pn]);
	}
	return (area)/2;
}

double getArea(double x, double y){
	double x1=10,y1=0,x2=10,y2=0;
	if (!inside(x,y)) return 0;
	pn=1;
	px[0]=x;
	py[0]=y;
	int last=1;
	/*int ptx[]={x,x+g,x+g,x,x},pty[]={y,y,y+g,y+g,y};
	for (int i=1; i<5; i++){
		int now=inside(ptx[i],pty[i]);
		if (now==0 && last==0);
		else if (
	}*/
	
	//right bot
	if (inside(x+g,y)){
		px[pn]=x+g; py[pn]=y; 
		pn++; last=1;
	}
	else{
		y1=y2=py[pn]=y; 
		x1=x2=px[pn]=sqrt(R*R-y*y);
		pn++; 	last=0;
	}
	//right top
	if (inside(x+g,y+g)){
		assert(last==1);
		px[pn]=x+g; py[pn]=y+g;
		pn++;		last=1;
	}
	else if (last==1){
		assert(R>=x+g);
		y1=y2=py[pn]=sqrt(R*R-(x+g)*(x+g));
		x1=x2=px[pn]=x+g;
		pn++;
		last=0;
	}
	//top
	if (inside(x,y+g)){
		if (last==0){
			assert(R>=y+g);
			x2=px[pn]=sqrt(R*R-(y+g)*(y+g));
			y2=py[pn]=y+g;
			pn++;
		}
		px[pn]=x;
		py[pn]=y+g;
		pn++;
		last=1;
	}
	else{
		assert(last==0);
		last=0;
	}
	//bott
	if (last==0){
		x2=px[pn]=x;
		y2=py[pn]=sqrt(R*R-x*x);
		pn++;
		last=1;
	}
	return polyarea()+circ1(x1,y1,x2,y2);
}

int main(){
	int l,u;
	double p=0;
	//freopen("in.txt","rt",stdin);
	scanf("%d",&l);
	for (u=0; u<l; u++){
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		if (t>=R || 2*f>=g) p=1;
		else{
			t+=f;
			R-=t;
			g-=2*f;
			r+=f;
			double x,y,a=0;
			for (x=r; x<R; x+=2*r+g){
				for (y=r; y<R; y+=2*r+g)
					a+=getArea(x,y);
			}
			double tot=PPI*(R+t)*(R+t)/4;
			p=(tot-a)/tot;
			//printf("tot=%lf\n",tot);
		}
		printf("Case #%d: %.09lf\n",u+1,p);
	}
	return 0;
}
