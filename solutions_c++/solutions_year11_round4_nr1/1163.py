#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int ca=0; ca<t; ca++) {
		int x, s, r, t, n;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		
		static int sp[1000000];
		memset(sp, 0, sizeof(sp));
		
		for (int i=0; i<n; i++) {
			int d1, d2, d3;
			scanf("%d%d%d", &d1, &d2, &d3);
			//printf("set %d %d\n", d1, d2);
			for (int j=d1; j<d2; j++)
				sp[j] = d3; 
		}	
		double ans = 0;
		sort(sp, sp+x);
		
		//for (int i=0; i<x; i++)	printf("%d ", sp[i]);	putchar(10);
		double tt = t;
		for (int i=0; i<x; i++) {
			double maxtt = (1.0 / (sp[i] + r));

			//printf("tt = %lf, maxtt = %lf\n", tt, maxtt);
			if (tt > maxtt) {
				//ans += 1.0 / (sp[i] + r);
				tt -= maxtt;
				ans += maxtt;
			}
			else {
				ans += tt / maxtt / (sp[i] + r);
				ans += (1 - tt / maxtt) / (sp[i] + s);
				tt = 0;	
			}
			//printf("ans = %lf\n", ans);
				
		}
		printf("Case #%d: %.10lf\n", ca+1, ans);
	}	
}
