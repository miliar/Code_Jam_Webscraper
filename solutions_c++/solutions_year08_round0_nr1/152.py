#include <stdio.h>
#include <string.h>

const int N_MAX = 20;
const int S_MAX = 100;
const int Q_MAX = 1000;
const int NAME_MAX = 100;

int N, S, Q;
char Names[S_MAX][NAME_MAX];
char Queries[Q_MAX][NAME_MAX];

int NamesMark[S_MAX];

int FindPrevious(int last_switch){
  int i = last_switch;
  int current_count = 0;
  int eng_num, j;

  memset(NamesMark, 0, S*sizeof(int));
  while( i > -1 ){
    /* find search engine string */
    for(j = 0; j < S; j ++ ){
      if( !strcmp(Names[j], Queries[i]) ){
        eng_num = j;
        break;
      }
    }
    /* Mark it */
    if( NamesMark[eng_num] == 0 ){
      NamesMark[eng_num] = 1;
      current_count ++;
    }
    if( current_count == S ){
      break;
    }
    i --;
  }

  if( i >= 0 ){
    printf("%s\n",Names[i]);
  }

  return i;
}

int Solver(void){
  int current_res = 0;
  int last_switch = Q-1;

  while( ( last_switch = FindPrevious(last_switch) ) != -1 ){
    current_res ++;
  }
  
  return current_res;
}

int main(int argc, char *argv[]){
  FILE* file;
  FILE* fileout;
  int n, i, res;

  if( argc < 2 ){
    printf("Usage is: task1 filename\n");
    return 0;
  }

  /* Input */

  file = fopen(argv[1], "r");
  if( file == NULL ){
    printf("Error open();\n");
    return 0;
  }
  fileout = fopen("res.txt", "w");


  fscanf(file, "%d\n", &N);
  for( n = 0; n < N; n ++ ){
    fscanf(file, "%d\n", &S);
    for( i = 0; i < S; i ++ ){
//      fscanf(file, "%s\n", Names[i]);
      fgets(Names[i], NAME_MAX, file);
	}
    fscanf(file, "%d\n", &Q);
    for( i = 0; i < Q; i ++ ){
//      fscanf(file, "%s\n", Queries[i]);
      fgets(Queries[i], NAME_MAX, file);
    }


  printf("%d ----------------------------------\n", N);
  printf("%d\n", S);
  for( i = 0; i < S; i ++ ){
    printf("%s\n", Names[i]);
  }
  printf("%d\n", Q);
  for( i = 0; i < Q; i ++ ){
    printf("%s\n", Queries[i]);
  }
  printf("%d ----------------------------------\n", N);


    /* Solving */
    res = Solver();
    /* Output */
    fprintf(fileout, "Case #%d: %d\n", n+1, res);
  }

  fclose(fileout);
  fclose(file);

  return 0;
}
