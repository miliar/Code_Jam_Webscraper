#include <stdio.h>

int main()
{
	int t;
	scanf("%d", &t);
	
	for (int k = 0; k < t; ++k) {
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		
		int* frequencies = new int[n];
		for (int i = 0; i < n; ++i)
			scanf("%d", &frequencies[i]);
			
		int ret = -1;
		for (int i = l; i <= h; ++i) {
			bool ok = true;
			for (int j = 0; j < n; ++j) {
				if (i % frequencies[j] != 0 && frequencies[j] % i != 0) {
					ok = false;
					break;
				}
			}
			
			if (ok) {
				ret = i;
				break;
			}
		}

		printf("Case #%d: ", k + 1); 

		if (ret < 0) 
			printf("NO\n");
		else
			printf("%lld\n", ret);
		
		delete [] frequencies;
	}
}
