#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

#define MAXN 128
#define EPS 1E-9

typedef double tint;

int T;

struct pt {
	tint x, y;
	pt(tint xx=0.0, tint yy=0.0) {
		x=xx; y=yy;
	}
} l[MAXN], u[MAXN];

struct trap {
	tint xl, xr, ylu, yld, yru, yrd;
} t[2*MAXN];

tint interpolate(const pt &p, const pt &q, const tint x) {
	return p.y + (q.y - p.y)*(x - p.x)/(q.x - p.x);
}

tint trap_area(trap tt) {
	return (tt.xr-tt.xl)*(tt.ylu-tt.yld + tt.yru-tt.yrd)/2.0;
}

tint area(tint x) {
	int i;
	trap tmp;

	tint RES = 0.0;
	for (i=0; i<T && t[i].xr<=x; i++) {
		RES += trap_area(t[i]);
	}
	if (i < T && t[i].xl < x) {
		tmp.xl = t[i].xl;
		tmp.ylu = t[i].ylu;
		tmp.yld = t[i].yld;
		tmp.xr = x;
		tmp.yru = interpolate(pt(t[i].xl, t[i].ylu), pt(t[i].xr, t[i].yru), x);
		tmp.yrd = interpolate(pt(t[i].xl, t[i].yld), pt(t[i].xr, t[i].yrd), x);
		RES += trap_area(tmp);
	}
	return RES;
}

int main() {

freopen("in.txt", "r", stdin);

int i, j, L, U, G, K, k;
tint W, AREA, tmp, s, e, m;

cin >> K;

for (k=1; k<=K; k++) {

cin >> W;
cin >> L;
cin >> U;
cin >> G;

for (i=0; i<L; i++) {
	cin >> l[i].x;
	cin >> l[i].y;
}

for (j=0; j<U; j++) {
	cin >> u[j].x;
	cin >> u[j].y;
}

i = j = 1; T = 0;
while (i < L || j < U) {
	if (T > 0) {
		t[T].xl = t[T-1].xr;
		t[T].yld = t[T-1].yrd;
		t[T].ylu = t[T-1].yru;
	} else {
		t[T].xl = 0.0;
		t[T].yld = l[0].y;
		t[T].ylu = u[0].y;
	}

	t[T].xr = min(l[i].x, u[j].x);
	if (l[i].x - t[T].xr < EPS) {
		t[T].yrd = l[i].y;
		i++;
	} else t[T].yrd = interpolate(l[i-1], l[i], t[T].xr);

	if (u[j].x - t[T].xr < EPS) {
		t[T].yru = u[j].y;
		j++;
	} else t[T].yru = interpolate(u[j-1], u[j], t[T].xr);
	T++;
}

/*for (i=0; i<T; i++) {
	cout << t[i].xl << ' ' << t[i].xr << endl;
	cout << t[i].yld << ' ' << t[i].ylu << endl;
	cout << t[i].yrd << ' ' << t[i].yru << endl;
	cout << trap_area(t[i]) << endl << endl;
}*/

cout << "Case #" << k << ":" << endl;

AREA = area(W)/G;
for (i=1; i<=G-1; i++) {
	tmp = AREA*i;
	s = 0.0; e = W;
	while (e-s > EPS) {
		m = (s+e)/2.0;
		if (area(m) > tmp) e = m;
		else s = m;
	}
	printf("%.9lf\n", (s+e)/2.0);
}

}

return 0;
}
