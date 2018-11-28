#include <iostream>
#include <cstdio>

struct Tpoint {
	double x,y;
};

Tpoint l[110], u[110];

double Y(Tpoint p1, Tpoint p2, double mid)
{
	return p1.y + (p2.y - p1.y) * (mid - p1.x) / (p2.x - p1.x);
}

int main() 
{
	freopen("p1.in", "r", stdin);
	freopen("p1.out", "w", stdout);
	int T;
	std::cin >> T;
	double W;
	int L, U, G; 
	for (int t = 0; t < T; t++) {
		printf("Case #%d:\n", t + 1);	
		std::cin >> W >> L >> U >> G;
		for (int i = 0; i < L; i++) 
			std::cin >> l[i].x >> l[i].y;
		for (int i = 0; i < U; i++)
			std::cin >> u[i].x >> u[i].y;
		double miny = l[0].y;
		double maxy = u[0].y;
		for (int i = 0; i < L; i++)
			if (l[i].y < miny) miny = l[i].y;
		for (int i = 0; i < U; i++)
			if (u[i].y > maxy) maxy = u[i].y;
		double area1 = 0;
		for (int i = 1; i < L; i++) 
			area1 += (l[i].y  - miny + l[i - 1].y - miny) * (l[i].x - l[i - 1].x) / 2;
		for (int i = 1; i < U; i++)
			area1 += (maxy - u[i].y + maxy - u[i - 1].y) * (u[i].x - u[i - 1].x) / 2;
	    double area = W * (maxy - miny) - area1;
		double earea = area / G;
		double tarea = 0;
		int count = 0;
		int p1 = 1; int p2 = 1;
		double lt = u[0].y - l[0].y;
		double lx = 0;
		while (count < G - 1) {
			if (l[p1].x < u[p2].x) {
				if ((l[p1].x - lx) * (lt + Y(u[p2 - 1], u[p2], l[p1].x) - Y(l[p1 - 1], l[p1], l[p1].x)) / 2 + tarea > earea) {
					double min = lx;
					double max = l[p1].x;
					while (max - min > 1e-6) {
						double mid = (min + max) / 2;
						double ta = (mid - lx) * (lt + Y(u[p2 - 1], u[p2], mid) - Y(l[p1 - 1], l[p1], mid)) / 2;
						if (ta > earea - tarea) {
							max = mid;
						} else min = mid;
					}
					lx = min;
					lt = Y(u[p2 - 1], u[p2], min) - Y(l[p1 - 1], l[p1], min);
					count++;
					tarea = 0;
					printf("%0.7lf\n", lx);
				} else {
					tarea += (l[p1].x - lx) * (lt + Y(u[p2 - 1], u[p2], l[p1].x)  - Y(l[p1 - 1], l[p1], l[p1].x)) / 2;
							
					lx = l[p1].x;
				    lt = Y(u[p2 - 1], u[p2], lx) - Y(l[p1 - 1], l[p1], lx);
					p1 ++;
				}
			} else {
				if ((u[p2].x - lx) * (lt + Y(u[p2 - 1], u[p2], u[p2].x) - Y(l[p1 - 1], l[p1], u[p2].x)) / 2 + tarea > earea) {
					double min = lx;
					double max = u[p2].x;
					while (max - min > 1e-6) {
						double mid = (min + max) / 2;
						double ta = (mid - lx) * (lt + Y(u[p2 - 1], u[p2], mid) - Y(l[p1 - 1], l[p1], mid)) / 2;
						if (ta > earea - tarea) {
							max = mid;
						} else min = mid;
					}
					lx = min;
					lt = Y(u[p2 - 1], u[p2], min) - Y(l[p1 - 1], l[p1], min);
					count++;
					printf("%0.7lf\n", lx);
					tarea = 0;
				} else {
					tarea += (u[p2].x - lx) * (lt + Y(u[p2 - 1], u[p2], u[p2].x) - Y(l[p1 - 1], l[p1], u[p2].x)) / 2;
					lx = u[p2].x;
					lt = Y(u[p2 - 1], u[p2], lx) - Y(l[p1 - 1], l[p1], lx);
					p2++;
				}
			}
		}

	}
	return 0;
}