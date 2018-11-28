#include <iostream>
#include <math.h>
using namespace std;


int n,m;
int x[2], y[2];

double len(int x, int y) {
	return sqrt(x*x+y*y);
}

int main() {
	//freopen("circles.in","r",stdin);
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	double PI=acos(-1.0);
	int tests;
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++) {
		scanf("%d %d",&n,&m);
		for (int i=0;i<n;i++) scanf("%d %d",&x[i],&y[i]);
		printf("Case #%d:",test);
		for (int i=0;i<m;i++) {
			int x0,y0;
			scanf("%d %d",&x0,&y0);

			int ACx=x0-x[0], ACy=y0-y[0];
			int ABx=x[1]-x[0], ABy=y[1]-y[0];

			int BCx=x0-x[1], BCy=y0-y[1];
			int BAx=x[0]-x[1], BAy=y[0]-y[1];

			double r0=len(ACx,ACy);
			double r1=len(BCx,BCy);

			double alfa=2*acos((ACx*ABx+ACy*ABy)/len(ACx,ACy)/len(ABx,ABy));
			double beta=2*acos((BCx*BAx+BCy*BAy)/len(BCx,BCy)/len(BAx,BAy));

			double A1 = (1.0/2)*alfa*pow(r0,2) - (1.0/2)*pow(r0,2)*sin(alfa);
			double A2 = (1.0/2)*beta*pow(r1,2) - (1.0/2)*pow(r1,2)*sin(beta);

			printf(" %.9lf",A1+A2);
		}
		printf("\n");
		//printf("Case #%d: %d\n",test,t);
	}
    return 0;
}
