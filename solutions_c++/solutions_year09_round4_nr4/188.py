#include <cstdio>
#include <cmath>

const double eps = 1e-12;
const int dire[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

struct TC {
	int px, py, r;
};

int casei, cases, n;
double ans;
int cc[3];
TC c[10];

inline void init() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%d%d%d", &c[i].px, &c[i].py, &c[i].r);
}

inline double sqr(double now) {
	return now * now;
}

inline double getDis(double px1, double py1, double px2, double py2) {
	return sqrt(sqr(px1 - px2) + sqr(py1 - py2));
}

inline double calc(int c1, int c2, int r2) {
	double r1 = getDis(c[c1].px, c[c1].py, c[c2].px, c[c2].py) + c[c1].r + c[c2].r;
	r1 = r1 * 0.5;
	if (r1 < r2) return r2;
	else return r1;
}

inline double getR(double px, double py, int c1, int c2, int c3) {
	cc[0] = c1; cc[1] = c2; cc[2] = c3;
	double rtn = 0;
	for (int i = 0; i < 3; ++i) {
		double tmp = getDis(px, py, c[cc[i]].px, c[cc[i]].py) + c[cc[i]].r;
		if (tmp > rtn) rtn = tmp;
	}
	return rtn;
}

inline double dd(int c1, int c2, int c3) {
	double len = 100;
	double px = 0; double py = 0;
	while (len > eps) {
		double tmp = getR(px, py, c1, c2, c3);
		for (int i = 0; i < 4; ++i)
			while (true) {
				double tmp1 = getR(px + dire[i][0] * len, py + dire[i][1] * len, c1, c2, c3);
				if (tmp1 < tmp) {
					tmp = tmp1; 
					px += dire[i][0] * len; py += dire[i][1] * len;
				}
				else break;
			}
		len *= 0.5;
	}
	return getR(px, py, c1, c2, c3);
}

inline void process() {
	if (n == 1) {
		ans = c[0].r;
		return; 
	}
	ans = calc(0, 1, 0);
	if (n == 2) {
		int tmp;
		if (c[0].r < c[1].r) tmp = c[1].r;
		else tmp = c[0].r;
		if (tmp < ans) ans = tmp;
		return;
	}
	
	for (int i = 0; i < 3; ++i)
		for (int j = i + 1; j < 3; ++j) {
			double tmp = calc(i, j, c[3 - i - j].r);
			if (tmp < ans) ans = tmp;
		}
		
/*	
	for (int i = 0; i < n; ++i)
		for (int j = i + 1; j < n; ++j)
			for (int k = j + 1; k < n; ++k) {
				double tmp1 = dd(i, j, k);
				for (int i = 0; i < n; ++i)
					for (int j = i + 1; j < n; ++j)
						for (int k = j + 1; k < n; ++k) {
				
				if (tmp < ans) ans = tmp;
	}
*/
}

inline void print() {
	printf("Case #%d: %.7lf\n", casei, ans);
}

int main() {
//	freopen("in.txt", "r", stdin);

	freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-small-attempt2.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
	
	return 0;
}
