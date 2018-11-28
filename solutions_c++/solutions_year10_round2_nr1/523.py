#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
int N,M,num;
char edir[100][101];
char ndir[100][101];
char node[10000][100];
int parent[10000];
int sorted[100];

int Add(char *name){
  int i, p, ops;
  char n[101], *s;

  if( strlen(name) < 2 ){
    return 0;
  }
  strcpy(n, name);
  ops = 0;
  p = -1;
  s = strtok(n, "/");
  while(s != NULL){
    for( i = 0; i < num; i ++ ){
      if( parent[i] != p ){
        continue;
      }
      if( !strcmp(s, node[i]) ){
        p = i;
        break;
      }
    }
    if( i == num ){
      strcpy(node[num], s);
      parent[num] = p;
      p = num;
      num ++;
      ops ++;
    }
    s = strtok(NULL, "/");
  }
  return ops;
}

int compare( const void *arg1, const void *arg2 )
{
   /* Compare all of both strings: */
   return strcmp( ndir[*(int*) arg1], ndir[*(int*) arg2] );
}

void Solver(FILE *filein, FILE *fileout){
  int i, j, n;
  num = 0;
  n = 0;
  for( i = 0; i < N; i ++ ){
    n += Add(edir[i]);
    //printf("---\n");
    //for( j = 0; j < num; j ++){
    //  printf("[%d]%d: %s\n", j, parent[j], node[j]);
    //}
  }

  for( i = 0; i < M; i ++ ){
    sorted[i] = i;
  }
  qsort(sorted, M, sizeof(int), compare);
//  printf("sorted --\n", ndir[sorted[i]]);
  for( i = 0; i < M; i ++ ){
    printf("%s\n", ndir[sorted[i]]);
    //n += Add(ndir[sorted[i]]);
    //printf("---\n");
    //for( j = 0; j < num; j ++){
    //  printf("%d: %s\n", parent[j], node[j]);
    //}
  }
  printf("end sorted --\n", ndir[sorted[i]]);

  n = 0;
  for( i = 0; i < M; i ++ ){
    n += Add(ndir[sorted[i]]);
    //printf("---\n");
    //for( j = 0; j < num; j ++){
    //  printf("[%d]%d: %s\n", j, parent[j], node[j]);
    //}
  }
  fprintf(fileout,"%d\n", n);
  printf("%d\n", n);
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int t, T, i, v;

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
    printf("-------------\nt=%d\n", t);
    fscanf(filein, "%d %d\n", &N, &M);
    printf("%d %d\n", N, M);
    for( i = 0; i < N; i ++ ){
      fscanf(filein, "%s\n", edir + i );
      printf("%s\n", edir[i]);
    }
    for( i = 0; i < M; i ++ ){
      fscanf(filein, "%s\n", ndir + i );
      printf("%s\n", ndir[i]);
    }
    // Solve & Output
    fprintf(fileout, "Case #%d: ", t + 1);
    Solver(filein, fileout);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
