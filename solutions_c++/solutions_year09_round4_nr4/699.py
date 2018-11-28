#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

double des(double x1, double y1, double x2, double y2){
	x1-=x2;
	y1-=y2;
	return sqrt(x1*x1+y1*y1);
}

int main(){
	int d, n;
	scanf("%d", &d);
	double a, b, c;
	int X[5], Y[5], R[5];
	for(int z=1; z<=d; z++){
		scanf("%d\n", &n);
		if(n==1){
			scanf("%d %d %d", &X[0], &Y[0], &R[0]);
			printf("Case #%d: %d\n", z, R[0]);
		}
		if(n==2){
			scanf("%d %d %d", &X[0], &Y[0], &R[0]);
			scanf("%d %d %d", &X[1], &Y[1], &R[1]);
			printf("Case #%d: %d\n", z, max(R[0], R[1]));
		}
		if(n==3){
			scanf("%d %d %d", &X[0], &Y[0], &R[0]);
			scanf("%d %d %d", &X[1], &Y[1], &R[1]);
			scanf("%d %d %d", &X[2], &Y[2], &R[2]);
			a=max((double)R[0], (des(X[1], Y[1], X[2], Y[2])+R[1]+R[2])/((double)(2)));
			b=max((double)R[1], (des(X[0], Y[0], X[2], Y[2])+R[0]+R[2])/((double)(2)));
			c=max((double)R[2], (des(X[1], Y[1], X[0], Y[0])+R[1]+R[0])/((double)(2)));
			printf("Case #%d: %.6lf\n", z, min(min(a, b), c));
		}
	}
}
