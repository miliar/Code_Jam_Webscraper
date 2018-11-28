#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

  if(argc >= 3) return -1;
  
  FILE *inf = fopen(argv[1], "r");
  
  int nCases;
  fscanf(inf, "%d", &nCases);
  
  for(int i = 0; i < nCases; i++) {
  	int N, K;
  	
  	fscanf(inf, "%d %d", &N, &K);
  	
  	if((K + 1) % (1 << N) == 0)
  	  printf("Case #%d: ON\n", i + 1);
  	else
      printf("Case #%d: OFF\n", i + 1);
  }
  
  return 0;
}