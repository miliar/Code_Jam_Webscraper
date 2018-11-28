#include <stdio.h>

unsigned T, A, B, d, x, z;


main()
{
	scanf("%d\n", &T);
	
	for (unsigned i = 1; i <= T; ++i) {
		scanf("%d %d\n", &A, &B);

		x = 0;
		for (z =1, d = 0; B >=z; z *= 10)		
			d++;

		for (unsigned n = A; n < B; n++) {
			unsigned m = n;
			for (unsigned j = 1; j < d; j++) {
				m = (m + (m%10) * z) / 10;
				if (A <= n && n < m && m <= B)
					x++;
			}
		}

		printf("Case #%d: %d\n", i, x);
		
	}
}

