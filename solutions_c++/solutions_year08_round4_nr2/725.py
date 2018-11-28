#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, m, A;

int mod(int x) {
	return (x < 0) ? -x : x;
}

int prod_vet(int x1, int y1, int x2, int y2) {
	return x1*y2 - x2*y1;
}

int main() {
	int cases, t = 1;
	int a, b, c, d;
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d %d %d",&n,&m,&A);
		for (a=0; a <= n; a++) {
			for (b=0; b <= m; b++) {
				for (c=0; c <= n; c++) {
					for (d=0; d <= m; d++) {
						if (mod(prod_vet(a,b,c,d)) == A)
							goto END;
					}
				}
			}
		}
		END:
		printf("Case #%d: ",t++);
		if (a <= n)
			printf("0 0 %d %d %d %d\n",a,b,c,d);
		else
			puts("IMPOSSIBLE");
	}
	
	return 0;
}
