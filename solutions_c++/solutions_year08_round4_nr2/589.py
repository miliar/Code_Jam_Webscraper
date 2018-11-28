#include<iostream>
#include<cmath>
#define eps 1e-9
using namespace std;
struct point {
	double x, y;
};

double operator*(point p1, point p2) {
    return p1.x * p2.y - p1.y * p2.x;
}

point operator-(point p1, point p2) {
    point p;
    p.x = p1.x - p2.x;
    p.y = p1.y - p2.y;
    return p;
}
double getarea (point p1, point p2, point p3) {
    return fabs ((p1 - p2) * (p3 - p2)) / 2.0;
}
int main(){
	freopen("b.out", "w", stdout);
	int cnt;
	scanf("%d", &cnt);
	for (int  t = 1; t <= cnt; t++){
		int n, m;
		double a;
		scanf("%d%d%lf", &n, &m, &a);
		int flag = 0;
		point p1, p2, p3;
	//	if (m * n < a) {
	//		printf("Case #%d: IMPOSSIBLE\n", t);
	//		continue;
	//	}
	//	for (int x1 = 0; x1 <= n && !flag; x1++)
		//for (int y1 = 0; y1 <= m && !flag; y1++)
				for (int x2 = 0; x2 <= n && !flag; x2++)
					for (int y2 = 0; y2 <= m && !flag; y2++)
						for (int x3 = 0; x3 <= n && !flag; x3++)
							for (int y3 = 0; y3 <= m && !flag; y3++){
								p1.x = 0.0;
								p1.y = 0.0;
								p2.x = (double)x2;
								p2.y = (double)y2;					
								p3.x = (double)x3;
								p3.y = (double)y3;
								double ans = getarea(p1, p2, p3);
								if (fabs(ans - a / 2.0) < eps)
									flag = 1;
							}
		if (!flag)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %.0lf %.0lf %.0lf %.0lf %.0lf %.0lf\n", t, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y);
	}
}

