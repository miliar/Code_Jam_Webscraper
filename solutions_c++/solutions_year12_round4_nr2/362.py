#include <stdio.h>
#include <memory.h>
#include <math.h>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(i, n) for (int i = 0; i < n; i++)
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : (-(x)))
#define SQR(x) ((x) * (x))

int main() {
	int T;
	scanf("%d", &T);
	FOR(ca, T) {
		int N, W, L;
		scanf("%d%d%d", &N, &W, &L);
		
		double r[1000];
		FOR(i, N)
			scanf("%lf", &r[i]);
		
		//sort(r, r+N);
		
		printf("Case #%d: ", ca+1);
		
		double x[1000], y[1000];
		
		
		FOR(i, N) {
			double cx = W, cy = L;
			double step;
			
			
			FOR(j, i) {
				if (SQR(x[j] - cx) + SQR(y[j] - cy) < SQR(r[i] + r[j] + 0.1)) {
					printf("too bad\n");
				}
			}
				
				
			FOR(kk, 2) {
				step = MAX(W, L);
				while (step > 1e-4) {
					bool ok = 1;
					double nx = cx - step * (kk == 1);
					double ny = cy - step * (kk == 0);
					
					//printf("check %.6lf %.6lf\n", nx, ny);
					if (nx > 0 && ny > 0) {
						FOR(j, i) {
							//printf("%.6lf %.6lf, %.6lf", SQR(x[j] - nx), SQR(y[j] - ny), (double)SQR(r[i] + r[j]));
							if (SQR(x[j] - nx) + SQR(y[j] - ny) < SQR(r[i] + r[j] + 0.1)) {
								ok = 0;
								break;
							}
						}
						if (ok) {
							cx = nx;
							cy = ny;
						}
					}
					else
						ok = 0;
					
					//printf("%d\n", (int)ok);
					if (!ok)
						step /= 2;
				}
			}
			
			x[i] = cx;
			y[i] = cy;
			
			printf("%.3f %.3f ", cx, cy);
			
		}
		
		putchar(10);
		
	}
	
}

