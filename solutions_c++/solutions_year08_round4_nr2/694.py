#include "utils.h"

u64 xmax, ymax, A;

void RunTCase(int n) {

  //  u64 x1 = 0;
  //  u64 y1 = 0;

  for(u64 x1 = 0; x1 <= xmax; x1++)
    for(u64 y1 = 0; y1 <= ymax; y1++)
      for(u64 x2 = x1; x2 <= xmax; x2++) {
	for(u64 y2 = 0; y2 <= ymax; y2++) {
	  for(u64 x3 = x2; x3 <= xmax; x3++) {
	    for(u64 y3 = 0; y3 <= ymax; y3++) {
	      u64 a2;

	  a2 = llabs((x2 * y1 - x1 * y2) +
		     (x3 * y2 - x2 * y3) +
		     (x1 * y3 - x3 * y1));


	  //	  printf("%lld %lld %lld %lld %lld %lld, a2 = %lld.\n", x1, y1, x2, y2, x3, y3, a2); 
	  
	  if (a2 == A) {
	    printf("Case #%d: %lld %lld %lld %lld %lld %lld\n", n, x1, y1, x2, y2, x3, y3); 
	    return;
	  }
	}
      }
    }
  }

  printf("Case #%d: IMPOSSIBLE\n", n); 
}

void GetInputs() {
  fscanf(ifile, "%d", &N);
  for(int i = 0; i < N; i++) {
    fscanf(ifile, "%lld %lld %lld", &xmax, &ymax, &A);
    //    fprintf(stderr, "i = %d.\n", i);
    RunTCase(i + 1);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();

  fclose(ifile);
}
