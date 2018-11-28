#include <stdio.h>
#include <math.h>

unsigned long int Tests, n;
FILE *fin, *fout;
unsigned long int i, j, k;
long double res;
unsigned long int P, K, L;
unsigned long int PP[1000];
unsigned long int Cost, Max, MaxNum;
//char N[1000000];
//int C=0;

int main(void){
  fin = fopen("in.txt","r");
  fout = fopen("out.txt","w");

  fscanf(fin, "%i\n", &Tests);
  printf("%Tests = %d\n", Tests);
  for( i = 0; i < Tests; i ++ ){
    fscanf(fin, "%i %i %i\n", &P, &K, &L);
    printf("%i %i %i\n", P, K, L);
    for( j = 0; j < L; j ++){
      fscanf(fin, "%i\n", PP+j);
      printf("%i ", PP[j]);
    }
    res = 0;
    for(j = 0; j < L; j ++ ){
      Cost = ( j / K ) + 1;
      Max = 0;
      MaxNum = 0;
      for( k = 0; k < L; k ++ ){
        if( PP[k] > Max ){
          Max = PP[k];
          MaxNum = k;
        }
      }
      res += Cost * PP[MaxNum];
      PP[MaxNum] = 0;
    }
    printf("%Lf\n", res);
    fprintf(fout, "Case #%i: %.0lf\n", i+1, res);
  }
  fclose(fin);
  fclose(fout);

/*  for( i = 2; i < 1000000; i ++ ){
    if( N[i] == 0 ){
      printf("%i\n",i);
      C++;
      for( j = 2 * i; j < 1000000; j += i ){
        N[j] = 1;
      }
    }
  }
  printf("%i\n",C);
*/
  return 0;
}