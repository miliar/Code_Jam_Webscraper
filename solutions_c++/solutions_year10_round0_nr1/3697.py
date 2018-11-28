#include <stdio.h>

bool IsSnapped(int N, int K);

int main(int argc, char** argv) {

  FILE *fp;
  fp = fopen(argv[1], "r");
  

  int num_of_cases;
  fscanf(fp, "%d\n", &num_of_cases);
  fprintf(stderr, "Number of Cases: %d\n", num_of_cases);

  for (int i = 0; i < num_of_cases; i++) {
    int N = 0; int K = 0;
    fscanf(fp, "%d %d\n", &N, &K);
    fprintf(stderr, "%d %d\n", N, K);
    printf("Case #%d: ", (i+1));
    
    if(IsSnapped(N, K))
      printf("ON\n");
    else
      printf("OFF\n");

  }
  
  return 0;
}

bool IsSnapped(int N, int K)
{
  bool Snapped = (K % (1<<N)) == ((1<<N)-1);
  return Snapped;
}
