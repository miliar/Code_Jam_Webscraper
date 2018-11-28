#include <stdio.h>
#include <stdlib.h>
#include <iostream.h>
#include <memory.h>

int compare(const void *a, const void *b);
unsigned __int64 gcd(unsigned __int64 m, unsigned __int64 n);
int main() {
	int C,  N;
	unsigned __int64 t[1000];
	int c = 1;
	FILE* f1 = fopen("b.in", "r"); FILE* f2 = fopen("b.out", "w");
	fscanf(f1, "%d", &C);
//	fscanf(f1, "%d", &T); 
	while (c <= C) {
		int i, j;
		fscanf(f1, "%d", &N); 
		for (i = 0; i < N; i ++)
			fscanf(f1, "%I64u", &t[i]);
		qsort(t, N, sizeof(t[0]), compare);

		unsigned __int64 sub[1000];
	
		int k = 0; 

		for (i = 1; i < N; i ++) {
			for (j = 0; j < i; j ++ ) {
				if (t[i] - t[j] != 0) 
					sub[k++] = t[i]  - t[j];
			}
		}

		
		unsigned __int64 y = 1;
		if ( k == 1)
			y = sub[0];
		else
			y = 1;
		for ( i = 0; i < k; i ++) {
			for (j = i + 1; j < k; j ++) {
				unsigned __int64 g = gcd(sub[i], sub[j]);
				if (g > y) 
					y = g;
			}
		}
			
		//printf("%I64u\n", y);
		unsigned __int64 T = t[0] / y;
		unsigned __int64 x;
		if ( t[0] % y != 0)
			T ++;
		
		x = T * y - t[0];

		//printf("Case #%d: %I64u\n", c, x);
		fprintf(f2, "Case #%d: %I64u\n", c, x);

		c ++;


	}
	return 0;
}

unsigned __int64 gcd(unsigned __int64 m, unsigned __int64 n) {
      unsigned __int64 r =0;
      if(n ==0) 
		  return m;
	  else{
		  r = m %n;
		  return gcd(n, r);
	  }
}
int compare(const void *a, const void *b) {
	unsigned __int64 *ai = (unsigned __int64*)(a);
	unsigned __int64 *bi = (unsigned __int64*)(b);
	if (*ai < *bi)
		return -1;
	else if (*ai > *bi)
		return 1;
	return 0;
}