// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 210
using namespace std;
int w,Ln,Un,g,Lx[N],Ly[N],Ux[N],Uy[N];
double Lz[N],Uz[N];
void input() {
	scanf("%d%d%d%d",&w,&Ln,&Un,&g);
	for ( int i=0; i<Ln; i++ ) scanf("%d%d",Lx+i,Ly+i);
	for ( int i=0; i<Un; i++ ) scanf("%d%d",Ux+i,Uy+i);
}
double cal_y( double x, double x1, double y1, double x2, double y2 ) {
	double dx=x2-x1;
	double dy=y2-y1;
	double y3=y1+(x-x1)/dx*dy;
	return y3;
}
/*
double cal_dy( double x, double y, double x1, double y1, double x2, double y2 ) {
	return y-cal_y(x,x1,y1,x2,y2);
}
*/
/*
double cal_z() {
	for ( int i=0,j=0; i<Ln; i++ ) {
		while ( j<Un-1 && Ux[j+1]<=Lx[i] ) j++;
		Lz[i]=cal_dy(Lx[i],Ly[i],Ux[j],Uy[j],Ux[j+1],Uy[j+1]);
	}
	for ( int i=0,j=0; i<Un; i++ ) {
		while ( j<Ln-1 && Lx[j+1]<=Ux[i] ) j++;
		Uz[i]=cal_dy(Ux[i],Uy[i],Lx[j],Ly[j],Lx[j+1],Ly[j+1]);
	}
}
*/
double cal_area( int n, double x[N], double y[N] ) {
	double ret=0;
	x[n]=x[0];
	y[n]=y[0];
	for ( int i=0; i<n; i++ ) ret+=x[i]*y[i+1]-x[i+1]*y[i];
	ret/=2;
	if ( ret<0 ) ret=-ret;
	return ret;
}
double cal_all() {
	double x[N],y[N];
	int n=0,i;
	for ( i=0; i<Ln; i++ ) {
		x[n]=Lx[i];
		y[n]=Ly[i];
		n++;
	}
	for ( i=Un-1; i>=0; i-- ) {
		x[n]=Ux[i];
		y[n]=Uy[i];
		n++;
	}
	return cal_area(n,x,y);
}
double cal( double Mx ) { 
	//printf("Mx = %f\n",Mx);
	if ( Mx==0 ) return 0;
	double x[N],y[N];
	int n=0,i;
	for ( i=0; i<Ln&&Lx[i]<Mx; i++ ) {
		x[n]=Lx[i];
		y[n]=Ly[i];
		n++;
	}
	x[n]=Mx;
	y[n]=cal_y(Mx,Lx[i-1],Ly[i-1],Lx[i],Ly[i]);
	n++;
	for ( i=0; i<Un&&Ux[i]<Mx; i++ );
	x[n]=Mx;
	y[n]=cal_y(Mx,Ux[i-1],Uy[i-1],Ux[i],Uy[i]);
	n++;
	for ( i--; i>=0; i-- ) {
		x[n]=Ux[i];
		y[n]=Uy[i];
		n++;
	}
	return cal_area(n,x,y);
}
void solve() {
	static int cas=0;
	double all=cal_all();
	//printf("all = %f\n",all);
	double now=0,avg=all/g;
	printf("Case #%d:\n",++cas);
	//printf("avg = %f\n",avg);
	for ( int i=0; i<g-1; i++ ) {
		double L=now,M,R=w;
		while ( R-L>1e-7 ) {
			M=(L+R)/2;
			if ( cal(M)-cal(now)<avg ) L=M;
			else R=M;
			//printf("===%f\n",cal(M)-cal(now));
		}
		printf("%.9f\n",(L+R)/2);
		//printf("area = %f\n",cal((L+R)/2)-cal(now));
		now=(L+R)/2;
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	while ( T-- ) {
		input();
		//cal_z();
		solve();
	}
	return 0;
}
