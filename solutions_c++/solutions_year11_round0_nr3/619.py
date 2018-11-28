#include <stdio.h>
#include <string.h>
#include <math.h>

int Solver(int N, int R[], int P[]){
  return 0;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, N, C;
  int t, n, xor, sum, cmin;

  if( argc < 3 ){
    printf("Usage is: task3 filein fileout\n");
    return 0;
  }

  // Input 

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
    printf("-------------\t=%d\n", t);
    fscanf(filein, "%d\n", &N);
    printf("%d\n", N);
    sum = 0;
    xor = 0;
    cmin = 1000001;
    for( n = 0; n < N - 1; n ++ ){
      fscanf(filein, "%d ", &C);
      printf("%d ", C);
      sum += C;
      xor ^= C;
      if( C < cmin ){
        cmin = C;
      }
    }
    fscanf(filein, "%d\n", &C);
    printf("%d\n", C);
    sum += C;
    xor ^= C;
    if( C < cmin ){
      cmin = C;
    }

    // Solve & Output
//    res = Solver(filein, fileout, N, K);
    if( xor != 0 ){
      fprintf(fileout, "Case #%d: NO\n", t + 1);
    }
    else{
      fprintf(fileout, "Case #%d: %d\n", t + 1, sum - cmin);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
