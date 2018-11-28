#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

int Solver(int N, char R[], int P[]){
  int Opos = -1, Bpos = -1;
//  int Oppos = -1, Bppos = -1;
  int n, s = 0, ps = 0;

  if( R[N - 1] == 'B' ){
    Bpos = P[N - 1];
  }
  else{
    Opos = P[N - 1];
  }
  s = 1;
  ps = 1;
  printf("Push %c s = %d ps =%d\n", R[N-1], s, ps);

  for( n = N - 2; n >= 0; n -- ){
    if( R[n] == R [n + 1] ){
      s += abs(P[n] - P[n + 1]) + 1;
      ps += abs(P[n] - P[n + 1]) + 1;
      if( R[n] == 'B' ){
        Bpos = P[n];
      }
      else{
        Opos = P[n];
      }
    }
    else{
      if( R[n] == 'B' ){
        if( Bpos == -1 ){
          s += 1;
          ps = 1;
        }
        else{
          if( abs(Bpos - P[n]) <= ps ){
            s += 1;
            ps = 1;
          }
          else{
            s += 1 + abs(Bpos - P[n]) - ps;
            ps = 1 + abs(Bpos - P[n]) - ps;
          }
        }
        Bpos = P[n];
      }
      else{
        if( Opos == -1 ){
          s += 1;
          ps = 1;
        }
        else{
          if( abs(Opos - P[n]) <= ps ){
            s += 1;
            ps = 1;
          }
          else{
            s += 1 + abs(Opos - P[n]) - ps;
            ps = 1 + abs(Opos - P[n]) - ps;
          }
        }
        Opos = P[n];
      }
    }
    printf("Push %c s = %d ps = %d\n", R[n], s, ps);
  }

  if( R[0] == 'B' ){
    if( P[0] > Opos - ps ){
      s += P[0];
    }
    else{
      s += Opos - ps;
    }
  }
  else{
    if( P[0] > Bpos - ps ){
      s += P[0];
    }
    else{
      s += Bpos - ps;
    }
  }
  s --;
  printf("Push %c s = %d\n", R[n], s);

  return s;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  char R[100];
  int T, N, P[100];
  int res, t, j;

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
    fscanf(filein, "%d ", &N);
    printf("%d ", N);
    for( j = 0; j < N - 1; j ++ ){
      fscanf(filein, "%c %d ", R + j, P + j);
      printf("%c %d ", R[j], P[j]);
    }
    fscanf(filein, "%c %d\n", R + j, P + j);
    printf("%c %d\n", R[j], P[j]);

    // Solve & Output
    res = Solver(N, R, P);
    fprintf(fileout, "Case #%d: %d\n", t + 1, res);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
