#include <stdio.h>

unsigned long R, k, N;
unsigned long gi[1000];
unsigned long subsum[1000];
unsigned long next[1000];

unsigned long solve() {
  unsigned long cur;
  for(cur=0; cur < N; cur++) {
    unsigned long num_people = 0;
    unsigned long i = 0;
    while(i < N) {
      if (num_people + gi[(i+cur)%N] > k)
	break;

      num_people += gi[(i+cur)%N];
      i++;
    }

    subsum[cur] = num_people;
    next[cur] = (i+cur)%N;
    
    // printf("subsum[%ld]=%ld, next[%ld]=%ld\n", cur, subsum[cur], cur, next[cur]);

  }

  unsigned long ret = 0;
  cur = 0;
  for(int ride=0; ride < R; ride++) {
    ret += subsum[cur];
    cur = next[cur];
  }
  return ret;
}


main(int argc, const char* argv[]) {
  FILE* f=fopen(argv[1], "r");
  FILE* f2=fopen(argv[2], "w");
  
  
  int num;
  fscanf(f, "%d", &num);
  int i=1;

  while(num--) {


    fscanf(f, "%ld %ld %ld", &R, &k, &N);

    int j=0;
    while(j < N) {
      fscanf(f, "%ld", &gi[j]);
      j++;
    }
    
    fprintf(f2, "Case #%d: %ld\n", i++, solve());
  }
  fclose(f2);

}

/*
Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
*/
