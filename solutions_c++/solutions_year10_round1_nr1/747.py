#include <stdio.h>
#include <string.h>
#include <math.h>

char board[51][51], board1[51][51];

void Solver(FILE *filein, FILE *fileout, int N, int K){
  int i,j,k;
  bool red, blue;
  for( i = 0; i < N; i ++ ){
    for( j = 0; j < N; j ++ ){
      board1[i][j] = board[N-1-j][i];
    }
    board1[i][N] = 0;
  }
  printf("Rotate --\n");
  for(i = 0; i < N; i ++){
    printf("%s\n", board1[i]);
  }
  for(i = N-1; i >= 0; i --){
    for(j = 0; j < N; j ++){
      if(board1[i][j] != '.'){
        for( k = i + 1; (k < N)&&(board1[k][j] == '.'); k ++ ){
          board1[k][j] = board1[k-1][j];
          board1[k-1][j] = '.';
        }
      }
    }
  }
  printf("Drop --\n");
  for(i = 0; i < N; i ++){
    printf("%s\n", board1[i]);
  }
  red = false;
  blue = false;
  for( i = 0; i < N + 1 - K; i ++ ){
    for( j = 0; j < N + 1 - K; j ++ ){
      for( k = 1; k < K; k ++){
        if( board1[i][j] != board1[i+k][j+k] ){
          break;
        }
      }
      if( k == K ){
        if( board1[i][j] == 'R' ){
          red = true;
        }
        if( board1[i][j] == 'B' ){
          blue = true;
        }
      }
    }
  }

  for( i = 0; i < N + 1 - K; i ++ ){
    for( j = 0; j < N; j ++ ){
      for( k = 1; k < K; k ++){
        if( board1[i][j] != board1[i+k][j] ){
          break;
        }
      }
      if( k == K ){
        if( board1[i][j] == 'R' ){
          red = true;
        }
        if( board1[i][j] == 'B' ){
          blue = true;
        }
      }
    }
  }

  for( i = 0; i < N; i ++ ){
    for( j = 0; j < N + 1 - K; j ++ ){
      for( k = 1; k < K; k ++){
        if( board1[i][j] != board1[i][j+k] ){
          break;
        }
      }
      if( k == K ){
        if( board1[i][j] == 'R' ){
          red = true;
        }
        if( board1[i][j] == 'B' ){
          blue = true;
        }
      }
    }
  }

  for( i = K - 1; i < N; i ++ ){
    for( j = 0; j < N + 1 - K; j ++ ){
      for( k = 1; k < K; k ++){
        if( board1[i][j] != board1[i-k][j+k] ){
          break;
        }
      }
      if( k == K ){
        if( board1[i][j] == 'R' ){
          red = true;
        }
        if( board1[i][j] == 'B' ){
          blue = true;
        }
      }
    }
  }

  if( !blue && !red ){
    fprintf(fileout,"Neither\n");
    printf("Neither\n");
  }
  if( !blue && red ){
    fprintf(fileout,"Red\n");
    printf("Red\n");
  }
  if( blue && !red ){
    fprintf(fileout,"Blue\n");
    printf("Blue\n");
  }
  if( blue && red ){
    fprintf(fileout,"Both\n");
    printf("Both\n");
  }
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, t, N, K, i, j;
  char res[10];

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
    fscanf(filein, "%d %d\n", &N, &K);
    printf("%d %d\n", N, K);
    for( j = 0; j < N; j ++ ){
      fscanf(filein, "%s\n", board[j]);
      printf("%s\n", board[j]);
    }

    // Solve & Output
    fprintf(fileout, "Case #%d: ", t + 1);
    Solver(filein, fileout, N, K);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
