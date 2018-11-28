#include <stdio.h>
#include <memory.h>
#include <vector>
#include <algorithm>
#define MN 1000000
#define ll long long
#define eps 1e-06
using namespace std;
int n;
double D;
int d[MN];
bool help(double x) {
	double p, q;
	int i, j, k;

	p = d[0]-x-D;
	for (i = 0; i < n; i++) {
		if (p+D < d[i]-x-eps) {
			p = d[i]-x;
		}
		else if (p+D > d[i]+x+eps) {
			return 0;
		}
		else {
			p = p+D;
		}
	}
	return 1;
}
int main()
{
	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	FILE *out=fopen("output.txt","w");
	int t, T, r, i, j, k;
	char str[4];
	double s, e, m;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		fprintf(out,"Case #%d: ",t);
		int p;
		scanf("%d%lf",&p,&D);
		s = e = 0;
		n = 0;
		for (i = 0; i < p; i++) {
			scanf("%d%d",&j,&k);
			e += k;
			while (k--) d[n++] = j;
		}
//		e *= D+d.back()-d.front();
		e *= D;
		for (p = 0; p < 100; p++) {
			m = (s+e)/2;
			if (help(m)) e = m;
			else s = m;
//			printf("%lf %lf %lf\n",s,e,m);
		}
		fprintf(out,"%.10lf\n",e+eps);
		printf("%d\n",t);
	}
	return 0;
}