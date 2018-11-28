#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

#define maxn 2000
#define PI (2 * acosl(0.))

typedef long double real;

real sqr(real a){ return a * a;}

real calcsector(real ax, real ay, real bx, real by, real r){
	real anglea = atan2(ay, ax), angleb = atan2(by, bx);
	return r * r / 2. * fabs(anglea - angleb) - fabs(ax * by - ay * bx) / 2.;
}

real calc(real ax, real ay, real bx, real by, real r){
	if (sqr(bx) + sqr(by) <= r * r) return (bx - ax) * (by - ay);
	if (sqr(ax) + sqr(ay) >= r * r) return 0.;
	if (sqr(ax) + sqr(by) > r * r && sqr(bx) + sqr(ay) > r * r){
		real cy = sqrt(r * r - ax * ax);
		real dx = sqrt(r * r - ay * ay);
		return (cy - ay) * (dx - ax) / 2. + calcsector(ax, cy, dx, ay, r);
	}else
	if (sqr(ax) + sqr(by) > r * r && sqr(bx) + sqr(ay) <= r * r){
		real cy = sqrt(r * r - ax * ax);
		real dy = sqrt(r * r - bx * bx);
		return (bx - ax) * (cy - ay + dy - ay) / 2. + calcsector(ax, cy, bx, dy, r);
	}else
	if (sqr(ax) + sqr(by) <= r * r && sqr(bx) + sqr(ay) > r * r){
		real cx = sqrt(r * r - by * by);
		real dx = sqrt(r * r - ay * ay);
		return (by - ay) * (cx - ax + dx - ax) / 2. + calcsector(cx, by, dx, ay, r);
	}else{
		real cx = sqrt(r * r - by * by);
		real dy = sqrt(r * r - bx * bx);
		return (bx - ax) * (by - ay) - (bx - cx) * (by - dy) / 2. + calcsector(cx, by, bx, dy, r);
	}
}

int main(){
	int ferlon;
	scanf("%d", &ferlon);
	for (int _ = 0; _ < ferlon; ++_){
		real f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
		int i, j;
		real res = 0.;
		if (2 * f < g){
			for (i = 0; ; ++i){
				for (j = 0; ; ++j){
					real ax, ay, bx, by;
					ay = i * (g + 2 * r) + r;
					ax = j * (g + 2 * r) + r;
					bx = ax + g;
					by = ay + g;
					if (ax * ax + ay * ay > (R - t) * (R - t)) break;
					res += calc(ax + f, ay + f, bx - f, by - f, R - t - f);
				}
				if (j == 0) break;
			}	
		}
		res = 1. - 4. * res / R / R / PI;
		printf("Case #%d: %.6lf\n", _ + 1, (double)res);
	}
	return 0;
}	
