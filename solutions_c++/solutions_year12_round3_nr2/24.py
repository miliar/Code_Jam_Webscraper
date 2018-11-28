#include <cstdio>
#include <vector>
#include <cmath>

#define mp make_pair
#define f first
#define s second

using namespace std;

const double eps = 1e-8;

vector<pair<double, double> > points;

void initIO() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int main() {
	initIO();
	int t;
	scanf("%d", &t);
	for (int ti=1; ti<=t; ti++) {
		printf("Case #%d:\n", ti);
		double D;
		int N, A;
		scanf("%lf%d%d", &D, &N, &A);
		points.clear();
		for (int i=0; i<N; i++) {
			double ti, xi;
			scanf("%lf%lf", &ti, &xi);
			points.push_back(mp(ti, xi));
		}
		for (int i=0; i<A; i++) {
			double acc, k=0;
			scanf("%lf", &acc);
			for (int j=0; j<points.size(); j++) {
				double a=points[j].f, b=points[j].s;
				if (b > D+eps && j) {
					double la = points[j-1].f, lb = points[j-1].s;
					double ratio = (D-lb) / (b-lb);
					a = (a-la)*ratio + la;
					b = (b-lb)*ratio + lb;
					double fastest = sqrt(b*2.0f/acc);
					k = max(k, a-fastest);
					break;
				}
				double fastest = sqrt(b*2.0f/acc);
				k = max(k, a-fastest);
				//printf("Fastest to %lf is %lf when acc is %lf\n", points[j].f, fastest, acc);
			}
			double tottime = sqrt(D*2.0f/acc);
			printf("%.7lf\n", tottime+k);
		}
	}
	return 0;
}
