#include <stdio.h>

int main() {
	int t, n, s, p, points, div, remainder;

	scanf("%d",&t);

	for (int i=1; i<=t; i++) {
	
		scanf("%d %d %d",&n,&s,&p);
		
		int count = 0;
	
		for (int j=0; j<n; j++) {
			
			scanf("%d",&points);
			
			div = points/3;
			remainder = points%3;

			if (remainder == 0) {
				if (div >= p) {
					count++;
				} else if (div+1 >= p && s > 0 && div+1 <= points) {
					count++;
					s--;
				}
			} else if (remainder == 1) {
				if (div+1 >= p && div+1 <= points)
					count++;
			} else {
				if (div+1 >= p) {
					count++;
				} else if (div+2 >= p && s > 0 && div+2 <= points) {
					count++;
					s--;
				}
			}

		}
		printf("Case #%d: %d\n",i,count);

	}
}
