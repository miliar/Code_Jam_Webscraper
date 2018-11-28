#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int INF=1000008;

int fd[51][51];

int check_diamond(int N, int S, int y, int x);
int get_value(int N, int S, int i, int j, int y, int x);

int main() {
  int i, y, x, oy, ox, N, S, A, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &N);
    y=x=0;
    oy=ox=0;
    for (i=0; i<N*N; i++) {
      scanf("%d", &fd[y--][x++]);
      if (y<0) {
        y=(++oy);
        x=0;
        if (y==N) {
          y=N-1;
          x=(++ox);
        }
      }
      else if (x==N) {
        y=N-1;
        x=(++ox);
      }
    }
    A=INF;
    for (S=N; A==INF; S++)
      for (i=0; i<=S-N; i++) {
        A=min(A, check_diamond(N, S, 0, i));
        A=min(A, check_diamond(N, S, S-N, i));
        A=min(A, check_diamond(N, S, i, 0));
        A=min(A, check_diamond(N, S, i, S-N));
      }
    PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}

int check_diamond(int N, int S, int y, int x) {
  int i, j, v1, v2, v3;
  for (i=0; i<S; i++)
    for (j=0; j<S; j++) {
      v1=get_value(N, S, i, j, y, x);
      v2=get_value(N, S, j, i, y, x);
      v3=get_value(N, S, S-j-1, S-i-1, y, x);
      if (v1>=0) {
        if (v2>=0 && v1!=v2) return INF;
        if (v3>=0 && v1!=v3) return INF;
      }
      else if (v2>=0 && v3>=0 && v2!=v3)
        return INF;
    }
  return S*S-N*N;
}

int get_value(int N, int S, int i, int j, int y, int x) {
  S=(-1);
  if (y<=i && i<=y+N-1)
    if (x<=j && j<=x+N-1)
      return fd[i-y][j-x];
  return -1;
}
