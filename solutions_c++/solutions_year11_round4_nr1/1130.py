#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

int testc() {
	int x,s,r,n;
	double t;
	VPII f;
	scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
	double rest = x;
	for (int i=0; i<n; ++i) {
		int b,e,w;
		scanf("%d%d%d", &b, &e, &w);
		f.push_back(PII(w,e-b));
		rest -= e-b;
	}

	sort(&f[0], &f[n]);
	
	double time = 0;

	double ss = r * t;
	if (ss > rest) {
		double tt = rest / (double)r;
		t -= tt;
		time += tt;
	} else {
		time += t;
		rest -= ss;
		t = 0;

		time += rest / (double)s;
	}

	for (int i=0; i<n; ++i) {
		rest = f[i].second;
		double w = f[i].first;
		ss = (r+w) * t;
		if (ss > rest) {
			double tt = rest / (double)(r+w);
			t -= tt;
			time += tt;
		} else {
			time += t;
			rest -= ss;
			t = 0;

			time += rest / (double)(s+w);
		}


	}

	printf(" %.12lf\n", time);
}

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		printf("Case #%d:",c);
		testc();
	}
	return 0;
}
