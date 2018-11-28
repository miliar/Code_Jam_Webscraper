#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

tipo arco(tipo x, tipo y, tipo r) {
	if (x >=r || y >= r || hypot(x, y)>=r) return 0.0;
	tipo ox = sqrt(r*r-y*y);
	tipo oy = sqrt(r*r-x*x);
	return  ((atan2(oy, x)-atan2(y, ox))*r*r)/2.0 - ((ox-x)*y + (oy-y)*x)/2.0;
}

tipo calc(tipo f, tipo r, tipo t, tipo d, tipo g) {
	t += f; if (t >= r) return 1.0;
	d += f; g -= 2*f;
	if (g <= 0.0) return 1.0;
	tipo ri = r-t;

	tipo x=d, y=d;
	tipo res = 0;
	while (y < ri) {
		x = d;
		while (x < ri) {
			res += arco(x, y, ri) + arco(x+g, y+g, ri) - (arco(x+g, y, ri) + arco(x, y+g, ri));
			x += g + 2*d;
		}
		y += g + 2*d;
	}
	return 1- (4*res)/(4*atan(1.0)*r*r);
}

int main() {
	int n;
	cin >> n;
	forn(tt, n) {
		tipo f, r, t, d, g;
		cin >> f >> r >> t >> d >> g;
		printf("Case #%d: %.8f\n", tt+1, (double)calc(f, r, t, d, g));
	}

//	cerr << arco(1, 0, 2) << endl;
	return 0;
}
