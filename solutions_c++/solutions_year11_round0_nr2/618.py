#include <stdio.h>
#include <string.h>
#include <math.h>

void Solver(FILE* fileout, int N, unsigned char List[], unsigned char R[26][26]){
  char final[101];
  int i, j, pos;

  pos = 0;
  final[pos] = '\0';
  for( i = 0; i < N; i ++ ){
    if( pos == 0 ){
      final[pos]     = List[i];
      final[pos + 1] = '\0';
      pos ++;
    }
    else{
      if( (R[List[i] - 'A'][final[pos - 1] - 'A'] & 0x7F) > 1 ){
        final[pos - 1] = R[List[i] - 'A'][final[pos - 1] - 'A'] & 0x7F;
      }
      else{
        final[pos]     = List[i];
        final[pos + 1] = '\0';
        pos ++;
        for( j = 0; j < pos - 1; j ++ ){
          if( (R[final[j] - 'A'][final[pos - 1] - 'A'] & 0x80) != 0 ){
            pos = 0;
            final[pos] = '\0';
            break;
          }
        }
      }
    }
  }

  fprintf(fileout, "[");
  for( i = 0; i < pos - 1; i ++ ){
    fprintf(fileout, "%c, ", final[i]);
  }
  if( pos > 0 ){
    fprintf(fileout, "%c", final[pos-1]);
  }
  fprintf(fileout, "]\n");
  return;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, C, D, N;
  unsigned char R[26][26], c1, c2, c3, List[101];
  int res, t, c, d, i, j;

  if( argc < 3 ){
    printf("Usage is: task2 filein fileout\n");
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
    for( i = 0; i < 26; i ++ ){
      for( j = 0; j < 26; j ++ ){
        R[i][j] = 0;
      }
    }
    fscanf(filein, "%d ", &C);
    printf("%d ", C);
    for( c = 0; c < C; c ++ ){
      fscanf(filein, "%c%c%c ", &c1, &c2, &c3);
      printf("%c%c%c ", c1, c2, c3);
      R[c1-'A'][c2-'A'] = c3;
      R[c2-'A'][c1-'A'] = c3;
    }
    fscanf(filein, "%d ", &D);
    printf("%d ", D);
    for( d = 0; d < D; d ++ ){
      fscanf(filein, "%c%c ", &c1, &c2);
      printf("%c%c ", c1, c2);
      R[c1-'A'][c2-'A'] |= 0x80;
      R[c2-'A'][c1-'A'] |= 0x80;
    }
    fscanf(filein, "%d ", &N);
    printf("%d ", N);
    fscanf(filein, "%s\n", List);
    printf("%s\n", List);

    for( i = 0; i < 26; i ++ ){
      for( j = 0; j < 26; j ++ ){
        printf("%c", R[i][j]);
      }
      printf("\n");
    }
    // Solve & Output
    fprintf(fileout, "Case #%d: ", t + 1);
    Solver(fileout, N, List, R);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
