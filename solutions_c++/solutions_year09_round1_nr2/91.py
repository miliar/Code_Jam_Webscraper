#include <stdio.h>

int s[20][20][3];
int r[40][40];

#define MAX 2000000000
int cal(int N, int M) {
  int i, j, k;
  for (i = 0; i < 2 * N; i++) {
    for (j = 0; j < 2 * M; j++) {
      r[i][j] = -1;
    }
  }
  r[2*N-1][0] = 0;
  for (k = 0; k < 4*N*M; k++) {
    for (i = 2*N-1; i >= 0; i--) {
      for (j = 0; j < 2*M; j++) {
        if (i%2==1) {
          // top of block
          if (i+1<2*N) {
            if (r[i+1][j]!=-1 && (r[i+1][j]+2<r[i][j] || r[i][j]==-1)) {
              r[i][j] = r[i+1][j]+2;
            }
          }
          if (i-1>=0) {
            if (r[i-1][j]!=-1) {
              int time = (r[i-1][j]-s[i/2][j/2][2]) % (s[i/2][j/2][0]+s[i/2][j/2][1]);
              if (time < 0) time+= (s[i/2][j/2][0]+s[i/2][j/2][1]);
              int min;
              if (time < s[i/2][j/2][0]) {
                min = r[i-1][j]+1;
              } else {
                min=r[i-1][j]+(s[i/2][j/2][0]+s[i/2][j/2][1])-time+1;
              }
              if (min < r[i][j] || r[i][j]==-1) r[i][j] = min;
            }
          }
        } else {
          // bottom of block
          if (i+1<2*N) {
            if (r[i+1][j]!=-1) {
              int time = (r[i+1][j]-s[i/2][j/2][2]) % (s[i/2][j/2][0]+s[i/2][j/2][1]);
              if (time < 0) time+= (s[i/2][j/2][0]+s[i/2][j/2][1]);
              int min;
              if (time < s[i/2][j/2][0]) {
                min = r[i+1][j]+1;
              } else {
                min=r[i+1][j]+(s[i/2][j/2][0]+s[i/2][j/2][1])-time+1;
              }
              if (min < r[i][j] || r[i][j]==-1) r[i][j] = min;
            }
          }
          if (i-1>=0) {
            if (r[i-1][j]!=-1 && (r[i-1][j]+2<r[i][j] || r[i][j]==-1)) {
              r[i][j] = r[i-1][j]+2;
            }
          }
        }
        if (j%2==1) {
          // left of block
          if (j+1<2*M) {
            if (r[i][j+1]!=-1 && (r[i][j+1]+2<r[i][j] || r[i][j]==-1)) {
              r[i][j] = r[i][j+1]+2;
            }
          }
          if (j-1>=0) {
            if (r[i][j-1]!=-1) {
              int time = (r[i][j-1]-s[i/2][j/2][2]) % (s[i/2][j/2][0]+s[i/2][j/2][1]);
              if (time < 0) time+= (s[i/2][j/2][0]+s[i/2][j/2][1]);
              int min;
              if (time < s[i/2][j/2][0]) {
                min = r[i][j-1]+s[i/2][j/2][0]-time+1;
              } else {
                min=r[i][j-1]+1;
              }
              if (min < r[i][j] || r[i][j]==-1) r[i][j] = min;
            }
          }
        } else {
          // right of block
          if (j+1<2*M) {
            if (r[i][j+1]!=-1) {
              int time = (r[i][j+1]-s[i/2][j/2][2]) % (s[i/2][j/2][0]+s[i/2][j/2][1]);
              if (time < 0) time+= (s[i/2][j/2][0]+s[i/2][j/2][1]);
              int min;
              if (time < s[i/2][j/2][0]) {
                min = r[i][j+1]+s[i/2][j/2][0]-time+1;
              } else {
                min=r[i][j+1]+1;
              }
              if (min < r[i][j] || r[i][j]==-1) r[i][j] = min;
            }
          }
          if (j-1>=0) {
            if (r[i][j-1]!=-1 && (r[i][j-1]+2<r[i][j] || r[i][j]==-1)) {
              r[i][j] = r[i][j-1]+2;
            }
          }
        }
      }
    }
  }
  return r[0][2*M-1];
}

int main() {
  FILE *in = fopen("in.txt", "r");
  FILE *out = fopen("out.txt", "w");
  int C;
  int N, M;
  int i, j, k;
  fscanf(in, "%d", &C);
  for (i = 0; i < C; i++) {
    fscanf(in, "%d %d", &N, &M);
    for (j = 0; j < N; j++) {
      for (k = 0; k < M; k++) {
        int S, W, T;
        fscanf(in, "%d", &S);
        fscanf(in, "%d", &W);
        fscanf(in, "%d", &T);
        s[j][k][0] = S;
        s[j][k][1] = W;
        s[j][k][2] = T;
      }
    }
    int ret = cal(N, M);
    fprintf(out, "Case #%d: %d\n", i+1, ret);
  }

  fclose(in);
  fclose(out);
  return 0;
}
