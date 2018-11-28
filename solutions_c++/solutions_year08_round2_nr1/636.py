#include <stdio.h>

unsigned long int Tests;
unsigned long int X, Y, n, A, B, C, D, x0, y0, M;
int N[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
FILE *fin, *fout;
unsigned long int i, j, k, count;
long double a, b, c;

int main(void){
  printf("Hello, world!\n");
  fin = fopen("in.txt","r");
  fout = fopen("out.txt","w");

  fscanf(fin, "%i\n", &Tests);
  printf("%Tests = %d\n", Tests);
  for( i = 0; i < Tests; i ++ ){
    fscanf(fin, "%i %i %i %i %i %i %i %i\n", &n, &A, &B, &C, &D, &x0, &y0, &M);
    printf("%i %i %i %i %i %i %i %i\n", n, A, B, C, D, x0, y0, M);
    for( j = 0; j < 3; j ++ ){
      for( k = 0; k < 3; k ++ ){
        N[j][k] = 0;
      }
    }
    X = x0; Y = y0;
    printf("%i %i\n", X, Y);
    N[X%3][Y%3] += 1;
    for( j = 1; j <= n-1; j++ ){
      a = (long double) A * (long double) X + (long double) B;
      b = (unsigned long) (a / (long double) M);
      c = a - b * (long double) M;
      X = (unsigned int) c;
      a = (long double) C * (long double) Y + (long double) D;
      b = (unsigned long) ( a / (long double) M );
      c = a - b * (long double) M;
      Y = (unsigned int) c;
//      X = (A * X + B) % M;
//      Y = (C * Y + D) % M;
      printf("%i %i\n", X, Y);
      N[X%3][Y%3] += 1;
    }
    for( j = 0; j < 3; j ++ ){
      for( k = 0; k < 3; k ++ ){
        printf("%3d ",N[j][k]);
      }
      printf("\n",N[j][k]);
    }
    count = 0;
    for( j = 0; j < 3; j ++ ){
      for( k = 0; k < 3; k ++ ){
        if( N[j][k] >= 3 ){
           count += N[j][k] * (N[j][k] - 1) * (N[j][k] - 2) / 6;
        }
      }
      count += N[j][0] * N[j][1] * N[j][2];
      count += N[0][j] * N[1][j] * N[2][j];
    }
    count += N[0][0] * N[1][1] * N[2][2];
    count += N[0][0] * N[2][1] * N[1][2];
    count += N[1][0] * N[0][1] * N[2][2];
    count += N[1][0] * N[2][1] * N[0][2];
    count += N[2][0] * N[0][1] * N[1][2];
    count += N[2][0] * N[1][1] * N[0][2];
    printf("%i\n", count);
    fprintf(fout, "Case #%i: %i\n", i+1, count);
  }
  fclose(fin);
  fclose(fout);

  return 0;
}