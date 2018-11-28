#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

void apply(int *p, char *S, char *C, int k, int n) {
  int i, j;
  for (i = 0; i < n/k; i++)
    for (j = 0; j < k; j++)
      C[i*k+j] = S[i*k+p[j]];
}

int compa(char *S, int n) {
  int i, res = 0;
  for (i = 1; i < n; i++)
    if (S[i] != S[i-1])
      res++;
  return res+1;
}

#define MAXK 10
#define MAXN 1123

int perm[MAXK];
char S[MAXN], C[MAXN];

int main() {
  int t, cases = 1;
  int k, i, n, res;

  scanf("%d", &t);
  while (t--) {
    scanf("%d ", &k);
    gets(S);

    for (i = 0; i < k; i++)
      perm[i] = i;
    
    res = 1000000;
    n = strlen(S);
    do {
      int p;
      apply(perm, S, C, k, n);
      if ((p = compa(C, n)) < res)
	res = p;
    } while (next_permutation (perm, perm+k));

    printf("Case #%d: %d\n", cases++, res);
  }

  return 0;
}
