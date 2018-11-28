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

#define DEBUG(format, args...) do { fprintf(stderr, format, ## args); fflush(stderr); } while (0)
#define PRINT(format, args...) do { fprintf(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

int pz[64];
char bf[64];

int GetLastOne(const char *bf);

int main() {
  int i, j, N, A, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &N);
    for (i=0; i<N; i++) {
      scanf("%s", bf);
      pz[i]=GetLastOne(bf);
    }
    A=0;
    for (i=0; i<N; i++) {
      for (j=i; pz[j]>i; j++)
        A++;
      for (j--; j>=i; j--)
        pz[j+1]=pz[j];
    }
    PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}

int GetLastOne(const char *bf) {
  int i, A=(-1);
  for (i=0; bf[i]; i++)
    if (bf[i]=='1')
      A=max(A, i);
  return A;
}
