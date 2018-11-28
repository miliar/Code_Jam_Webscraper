#include <stdio.h>
#include <string.h>
#include <math.h>

int N, K, B, T;
int x[50], v[50];

int f(int n, int k){
  if( k == 0 ){
    return 0;
  }
  if( x[n-1] + v[n-1]*T >= B ){
    return f(n-1,k-1);
  }
  else{
    return f(n-1,k) + k;
  }
}

void Solver(FILE *filein, FILE *fileout){
  int i, n, res;

  n = 0;
  for( i = 0; i < N; i ++ ){
    if( x[i] + v[i]*T >= B ){
      n ++;
    }
  }
  if( n < K ){
    fprintf(fileout,"IMPOSSIBLE\n");
    return;
  }
  res = f(N,K);
  fprintf(fileout,"%d\n",res);
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int t, C, i;

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

  fscanf(filein, "%d\n", &C);
  printf("%d\n", C);
  for( t = 0; t < C; t ++ ){
    printf("-------------\nt=%d\n", t);
    fscanf(filein, "%d %d %d %d\n", &N, &K, &B, &T);
    printf("%d %d %d %d\n", N, K, B, T);
    for( i = 0; i < N - 1; i ++ ){
      fscanf(filein, "%d ", x + i);
      printf("%d ", x[i]);
    }
    fscanf(filein, "%d\n", x + i);
    printf("%d\n", x[i]);

    for( i = 0; i < N - 1; i ++ ){
      fscanf(filein, "%d ", v + i);
      printf("%d ", v[i]);
    }
    fscanf(filein, "%d\n", v + i);
    printf("%d\n", v[i]);

    // Solve & Output
    fprintf(fileout, "Case #%d: ", t + 1);
    Solver(filein, fileout);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
