#include <algorithm>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long i64;
typedef long double d64;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif
const int maxn = 239;

double lx[maxn],ly[maxn],ux[maxn],uy[maxn];
double resx[maxn];
int L,U;

double Area(double x1,double y1,double x2,double y2){
	return fabs((y1+y2)*0.5*(x2-x1));
}
double calcArea(double left){
	double tarea = 0.;
	for(int i = 0 ; i+1 < U ; i++ ){
		if(left > ux[i+1] ){
			tarea += Area(ux[i],uy[i],ux[i+1],uy[i+1]);
		}else{
			double k = (left - ux[i])/(ux[i+1]-ux[i]);
			double tx = ux[i]+k*(ux[i+1]-ux[i]);
			double ty = uy[i]+k*(uy[i+1]-uy[i]);
			tarea+=Area(ux[i],uy[i],tx,ty);
			break;
		}
	}
	for(int i = 0 ; i+1 < L ; i++ ){
		if(left > lx[i+1] ){
			tarea -= Area(lx[i],ly[i],lx[i+1],ly[i+1]);
		}else{
			double k = (left - lx[i])/(lx[i+1]-lx[i]);
			double tx = lx[i]+k*(lx[i+1]-lx[i]);
			double ty = ly[i]+k*(ly[i+1]-ly[i]);
			tarea -=Area(lx[i],ly[i],tx,ty);
			break;
		}
	}
	return tarea;
}

double calc(double left,double right,double area){
	double tarea = calcArea(left);
	for(int iter = 0 ; iter < 50 ; iter++ ){
		double ave;
		ave = (left+right)/2.;
		double ar = calcArea(ave)-tarea;
		if(ar>area) right = ave ; else left = ave;
	}
	return left;
}

int main(){
	int T;scanf("%d",&T);
	for(int id = 1 ; id <= T ; id++ ){
		double w;
		scanf("%lf",&w);
		scanf("%d%d",&L,&U);
		int G;
		scanf("%d",&G);
		forn(i,L) scanf("%lf%lf",lx+i,ly+i),ly[i]+=10000.;
		forn(i,U) scanf("%lf%lf",ux+i,uy+i),uy[i]+=10000.;
		resx[0]=0.;
		double area = 0.;
		for(int i = 0 ; i+1 < U ; i++ ) area+=Area(ux[i],uy[i],ux[i+1],uy[i+1]);
		for(int i = 0 ; i+1 < L ; i++ ) area-=Area(lx[i],ly[i],lx[i+1],ly[i+1]);
		//eprintf("area = %lf\n",calcArea(w));
		for(int i = 1 ; i < G ; i++ ){
			resx[i] = calc(resx[i-1],w,area/G);
		}
		resx[G] = w;
		//for(int i = 0 ; i < G ; i++ ) eprintf("%.5lf\n",calcArea(resx[i+1])-calcArea(resx[i]));
		eprintf("%d\n",id);
		printf("Case #%d:\n",id);
		for(int i = 1 ; i < G ; i++ ) printf("%.20lf\n",resx[i]);
	}
	return 0;
}
