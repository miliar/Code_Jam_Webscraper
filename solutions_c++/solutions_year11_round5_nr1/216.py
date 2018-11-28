#include <cstdio>

double lx1[110], ly1[110], ux1[110], uy1[110], x[210], uy[210], ly[210], dy[210];
void work() {
	int w, l, u, g;
	scanf("%d%d%d%d", &w, &l, &u, &g);
	for (int i = 0; i < l; ++i) {
		scanf("%lf%lf", &lx1[i], &ly1[i]);
	}
	for (int i = 0; i < u; ++i) {
		scanf("%lf%lf", &ux1[i], &uy1[i]);
	}

	int i = 0, j = 0, n = 0;
	while (i < l || j < u) {
		if (lx1[i] == ux1[j]) {
			x[n] = lx1[i];
			ly[n] = ly1[i];
			uy[n] = uy1[j];
			dy[n] = uy[n] - ly[n];
			i++;j++;
		} else if (lx1[i] < ux1[j]) {
			x[n] = lx1[i];
			ly[n] = ly1[i];
			uy[n] = uy1[j - 1] + (uy1[j] - uy1[j - 1]) *
				(x[n] - ux1[j - 1]) / (ux1[j] - ux1[j - 1]);
			i++;
			dy[n] = uy[n] - ly[n];
		} else {
			x[n] = ux1[j];
			uy[n] = uy1[j];
			ly[n] = ly1[i - 1] + (ly1[i] - ly1[i - 1]) *
				(x[n] - lx1[i - 1]) / (lx1[i] - lx1[i - 1]);
			j++;
			dy[n] = uy[n] - ly[n];
		}
		n++;
	}
	double s = 0;
	n--;
	for (int i = 0; i < n; ++i) {
		s += (dy[i] + dy[i + 1]) * (x[i + 1] - x[i]) / 2;
	}
	s /= g;

	i = 0;
	double cx = 0, cy = uy[0] - ly[0];
	int k = 1;
	double d = s;
	while (k < g) {
		double s2 = (cy + dy[i + 1]) * (x[i + 1] - cx) / 2;
		if (s2 < d) {
			cx = x[i + 1];
			cy = uy[i + 1] - ly[i + 1];
			++i;
			d -= s2;
		} else {
			double low = cx, high = x[i + 1];
			while (high - low > 1e-8) {
				double c = (low + high) / 2;
				double y = dy[i] + 
					(dy[i + 1] - dy[i]) * (c - x[i]) / (x[i + 1] - x[i]);
				if ((y + cy) * (c - cx) / 2 > d)
					high = c;
				else
					low = c;
			}
			cx = high;
			cy = dy[i] + (dy[i + 1] - dy[i]) * (cx - x[i]) / (x[i + 1] - x[i]);
			printf("%.6lf\n", cx);
			++k;
			d = s;
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d:\n", i + 1);
		work();
	}
}
