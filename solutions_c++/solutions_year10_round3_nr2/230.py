#include <cstdio>

FILE *inputfile = fopen("B-small.in", "r");
FILE *outputfile = fopen("B-small.out", "w");
long long T, C, L, P;


int main(){
  fscanf(inputfile, "%lld", &T);
  for (int foo = 1; foo <= T; foo++){
    fscanf(inputfile, "%lld%lld%lld", &L, &P, &C);
    int multiples = 1;
    while (L*C < P){
      L *= C;
      multiples++;
    }
    int count = 0;
    while (1 << count < multiples){
      count++;
    }
    fprintf(outputfile, "Case #%d: %d\n", foo, count);
  }
  return 0;
}
