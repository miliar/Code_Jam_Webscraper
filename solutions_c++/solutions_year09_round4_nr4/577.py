#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

struct circle {
	double x, y, r;
};

FILE *fp_r, *fp_w;
int t, n;
vector<circle> v;
circle c;
double left, right, mid;
int use[40];

double dist(circle c1, circle c2) {
	return (sqrt((c1.x - c2.x) * (c1.x - c2.x) + (c1.y - c2.y) * (c1.y - c2.y)) + c1.r + c2.r) / 2.0;
}

int main() {
	fp_r = fopen("d.in", "r");
	fp_w = fopen("d.out", "w");

	fscanf(fp_r, "%d", &t);
	for(int i = 0; i < t; ++i) {
		fscanf(fp_r, "%d", &n);
		v.clear();
		for(int j = 0; j < n; ++j) {
			fscanf(fp_r, "%lf %lf %lf", &c.x, &c.y, &c.r);
			v.push_back(c);
		}

		if (n == 3) {
			fprintf(fp_w, "Case #%d: %.6lf\n", i+1, min(min(max(dist(v[0], v[1]), v[2].r), max(dist(v[0], v[2]), v[1].r)), max(dist(v[1], v[2]), v[0].r)));
		}
		else if (n == 2) {
			fprintf(fp_w, "Case #%d: %.6lf\n", i+1, max(v[0].r, v[1].r));
		}
		else if (n == 1) {
			fprintf(fp_w, "Case #%d: %.6lf\n", i+1, v[0].r);
		}
	}

	fclose(fp_w);
	fclose(fp_r);	

	return 0;
}