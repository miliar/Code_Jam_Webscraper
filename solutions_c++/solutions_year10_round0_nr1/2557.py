#include <stdio.h>

bool solve(int n, int k) {

  unsigned long state = 0; // all off
  
  while (k--) {
    // toggle state
    // make a mask for the snappers which have power
    // the gfirst one has
    unsigned long mask =1;
    while((state&mask) == mask) {
      mask <<= 1;
      mask |= 1;
    }

    state = state ^ mask;
  }

  unsigned long mask =1;
  while((state&mask) == mask) {
    mask <<= 1;
    mask |= 1;
  }

printf("%ld %ld %ld\n", mask, 1ul<<n,  mask & (1ul<<n));
return (mask & (1ul<<n)) != 0;
}

main(int argc, const char* argv[]) {
  FILE* f=fopen(argv[1], "r");
  FILE* f2=fopen(argv[2], "w");
  
  
  int num;
  fscanf(f, "%d", &num);
  int i=1;
  while(num--) {
    int n,k;
    fscanf(f, "%d %d", &n, &k);
    
    fprintf(f2, "Case #%d: %s\n", i++, solve(n,k)?"ON":"OFF");
  }

}

/*
Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
*/
