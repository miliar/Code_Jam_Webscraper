#include <stdio.h>
#include <string.h>
#include <math.h>

//int Solver(int N, int R[], int P[]){
//  return 0;
//}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, N, A[1000];
  int t, n, i, j;
//  double a, b, c;
  int res;

  if( argc < 3 ){
    printf("Usage is: task1 filein fileout\n");
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
    for( n = 0; n < N - 1; n ++ ){
      fscanf(filein, "%d ", A + n);
      printf("%d ", A[n]);
    }
    fscanf(filein, "%d\n", A + n);
    printf("%d\n", A[n]);

    // Solve & Output
//    res = Solver(filein, fileout, N, K);
    for( n = N - 1; n >= 0; n -- ){
      if( A[n] == n + 1 ){
        N --;
      }
    }
    fprintf(fileout, "Case #%d: %.6f\n", t + 1, (double)N);
  }

  //a = 0;
  //b = 1.0;
  //for( i = 0; i < 50; i ++ ){
  //  a += b * ((i+1.0)/6 + (i+3.0)/2);
  //  b *= 1.0/3;
  //}
  //printf("%f\n",a);

  //a = 0;
  //b = 1.0;
  //for( i = 0; i < 50; i ++ ){
  //  a += b * ((i+1.0)/24 + 6.0*(i+3.0)/24 + 8.0*(i+4.0)/24);
  //  b *= 9.0/24;
  //}
  //printf("%f\n",a);

  fclose(fileout);
  fclose(filein);

  return 0;
}
