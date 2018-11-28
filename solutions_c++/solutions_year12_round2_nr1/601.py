
#include <cstdio>
using namespace std;

int nc, votes[205];
double after[205];

double opt(int xx, double tt) {
	double a=votes[xx], b=3*tt, c, rq;
	while (a+(1e-7)<b) {
		c=(a+b)/2;
		rq=0;
		for (int i=0; i<nc; i++) if (votes[i]<c) {
			rq += (c-votes[i])/tt;
		}
		if (rq>=1) { // safe
			b=c;
		} else {
			a=c;
		}
	}
	
	return (c-votes[xx])/tt;
}

void solve(int t) {
	scanf("%d",&nc);
	int tt=0;
	for (int c=0; c<nc; c++) {
		scanf("%d",votes+c);
		tt+=votes[c];
	}
	
	printf("Case #%d: ", t);
	for (int c=0; c<nc; c++) {
		printf("%.6lf ", opt(c, tt)*100);
	}
	printf("\n");
}

main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) 
		solve(t);
} 
