#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

double PI;

#define DIST(x, y)	sqrt( (x) * (x) + (y) * (y) )

void calc(int no)
{
	double f, R, t, r, g;
	double S;
	double ans = 0;
	double x1, x2, y1, y2, cx1, cx2, cy1, cy2;
	double an1, an2, dan;
	double SH = 0, SS;
	int nx = -1, ny = -1;
	int ns = -1, max_s;
	int cnt = 0;
	
	
	cin >> f >> R >> t >> r >> g;
	
	S = R * R * PI;
	r += f;
	R -= t + f;
	g -= 2 * f;
	
	if (g <= 0) {
		goto out;
	}
	
	max_s = (int) ceil( (R + r) / (2 * r + g) );
	
	for (nx = 1; nx <= max_s; nx++) {
		for (ny = 1; ny <= max_s; ny++) {
			x2 = (2 * r + g) * nx - r;
			y2 = (2 * r + g) * ny - r;
			x1 = x2 - g;
			y1 = y2 - g;
			if (R >= DIST(x2, y2) ) {
				SS = g * g;
			} else if (R > DIST(x1, y1) ) {
				cnt++;
				if (R > DIST(x1, y2) ) {
					cy1 = y2;
					cx1 = sqrt(R * R - y2 * y2);
					if (R > DIST(x2, y1) ) {
						cx2 = x2;
						cy2 = sqrt(R * R - x2 * x2);
						SS = (g * g) - (x2 - cx1) * (y2 - cy2) / 2;
					} else {
						cy2 = y1;
						cx2 = sqrt(R * R - y1 * y1);
						SS = (g * (min(cx1, cx2) - x1) ) + g * fabs(cx2 - cx1) / 2;
					}
				} else {
					cx1 = x1;
					cy1 = sqrt(R * R - x1 * x1);
					if (R > DIST(x2, y1) ) {
						cx2 = x2;
						cy2 = sqrt(R * R - x2 * x2);
						SS = (g * (min(cy1, cy2) - y1) ) + g * fabs(cy2 - cy1) / 2;
					} else {
						cy2 = y1;
						cx2 = sqrt(R * R - y1 * y1);
						SS = (cy1 - y1) * (cx2 - x1) / 2;
					}
				}
				if (cx1 == 0) an1 = 0;
				else an1 = atan(cy1 / cx1);
				if (cx2 == 0) an2 = 0;
				else an2 = atan(cy2 / cx2);
				dan = fabs(an2 - an1);
				SS += R * R * dan / 2 - R * R * sin(dan) / 2;
				//printf("(%.2f,%.2f)-(%.2f,%.2f), (%.2f,%.2f)-(%.2f,%.2f), R = %.2f, dan = %.2f, SS = %.2f, %.2f\n",
				//x1, y1, x2, y2, cx1, cy1, cx2, cy2, R, dan, SS, g * g);
			} else SS = 0;
			//printf("(%.2f,%.2f)-(%.2f,%.2f), R = %.2f, %.2f, SS = %.2f\n",
			//	x1, y1, x2, y2, R, DIST(x2, y2), SS);
			SH += SS;
		}
	}
	
out:
	ans = (S - 4 * SH) / S;
	//printf("Case #%d: %.6f - cnt = %d, S - %.2f, SH - %.2f\n", no, ans, cnt, S, SH);
	printf("Case #%d: %.6f\n", no, ans);
	
	return;
}

int main()
{
	int n;
	int i;
	
	PI = acos(0) * 2;
	
	cin >> n;
	
	for (i = 0; i < n; i++) calc(i + 1);
	
	return 0;
}
