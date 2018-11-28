#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <assert.h>
#include <math.h>
using namespace std;

#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MOD(a,b) (((a)%(b)+(b))%(b))

int T;

int W, L, U, G;
long double xl[1000];
long double yl[1000];
long double xu[1000];
long double yu[1000];

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d:\n", test+1);
		scanf("%d %d %d %d", &W, &L, &U, &G);
		long double area = 0;
		for (int i = 0; i < L; i++) {
			scanf("%Lf %Lf", &xl[i], &yl[i]);
			if (i > 0)
				area -= 0.5*(xl[i]-xl[i-1])*(yl[i]+yl[i-1]);
		}
		for (int i = 0; i < U; i++) {
			scanf("%Lf %Lf", &xu[i], &yu[i]);
			if (i > 0)
				area += 0.5*(xu[i]-xu[i-1])*(yu[i]+yu[i-1]);
		}
		area /= G;
		for (int i = 0; i < G-1; i++) {
			long double s = 0, e = W;
			while(e > s+1E-10) {
				long double x = (s+e)/2;
				long double want = area*(i+1);
				for (int i = 0; i < U-1 && xu[i] < x; i++) {
					if (xu[i+1] <= x) {
						want -= 0.5*(xu[i+1]-xu[i])*(yu[i+1]+yu[i]);
					} else {
						want -= 0.5*(x-xu[i])*((yu[i+1]-yu[i])/(xu[i+1]-xu[i])*(x-xu[i])+2*yu[i]);
					}
				}
				for (int i = 0; i < L-1 && xl[i] < x; i++) {
					if (xl[i+1] <= x) {
						want += 0.5*(xl[i+1]-xl[i])*(yl[i+1]+yl[i]);
					} else {
						want += 0.5*(x-xl[i])*((yl[i+1]-yl[i])/(xl[i+1]-xl[i])*(x-xl[i])+2*yl[i]);
					}
				}
				if (want > 0)
					s = x;
				else
					e = x;
			}
			printf("%Lf\n", s);
		}
	}
	return 0;
}
