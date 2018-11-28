#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define eps 1e-8
#define oo 1e9


using namespace std;

typedef struct{
	double x, y, z;
}aa;

int T, m, n, q, w, mi, ma, cnt, fi, cc, e,  z, an;
aa a[1010];
double S, t, x, s, r, xx;

bool ss(aa x, aa y){
	return (x.z < y.z);
}

int main(){
	scanf("%d", &T);
	for (int rr=1; rr<=T; rr++){
		S = 0;
		printf("Case #%d: ", rr);
		scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &m);
		t *= r;
		for (int i=0; i<m; i++)
			scanf("%lf%lf%lf", &a[i].x, &a[i].y, &a[i].z);
		sort(a, a+m, ss);
		xx = x;
		for (int i=0; i<m; i++)
			xx -= (a[i].y - a[i].x);
		if (xx >= t){
			for (int i=0; i<m; i++){
				S += ((double)a[i].y - a[i].x)/((double)a[i].z + (double)s);
			}
			S += (double)t/(double)r;
			S += ((double)xx - (double)t)/s;
		} else {
			t /= (double)r;
			S += (double)xx/(double)r;
			t -= (double)xx/(double)r;
			fi = 1;
			for (int i=0; i<m; i++){
				if (t - ((double)a[i].y - (double)a[i].x)/((double)a[i].z + r) >= 0){
					t -= ((double)a[i].y - (double)a[i].x)/((double)a[i].z + r);
					S += ((double)a[i].y - (double)a[i].x)/((double)a[i].z + r);
				} else {
					if (fi == 1) {
						S += t;
						S += ((a[i].y - a[i].x - ((double)a[i].z+(double)r)*t)/((double)a[i].z+(double)s));
						fi = 0;
						t = -1;
					} else
					S += ((double)(a[i].y - a[i].x))/((double)a[i].z + s);
				}
			}
		}
		printf("%.9f\n", S);
	}
	return 0;
}
