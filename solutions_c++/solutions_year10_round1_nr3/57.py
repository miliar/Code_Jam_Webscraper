#include <stdio.h>
#include <math.h>

int main() {


  FILE* fin  = fopen("C.in", "r");
  FILE* fout = fopen("C.out", "w");


  int tests;
  fscanf(fin, "%d", &tests);

  double phi = (1 + sqrt(5)) / 2.0;

  for(int t = 0; t < tests; ++t) {
    int a1,a2,b1,b2;
    long long count = 0;
    fscanf(fin, "%d %d %d %d", &a1, &a2, &b1, &b2);
    for(int a = a1; a <= a2; ++a) {
      int x = (int)(floor(a / phi) + 0.5);
      int y = (int)(ceil(a * phi) + 0.5);
      if(b1 <= x) {
	if(x <= b2) {
	  count += x - b1 + 1;
	} else {
	  count += b2 - b1 + 1;
	}
      }
      if(y <= b2) {
	if(b1 <= y) {
	  count += b2 - y + 1;
	} else {
	  count += b2 - b1 + 1;
	}
      }
    }
    fprintf(fout, "Case #%d: %lld\n", 1+t, count);
  }

  fclose(fin);
  fclose(fout);


  return(0);
}
