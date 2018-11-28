#include <iostream>
#include <cstdio>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

double a[1000020];

double e = 1e-6;
 
bool calculate(int n, double time, double distance) 
{
	double x = max((a[0] - distance),(double)INT_MIN);
  	int i;

  	for (i = 1; i < n; i++) {
    		if (a[i] + distance < x + time) 
			return 0;
    		x = max(a[i] - distance, x + time);
  	}

  	return 1;
}
 
int main() 
{
	int T, Ti, n, y, k;
	double t, x, j, i;
		
	scanf("%d", &T);

	for ( Ti = 1; Ti <= T; Ti++ ) {  	
		scanf("%d%lf", &n, &t);
	
		k = 0;

		for (i = 0; i < n; i++ ) {
			scanf("%lf%d", &x, &y);

			for( j = 0; j < y; j++ )
				a[k++] = x;
		}

		sort (a, a + k);

		double lo = 0, hi = 1;

		while (!calculate(k, t, hi)) 
			hi *= 2.0;

    		while ( lo + e < hi ) {
      			double mid = (lo + hi) / 2.0;

      			if (calculate( k, t, mid)) 
				hi = mid;
      			else 
				lo = mid;
    		}

		printf("Case #%d: %.1lf\n", Ti, lo);
  	}

	return 0;
}
