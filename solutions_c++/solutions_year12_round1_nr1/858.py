#include <cstdio>
#include <vector>
using namespace std;

#define pb push_back

int t, a, b;
double res, p, w;
vector<double> r;

int main() {
	scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		r.clear();
		w = 1.;
		printf("Case #%d: ", c);
		scanf("%d%d", &a, &b);
		for(int i = 0; i < a; i++) {
			scanf("%lf", &p);
			r.pb(p);
			w*=p;
		}
		res = b+2;
		res = min(res, w*(b-a+1)+(1.-w)*(b+b-a+2)); //p bez usuwania
		for(int i = a-1; i >= 0; i--) {
			w/=r[i];
			res = min(res, w*(b-a+1+(a-i)*2)+(1.-w)*(b+b-a+2+(a-i)*2));
		}
		printf("%.6f\n", res);
	}
	return 0;
}
