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

struct Stock {
  int pr[32];
  bool operator<(const Stock &st) const { return pr[0]<st.pr[0]; }
};

const int INF=1000008;

int S, P;
Stock st[108];
int co[108][108];
int mz[1<<16];
int mo[1<<16];

int CanOverlayOne(const Stock &s1, const Stock &s2);
int CanOverlayAll(int m);
int recurse(int m);

int main() {
  int i, j, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d", &S, &P);
    for (i=0; i<S; i++)
      for (j=0; j<P; j++)
        scanf("%d", &st[i].pr[j]);
    sort(st, st+S);
    for (i=0; i<S-1; i++)
      for (j=i+1; j<S; j++)
        co[j][i]=CanOverlayOne(st[j], st[i]);
    memset(mz, -1, sizeof mz);
    memset(mo, -1, sizeof mo);
    PRINT("Case #%d: %d\n", t, recurse((1<<S)-1));
  }
  return 0;
}

int CanOverlayOne(const Stock &s1, const Stock &s2) {
  for (int i=0; i<P; i++)
    if (s1.pr[i]<=s2.pr[i])
      return 0;
  return 1;
}

int CanOverlayAll(int m) {
  int &A=mo[m];
  if (A<0) {
    int i, l=(-1);
    A=0;
    for (i=0; i<S; i++)
      if (m&(1<<i))
        if (l<0)
          l=i;
        else if (co[i][l])
          l=i;
        else
          return A;
    A=1;
  }
  return A;
}

int recurse(int m) {
  int &A=mz[m];
  if (A<0)
    if (m==0)
      A=0;
    else {
      A=INF;
      for (int n=m; n>0; n=(n-1)&m)
        if (CanOverlayAll(n))
          A=min(A, 1+recurse(m-n));
    }
  return A;
}
