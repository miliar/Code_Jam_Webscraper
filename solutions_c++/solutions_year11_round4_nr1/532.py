#include <cstdio>
#include <algorithm>
#include <cstring>
#define FOR(i,s,e) for (int i=(s); i<(int)(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(int)(e); i++)
using namespace std;

struct seg{
	int l, s1, s2;
	double r;
	bool operator < (seg const &T) const{return r > T.r;}
}	a[1005];

int tc, m, v1, v2, vt, n, L, st, ed, ad;
double t, rem, ret, s;



int main(){

	scanf("%d", &tc);
	FOE(c,1,tc){

		scanf("%d%d%d%d%d", &m, &v1, &v2, &vt, &n);
		L = m;
		FOR(i,0,n){
			scanf("%d%d%d", &st, &ed, &ad);
			a[i].l = ed - st;
			L -= a[i].l;
			a[i].s1 = v1 + ad;
			a[i].s2 = v2 + ad;
			a[i].r = a[i].s2 * 1. / a[i].s1;
		}
		
		a[n].l = L;
		a[n].s1 = v1;
		a[n].s2 = v2;
		a[n++].r = a[n].s2 * 1. / a[n].s1;
		
		sort(a, a + n);
		ret = 0;
		rem = vt;
		FOR(i,0,n){
			t = min(rem, a[i].l * 1. / a[i].s2);
			rem -= t;
			ret += t;
			s = a[i].l - t * a[i].s2;
			ret += s / a[i].s1;
		}
		
		printf("Case #%d: %.9f\n", c, ret+1e-11);

	}

	return 0;
}
