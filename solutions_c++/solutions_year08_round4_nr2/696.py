#include <cstdio>
#include <cstdlib>
using namespace std;

int n, m;

int get_a(int xb, int yb, int xc, int yc) {
	return abs(xb * yc - xc * yb);
}



bool solve(int a, int& x1, int& y1, int& x2, int& y2) {
	/*int xc, yc;
	for(int xb = 0; xb <= n; xb++)
		for(int yb = 0; yb <= m; yb++)
		{
			x1 = xb;
			y1 = yb;
			if(xb == 0 && yb == 0) continue;

			if(get_a(xb, yb, 0, m) < a &&
			   get_a(xb, yb, n, 0) < a && 
			   get_a(xb, yb, n, m) < a ) continue;

			if(yb == 0) {
				if(a % xb == 0) yc = a / xb;
				if(yc >= 0 && yc <= m) {
				  x2 = 0;
				  y2 = yc;
				  return true;
				}
				continue;
			}

			for(yc = 0; yc <= m; yc++)
			{
				if( abs(a - xb * yc) % yb == 0 ) {
					xc = -(a - xb * yc) / yb;
					if(xc >= 0 && xc <= n) {
						x2 = xc;
						y2 = yc;
						return true;
					}
				}		
			}

		}

	return false;*/

	for(x1 = 0; x1 <= n; x1++)
		for(y1 = 0; y1 <= m; y1++)
			for(x2 = 0; x2 <= n; x2++)
		       for(y2 = 0; y2 <= m; y2++)
				   if(abs(x1*y2 - x2*y1) == a) return true;


	return false;

}

int main(void) {
	int c;
	int a;
	int x1, y1, x2, y2;

	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &c);
	for(int t=1; t<=c; ++t) {
		scanf("%d%d%d", &n, &m, &a);
		
		bool res = solve(a, x1, y1, x2, y2);		

		if(res)
			printf("Case #%d: 0 0 %d %d %d %d\n", t, x1, y1, x2 ,y2);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}

	return 0;
}

