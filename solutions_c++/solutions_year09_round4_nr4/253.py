#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int N;

struct Circ {
	double x,y,r;
};

Circ circs[50];

double dist(Circ a, Circ b) {
	return sqrt( pow(a.x-b.x,2) + pow(a.y-b.y,2) );
}

double junta (Circ a, Circ b) {
	double d = dist(a,b);
	if (a.r >= d + b.r || b.r >= d + a.r) {
		return max(a.r, b.r);
	} else {
		return (d + a.r + b.r)/2;
	}
}

void process() {
	if (N == 1) {
		printf("%lf\n", circs[0].r);
	} else if (N==2) {
		printf("%lf\n", max(circs[0].r,circs[1].r));
	} else {
		// N == 3
		double c0 = junta(circs[1], circs[2]);
		double c1 = junta(circs[0], circs[2]);
		double c2 = junta(circs[0], circs[1]);
		
		c0 = max(c0, circs[0].r);
		c1 = max(c1, circs[1].r);
		c2 = max(c2, circs[2].r);
		
		printf("%lf\n", min(c0,min(c1,c2)));
		
	}
}

void read() {
	scanf("%d", &N);
	for (int i = 0 ; i < N ; i++) {
		scanf("%lf%lf%lf", &circs[i].x, &circs[i].y, &circs[i].r);
	}
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	int C;
	scanf("%d", &C);
	for (int i = 1 ; i <= C ; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}
