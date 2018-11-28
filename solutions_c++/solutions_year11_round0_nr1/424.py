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
#include <utility>
#include <algorithm>
using namespace std;

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

typedef pair<char[4], int> PCI;
#define FST first
#define SND second

int I;
PCI in[108];

int signum(int n);
int next_instruction(char c, int p);

int main() {
  int i, pb, po, ib, io, t, T, d, A;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &I);
    for (i=0; i<I; i++)
      scanf("%s %d", in[i].FST, &in[i].SND);
    A=0;
    pb=po=1;
    ib=next_instruction('B', 0);
    io=next_instruction('O', 0);
    while (ib<I || io<I)
      if (ib<io) {
        d=abs(in[ib].SND-pb)+1;
        pb=in[ib].SND;
        A+=d;
        if (io<I)
          po=(d>=abs(in[io].SND-po) ? in[io].SND : po+d*signum(in[io].SND-po));
        ib=next_instruction('B', ib+1);
      }
      else {
        d=abs(in[io].SND-po)+1;
        po=in[io].SND;
        A+=d;
        if (ib<I)
          pb=(d>=abs(in[ib].SND-pb) ? in[ib].SND : pb+d*signum(in[ib].SND-pb));
        io=next_instruction('O', io+1);
      }
    PRINT("Case #%d: %d\n", t, A);
  }
  return 0;
}

int signum(int n) {
  if (n<0)
    return -1;
  if (n>0)
    return +1;
  return 0;
}

int next_instruction(char c, int p) {
  while (p<I && in[p].FST[0]!=c)
    p++;
  return p;
}
