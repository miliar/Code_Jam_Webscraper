#include <cstdio>
#include <cmath>

using namespace std;

int l1[10002], l2[10002], u1[10002], u2[10002];
double sy[1000002];
int sx[1000002];

bool eq(double a, double b) {
	if (abs(a-b) < 0.0001) return 1;
	else return 0;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++) {
		int w, l, u, g;
		scanf("%d %d %d %d", &w, &l, &u, &g);
		for (int x=1; x<=l; x++) scanf("%d %d", &l1[x], &l2[x]);
		for (int x=1; x<=u; x++) scanf("%d %d", &u1[x], &u2[x]);
		int p1 = 1, p2 = 1, p = 0;
		while (1) {
			if (l1[p1] == u1[p2]) {
				sy[p] = u2[p2]-l2[p1];
				sx[p] = l1[p1];
				p++;
				if (l1[p1] == w) break;
				p1++;
				p2++;
			} else if (l1[p1] < u1[p2]) {
				
				sy[p] = (double)(u2[p2]-u2[p2-1])/(u1[p2]-u1[p2-1])*(l1[p1]-u1[p2-1]) + u2[p2-1]-l2[p1];
				sx[p] = l1[p1];
				p++;
				p1++;
			} else {
				sy[p] = u2[p2]-l2[p1-1]-(double)(l2[p1]-l2[p1-1])/(l1[p1]-l1[p1-1])*(u1[p2]-l1[p1-1]);
				sx[p] = u1[p2];
				p++;
				p2++;
			}
		}
		printf("Case #%d:\n", i);
		for (int j=0; j<p; j++) {
			//printf("%d %llf\n", sx[j], sy[j]);	
		}
		double total = 0;
		for (int j=1; j<p; j++) total += (sy[j]+sy[j-1])*(sx[j]-sx[j-1])/2;
		double mean = total/g;
		double curx=0, cury=sy[0], cura=0;
		int cnt = 1;
		int j = 0;
		while (cnt < g) {
			while (sx[j] <= curx) j++;
			double slope = (sy[j]-cury)/(sx[j]-curx);
			if (eq(cura+(sy[j]+cury)*(sx[j]-curx)/2, mean)) {
				curx = sx[j];
				cury = sy[j];
				printf("%llf\n", curx);
				cura = 0;
				cnt++;
			} else if (cura+(sy[j]+cury)*(sx[j]-curx)/2 < mean) {
				cura += (sy[j]+cury)*(sx[j]-curx)/2;
				curx = sx[j];
				cury = sy[j];
			} else if (eq(slope, 0)) {
				curx += (mean-cura)/cury;
				printf("%llf\n", curx);
				cura = 0;
				cnt++;
			} else {
				long double x = (-cury + sqrt(cury*cury-2*slope*(cura-mean)))/(slope);
				cury += x*slope;
				curx += x;
				printf("%llf\n", curx);
				cura = 0;
				cnt++;
			}
			//printf("%f %f %f\n", curx, cury, cura);
		}
	}
	return 0;
}
