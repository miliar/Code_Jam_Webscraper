#include <stdio.h>
#include <cstring>
const char* A = "welcome to code jam";

int N;
int D[20][1000];
#define M 10000

int main() {
  char buf[1000];
  fgets(buf, 1000, stdin);
  sscanf(buf, "%d", &N);
  for (int i = 1; i <= N; i++) {
    memset(D, 0, sizeof(D));
    fgets(buf, 1000, stdin);
    int L = strlen(buf);
    if (buf[L-1]=='\n') { buf[L-1] = '\0'; L--; }

    for (int l = 0; l < L; l++) if (buf[l]==A[0]) D[0][l] = 1;
    for (int j = 1; j < 19; j++) {
      for (int l = 0; l < L; l++) {
        if (buf[l] == A[j]) {
          for (int k = 0; k < l; k++) {
            D[j][l]+=D[j-1][k];
            D[j][l]%=M;
          }
        }
      }
    }

    int R = 0;
    for (int l = 0; l < L; l++) {
      R += D[18][l];
      R %= M;
    }
    printf("Case #%d: %04d\n", i, R);
  }
  return 0;
}
