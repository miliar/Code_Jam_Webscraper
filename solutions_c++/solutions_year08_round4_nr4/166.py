#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) { fprintf(stderr, format, ## args); fflush(stderr); }
#define PRINT(format, args...) { fprintf(stdout, format, ## args); DEBUG(format, ## args); }

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

char bf[50003];
char tp[50003];

int apply(int *pm, int P, char *bf, int B);

int main() {
  int i, t, T, K, L, A;
  int pm[32];
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %s", &K, bf);
    L=strlen(bf);
    for (i=0; i<K; i++)
      pm[i]=i;
    A=1000000;
    do
      A=min(A, apply(pm, K, bf, L));
    while (next_permutation(pm, pm+K));
    PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}

int apply(int *pm, int P, char *bf, int B) {
  int i, j, b, I=B/P, A=1;
  for (i=0; i<I; i++) {
    b=i*P;
    for (j=0; j<P; j++)
      tp[b+j]=bf[b+pm[j]];
  }
  for (i=1; i<B; i++)
    if (tp[i]!=tp[i-1])
      A++;
  return A;
}
