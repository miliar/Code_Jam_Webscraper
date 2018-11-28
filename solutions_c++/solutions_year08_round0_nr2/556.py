#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int maxN = 400 + 10;

int T[maxN];
int ans[2];
int TT, NA, NB, N, data;

int getinf() {
  int h, m;

  scanf("%d", &TT);
  scanf("%d%d\n", &NA, &NB);
  memset(T, 0, sizeof(T));
  N = 0;
  for (int i = 0; i < NA; i++) {
    scanf("%d:%d", &h, &m);
    T[N++] = (h * 60 + m) * 100;
    scanf("%d:%d\n", &h, &m);
    m += TT;
    h += m / 60;
    m %= 60;
    T[N++] = (h * 60 + m) * 100 + 1;
  }
  for (int i = 0; i < NB; i++) {
    scanf("%d:%d\n", &h, &m);
    T[N++] = (h * 60 + m) * 100 + 10;
    scanf("%d:%d\n", &h, &m);
    m += TT;
    h += m / 60;
    m %= 60;
    T[N++] = (h * 60 + m) * 100 + 11;
  }
}

bool cmp(const int &a, const int &b) {
  return (a / 100 < b / 100 || (a / 100 == b / 100 && a % 10 > b % 10));
}

void work() {
  int L[2], num, kind;

  sort(T, T + N, cmp);
  ans[0] = ans[1] = L[0] = L[1] = 0;
  for (int i = 0; i < N; i++) {
    num = T[i] % 100 / 10;
    kind = T[i] % 10;
    if (kind) {
      L[1 - num]++;
    } else {
      if (L[num]) L[num]--;
      else ans[num]++;
    }
  }
}


int main() {
  scanf("%d", &data);
  for (int tot = 1; tot <= data; tot++) {
    getinf();
    work();
    printf("Case #%d: %d %d\n", tot, ans[0], ans[1]);
  }
}
