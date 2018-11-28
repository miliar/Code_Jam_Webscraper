#include <stdio.h>
#include <algorithm>

#define FORab(i,a,b) for(int i = (a); i < (b); i++)
#define FORn(i,n) FORab(i,0,n)
#define DBG(args...) /*fprintf(stderr, args)*/

 
using namespace std;
 
const int MAXN = 10000;
const double EPS = 1e-10;
 
double a[MAXN];
 
bool solvable(int n, double t, double d) {
	double x = a[0]-d;
	
	for (int i = 1; i < n; ++i) {
	  if (a[i]+d<x+t) return false;
	  x = max(a[i]-d,x+t);
	}
	return true;
}
 
void main2() {
	int C, D;
	scanf("%d %d", &C, &D);
	int k = 0;
	FORn(i,C) {
		int V, P;
		scanf("%d %d", &P, &V);
		FORn(j,V)
			a[k++] = P;
	}
	double lo = 0, hi = D*k;
	while (lo+EPS<hi) {
		double mid = (lo+hi)/2;
		if (solvable(k,D,mid))
			hi = mid;
		else
			lo = mid;
	}
	printf("%.12lf\n", lo);
}

int main() {
	int T; scanf("%d", &T);

	for(int caseno = 1; caseno <= T; caseno++) {
		printf("Case #%d: ", caseno);
		main2();
	}

	return 0;
}
