#include <stdio.h>

bool Solver(int N, int K){
  int mask = (1 << N) - 1;
  if (mask == (K & mask)){
    return true;
  }
  else{
    return false;
  }
}


int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, N, K;
  int t;

  if( argc < 3 ){
    printf("Usage is: task1 filein fileout\n");
    return 0;
  }

  /* Input */

  filein = fopen(argv[1], "r");
  if( filein == NULL ){
    printf("Error open(); filein\n");
    return 0;
  }
  fileout = fopen(argv[2], "w");
  if( fileout == NULL ){
    printf("Error open(); fileout\n");
    return 0;
  }

  fscanf(filein, "%d\n", &T);
  printf("%d\n", T);
  for( t = 0; t < T; t ++ ){
    fscanf(filein, "%d %d\n", &N, &K);
    printf("-------------\n", N, K);
    printf("%d %d\n", N, K);

    /* Solve & Output*/
    if( Solver(N, K) ){
      fprintf(fileout, "Case #%d: ON\n", t+1);
    }
    else{
      fprintf(fileout, "Case #%d: OFF\n", t+1);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
