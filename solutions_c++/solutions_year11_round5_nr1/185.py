#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

int W,N,M,G;
double U[1000][2], D[1000][2];

double f(double sx, double ex) {
	int i;
	double area = 0,t,x1,x2,y1,y2;
	for(i=0;i+1<M;i++) {
		x1 = max(sx,U[i][0]);
		x2 = min(ex,U[i+1][0]);
		if(x1 < x2) {
			t = (U[i+1][1] - U[i][1])/(U[i+1][0] - U[i][0]);
			y1 = t*x1-t*U[i][0]+U[i][1];
			y2 = t*x2-t*U[i][0]+U[i][1];
			area += (y1+y2)*(x2-x1)/2;
		}
	}
	for(i=0;i+1<N;i++) {
		x1 = max(sx,D[i][0]);
		x2 = min(ex,D[i+1][0]);
		if(x1 < x2) {
			t = (D[i+1][1] - D[i][1])/(D[i+1][0] - D[i][0]);
			y1 = t*x1-t*D[i][0]+D[i][1];
			y2 = t*x2-t*D[i][0]+D[i][1];
			area -= (y1+y2)*(x2-x1)/2;
		}
	}
	return area;
}

void solve(int t) {
	int i,j;
	scanf("%d %d %d %d",&W,&N,&M,&G);
	for(i=0;i<N;i++) {
		scanf("%lf %lf",&D[i][0],&D[i][1]);
		D[i][1] += 1001;
	}
	for(i=0;i<M;i++) {
		scanf("%lf %lf",&U[i][0],&U[i][1]);
		U[i][1] += 1001;
	}
	double area = f(0,W)/G,lx=0;
	printf("Case #%d:\n",t);
	for(i=0;i+1<G;i++) {
		double st = lx, md, en = W;
		for(j=0;j<100;j++) {
			md = (st+en)/2;
			if( f(lx,md) > area ) en = md;
			else st = md;
		}
		lx = md;
		printf("%.9lf\n",lx);
	}
}

int main() {
	int t,T;
	double sec, tot;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		solve(t);
	}
	return 0;
}
