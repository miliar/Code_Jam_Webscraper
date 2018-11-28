#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int ca=0; ca<t; ca++) {
		printf("Case #%d: ", ca+1);
		int c, d;
		cin >> c >> d;
		
		double mint = 0, maxt = 1e100;
		
		int p[200], v[200];
		for (int i=0; i<c; i++) {
			cin >> p[i] >> v[i];
			if ((v[i] - 1) * d / 2.0 > mint)
				mint = (v[i] - 1) * d / 2.0;
		}
			

		
		while (maxt - mint > 1e-10) {
			double t = (mint + maxt) / 2;
			
			double lastp = -1e100;
			for (int i=0; i<c; i++) {
				double minp = p[i] - t, maxp = p[i] + t;
				
				if (maxp < lastp + v[i] * d)
					goto fail;
				
				double firstp = lastp + d;
				if (firstp < minp)
					firstp = minp;
					
				lastp = firstp + (v[i] - 1) * d;
			}
			
			maxt = t;
			continue;
fail:
			mint = t;

		}
		printf("%.8lf\n", mint);
	}
}	
