#include <iostream>
#include <cmath>

using namespace std;

int a, n, m;
int ax, ay, bx, by, cx,cy;
int as;
void duantvienos() {
	int S = -1;
	for (int r = 0; r <= n; r++) 
	 for (int e = r + 1; r <= n; r++) 
	  for (int t = 0; t <= m; t++) {
		S = (e - r) * t;
		if (S == a) {cx = n; cy = t;}
		if (S == a) {ax = r; ay = by = 0; bx = e;}
		if (cx == ax && cy == ay) ax = -1;
	  }
}

int area(int tx, int ty, int rx, int ry, int ex ,int ey) {
	int abx = rx - tx, aby = ry - ty;
	int acx = ex - tx, acy = ey - ty;
	int rez = abx * acy - aby * acx;
	if (rez < 0) rez = rez * -1;
	return rez;
}

void antvienos() {
	int tax, tay, tbx, tby, tcx, tcy;
	for (int r1 = 0; r1 <= n; r1++)
		for (int r2 = 0; r2 <= m; r2++)
			for (int r3 = 0; r3 <= max(m,  n); r3++) {
				tax = r1; tay = 0; tbx = 0; tby = r2;
				if (r3 <= m) {
					tcx = n; tcy = r3;
					if ((int)area(tax, tay, tbx, tby, tcx, tcy) == a) 
						{ax = tax; ay = tay; bx = tbx; by = tby; cx = tcx; cy= tcy;}
				}
				if (r3 <= n) {tcy = m; tcx = r3;
					if ((int)area(tax, tay, tbx, tby, tcx, tcy) == a) 
						{ax = tax; ay = tay; bx = tbx; by = tby; cx = tcx; cy= tcy;}
					}
				if (cx == ax && cy == ay) ax = -1;
			}
}				

int main() {
	freopen("bsmall.in", "r", stdin);
	freopen("bsmall.out", "w", stdout);
	scanf("%d", &as);
	for (int f = 0; f < as; f++) {
		ax = -1;
		scanf("%d %d %d", &n, &m, &a);
		bool rasta = false;
		for (int gh = 0; gh < 2 && !rasta; gh++) {
//		swap(n, m);
		duantvienos();	
//		if (gh == 1 && ax != -1) {swap(ax, ay); swap(bx, by); swap(cx, cy);}
		if (!rasta && ax != -1) {printf("Case #%d: %d %d %d %d %d %d\n", f + 1, ax, ay, bx, by, cx, cy);rasta =true;}
			else {
		antvienos();
//		if (gh == 1 && ax != -1) {swap(ax, ay); swap(bx, by); swap(cx, cy);}
		if (!rasta && ax != -1) {rasta = true;printf("Case #%d: %d %d %d %d %d %d\n", f + 1, ax, ay, bx, by, cx, cy);}
		}}
		if (!rasta) printf("Case #%d: IMPOSSIBLE\n", f + 1);
	}	 
	return 0;
}
