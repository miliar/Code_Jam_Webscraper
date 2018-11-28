#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<vector>
using namespace std;
struct XD{
    double x,y;
    XD(double xx=0,double yy=0):x(xx),y(yy){}
    bool operator<(const XD& b)const{
	return x<b.x;
    }
    void input(){scanf("%lf%lf",&x,&y);}
};
XD up[110],dow[110];
inline double ff(double a,double b,double ay,double by){
    return (ay*b+by*a)/(a+b);
}
inline double so(double a,double b,double c){if(fabs(a)<1e-7)return -c/b;return (-b+sqrt(b*b-4*a*c))/2/a;}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
	double w;
	int l,u,g;
	scanf("%lf%d%d%d",&w,&l,&u,&g);
	int i;
	for(i=0;i<l;i++)dow[i].input();
	for(i=0;i<u;i++)up[i].input();
	double tota=0;
	for(i=0;i<l-1;i++)tota-=(dow[i+1].x-dow[i].x)*(dow[i+1].y+dow[i].y)/2.0;
	for(i=0;i<u-1;i++)tota+=(up[i+1].x-up[i].x)*(up[i+1].y+up[i].y)/2.0;
	tota/=g;
	//printf("%lf\n",tota);
	double na=0;
	double nx=0;
	int ng=0;
	int uu=0,dd=0;
	double dy=up[uu].y-dow[dd].y;
	printf("Case #%d:\n",cas++);
	while(uu<u-1||dd<l-1){
	    double ndy;
	    double nnx;
	    if(up[uu+1].x<dow[dd+1].x){
		nnx=up[uu+1].x;
		ndy=up[uu+1].y-ff(dow[dd+1].x-nnx,nnx-dow[dd].x,dow[dd+1].y,dow[dd].y);
		uu++;
	    }else{
		nnx=dow[dd+1].x;
		ndy=-dow[dd+1].y+ff(up[uu+1].x-nnx,nnx-up[uu].x,up[uu+1].y,up[uu].y);
		dd++;
	    }
	    if(nnx<nx+1e-9)continue;
	    double aa=(dy+ndy)*(nnx-nx)/2.0;
	    //printf("%lf %lf %lf %lf\n",nx,nnx,dy,ndy);
	    while(ng<g-1&&(ng+1)*tota<na+aa){
		double la=tota*(ng+1)-na;
		double a=(ndy-dy)/(nnx-nx);
		printf("%.6lf\n",so(a,2*dy,-2*la)+nx);
		ng++;
	    }
	    dy=ndy;nx=nnx;
	    na+=aa;
	}
    }
}
