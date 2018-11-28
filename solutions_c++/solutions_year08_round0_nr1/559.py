#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int maxM = 1000 + 10;
const int maxN = 100 + 10;
const int maxL = 100;
const int infinite = 1 << 28;

char Q[maxM][maxL], E[maxN][maxL];
int f[maxM][maxN];
int data, N, M, ans;

void getinf() {
  scanf("%d\n", &N);
  for (int i = 1; i <= N; i++) gets(E[i]);
  scanf("%d\n", &M);
  for (int i = 1; i <= M; i++) gets(Q[i]);
}

void work() {
  memset(f, 0, sizeof(f));
  for (int i = 1; i <= M; i++)
    for (int j = 1; j <= N; j++) {
      f[i][j] = infinite;
      if (strcmp(Q[i], E[j])) {
	for (int k = 1; k <= N; k++)
	  f[i][j] <?= f[i - 1][k] + (j != k);
      }
    }
  ans = infinite;
  for (int j = 1; j <= N; j++) ans <?= f[M][j];
}

int main() {
  scanf("%d", &data);
  for (int tot = 1; tot <= data; tot++) {
    getinf();
    work();
    printf("Case #%d: %d\n", tot, ans);
  }
}
