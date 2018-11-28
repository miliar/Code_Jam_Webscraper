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

const int MAX_GROUPS=1008;

int gp[MAX_GROUPS];
int cn[MAX_GROUPS];
int nx[MAX_GROUPS];
i64 sm[MAX_GROUPS];
i64 zm[MAX_GROUPS];

int GetNext(int p, int S, int G);
i64 GetSum(int p1, int p2, int G);

int main() {
  int i, j, c, t, T, R, S, G;
  i64 A, z;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d %d", &R, &S, &G);
    for (i=0; i<G; i++) {
      scanf("%d", gp+i);
      sm[i]=(i==0 ? gp[i] : sm[i-1]+gp[i]);
    }
    memset(cn, -1, G*sizeof(int));
    cn[i=0]=c=0;
    zm[i]=z=0;
    do {
      c++;
      nx[i]=(j=GetNext(i, S, G));
      z+=GetSum(i, j, G);
      if (cn[i=j]<0) {
        cn[j]=c;
        zm[j]=z;
      }
      else
        break;
    }
    while (true);
    A=j=0;
    while (j!=i && R>0) {
      A+=GetSum(j, nx[j], G);
      j=nx[j];
      R--;
    }
    if (R>0) {
      A+=(z-zm[i])*(R/(c-cn[i]));
      R%=(c-cn[i]);
    }
    while (R>0) {
      A+=GetSum(j, nx[j], G);
      j=nx[j];
      R--;
    }
    PRINT("Case #%d: %lld\n", t, A);
  }
  return 0;
}

int GetNext(int p, int S, int G) {
  int i, s=0;
  i=p;
  while (true) {
    s+=gp[i++];
    if (i==G)
      i=0;
    if (i==p || s+gp[i]>S)
      break;
  }
  return i;
}

i64 GetSum(int p1, int p2, int G) {
  if (p1==p2)
    return sm[G-1];
  if (p1<p2)
    return sm[p2-1]-(p1==0 ? 0 : sm[p1-1]);
  if (p1>p2)
    return (sm[G-1]-sm[p1-1])+(p2==0 ? 0 : sm[p2-1]);
  assert(0);
}
