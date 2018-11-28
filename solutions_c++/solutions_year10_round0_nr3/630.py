#include <stdio.h>

long long CountCost(int g[], int N, int k, int start, int count){
  long long sum, cost, i, j;

  cost = 0;
  j = start;
  for( i = 0; i < count; i ++){
    sum = g[j];
    while( true ){
      j = (j + 1) % N;
      if( sum + g[j] > k ){
        break;
      }
      sum = sum + g[j];
    }
    cost = cost + sum;
  }
  return cost;
}

long long Solver(int R, int k, int N, int g[]){
  int first[1000], i, iter = 1, start = 0, loopstart, loopstartiter, loopnextiter;
  long long sum;
  long long loopcost;
  bool loopfound;

  for( i = 0; i < N; i ++ ){
    first[i] = 0;
  }

  /* Special case of low people */
  sum = 0;
  for( i = 0; i < N; i ++ ){
    sum += g[i];
  }
  if( sum <= k ){
    return sum*R;
  }

  loopfound = false;
  while( ! loopfound ){
    first[start] = iter;
    i = start;
    sum = g[i];
    while( true ){
      i = (i + 1) % N;
      if( sum + g[i] > k ){
        break;
      }
      sum = sum + g[i];
    }
    start = i;
    iter ++;
    if( first[start] != 0 ){
      loopstart = start;
      loopstartiter = first[start];
      loopnextiter = iter;
      loopfound = true;
      loopcost = CountCost(g, N, k,loopstart, loopnextiter - loopstartiter);
    }
  }

  if( R <= loopnextiter ){
    return CountCost(g, N, k, 0, R);
  }
  else{
    iter = (R - (loopstartiter - 1)) / (loopnextiter - loopstartiter);
    return CountCost(g, N, k, 0, loopstartiter - 1) + iter * loopcost + CountCost(g, N, k, loopstart, (R - (loopstartiter - 1)) % (loopnextiter - loopstartiter));
  }

}


int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, R, k, N, g[1000];
  int t, i;

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
    fscanf(filein, "%d %d %d\n", &R, &k, &N);
    printf("-------------\n");
    printf("%d %d %d\n", R, k, N);
    for( i = 0; i < N - 1; i ++ ){
      fscanf(filein, "%d ", g + i);
    }
    fscanf(filein, "%d\n", g + N - 1);
    for( i = 0; i < N; i ++ ){
      printf("%d ", g[i]);
    }
    printf("\n");

    /* Solve & Output*/
    fprintf(fileout, "Case #%d: %lld\n", t+1, Solver(R, k, N, g));
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
