#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef long double ld;

const ld pi = 2 * acos(0);

// sektors (taisna leņķa šķēlums ar riņķi)
ld arsc(ld x, ld y, ld r) {
	if (x * x + y * y >= r * r) return 0;
	
	ld xy = sqrtl(r * r - y * y), yx = sqrtl(r * r - x * x), a = atan2(yx, x) - atan2(y, xy);
	
	return (xy - x) * (yx - y) / 2 + r * r * a / 2 - r * r * sin(a) / 2;
}

// kvadrāta šķēlums ar riņķi: kreisais apakšējais stūris (plus muša), mala (mīnus muša), iekšējais rādiuss (mīnus muša)
ld arin(ld x, ld y, ld s, ld r) {
	return arsc(x, y, r) - arsc(x + s, y, r) - arsc(x, y + s, r) + arsc(x + s, y + s, r);
}

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		ld f, R, t, r, g, p, a;
		int i, j;
		
		cin >> f >> R >> t >> r >> g;
		if (2 * f >= g || f >= R - t) {
			p = 1;
		} else {
			p = 0;
			for (i = 0; i < 1000; i++) for (j = 0; a = arin(i * (r + r + g) + r + f, j * (r + r + g) + r + f, g - f - f, R - t - f); j++) p += a;
			p = 1 - p / (pi * R * R / 4);
		}
		
		cout << "Case #" << it << ": " << setprecision(40) << fixed << p << '\n';
	}
	
	return 0;
}
