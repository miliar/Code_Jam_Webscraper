#include <iostream>
#include <cmath>
using namespace std;
const double eps = 1e-8;
inline double xmult(double x1, double y1, double x2, double y2, double x0, double y0) {
	return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0);
}
inline double areaTriangle(double x1, double y1, double x2, double y2, double x3, double y3) {
	return fabs(xmult(x1, y1, x2, y2, x3, y3)) / 2;
}
int main(){
	int cases;
	cin >> cases;
	for (int t = 0; t != cases; ++t){
		int n, m, a;
		cin >> n >> m >> a;
		double req = (a + 0.0) / 2;
		printf("Case #%d: ", t + 1);
		bool ok = false;
		for (int i = 0; i <= n; ++i){
			for (int j = 0; j <= m; ++j){
				for (int k = 0; k <= n; ++k){
					for (int l = 0; l <= m; ++l){
						double s = areaTriangle(i, j, k, l, 0, 0);
						if (fabs(s - req) < eps){
							ok = true;
							printf("%d %d %d %d %d %d\n", 0, 0, i, j, k, l);
							break;
						}
					}
					if (ok) break;
				}
				if (ok) break;
			}
			if (ok) break;
		}
		if (!ok) printf("IMPOSSIBLE\n");
	}
	return 0;
}