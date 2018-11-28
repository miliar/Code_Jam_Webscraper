#include <cstdio>

using namespace std;

void setup(bool val[], bool gate[], int M, int p = 0) {
  if (p < (M-1)/2) {
    setup(val, gate, M, 2*p+1);
    setup(val, gate, M, 2*p+2);
    if (gate[p]) val[p] = val[2*p+1] && val[2*p+2];
    else val[p] = val[2*p+1] || val[2*p+2];
    }
  }

int minChange(bool val[], bool gate[], bool change[], int V, int M, int p = 0) {
  if (val[p] == V) return 0;
  int m = 100000;
  if (p >= (M-1)/2) return m;
  int a = minChange(val, gate, change, 0, M, 2*p+1);
  int b = minChange(val, gate, change, 1, M, 2*p+1);
  int c = minChange(val, gate, change, 0, M, 2*p+2);
  int d = minChange(val, gate, change, 1, M, 2*p+2);
  if (V) {
    if (gate[p]) {
      if ((b+d) < m) m = b+d;
      if (change[p]) {
        if ((1+b) < m) m = 1+b;
        if ((1+d) < m) m = 1+d;
        }
      }
    else {
      if (b < m) m = b;
      if (d < m) m = d;
      }
    }
  else {
    if (gate[p]) {
      if (a < m) m = a;
      if (c < m) m = c;
      }
    else {
      if ((a+c) < m) m = a+c;
      if (change[p]) {
        if ((1+a) < m) m = 1+a;
        if ((1+c) < m) m = 1+c;
        }
      }
    }
  return m;
  }

int main() {
  int N; scanf("%d", &N);
  for (int c = 1; c <= N; ++c) {
    int M, V; scanf("%d %d", &M, &V);
    bool val[10000] = {false}, gate[10000] = {false}, change[10000] = {false};
    for (int i = 0; i < (M-1)/2; ++i) {
      int G, C; scanf("%d %d", &G, &C);
      gate[i] = G; change[i] = C;
      }
    for (int i = (M-1)/2; i < M; ++i) {
      int I; scanf("%d", &I);
      val[i] = I;
      }
    setup(val, gate, M);
    printf("Case #%d:", c);
    int m = minChange(val, gate, change, V, M);
    if (m > 10000)
      printf(" IMPOSSIBLE\n");
    else printf(" %d\n", m);
    }
  }