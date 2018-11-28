#include <cstdio>
#include <string.h>
#include <stack>
#include <vector>
#include <algorithm>


#define DEBUG(...)
//#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int T;

int N;
int d[10002];
int l[10002];
int D;

void readInput() {
   scanf("%d", &N);
   for (int i=0; i<N; ++i) scanf("%d %d", &(d[i]), &(l[i]));
   scanf("%d", &D);
}

int B[10002];
#define INF 2000000000

void solve() {
   for (int i=0; i<=N; ++i) B[i] = 0;
   if (l[0] < d[0]) {
      printf("NO");
      return;
   }
   d[N] = D;
   l[N] = 1; // just >0
   B[0] = d[0];
   int j=1; // where to begin improve B
   for (int i=0; i<=N; ++i) {
      if (B[i] == 0) {
         printf("NO");
         return;
      }
      for (; j<=N && d[i]+B[i] >= d[j]; ++j) {
         B[j] = min(l[j], d[j]-d[i]);
      }
   }
   if (B[N] == 0) {
      printf("NO");
   } else if (B[N] == 1) {
      printf("YES");
   } else {
      printf("WEIRD");
   }
   /*
   if (d[N-1] + B[N-1] >= D) {
      printf("YES");
   } else {
      printf("NO");
   }
   */
}



int main() {
   scanf("%d ", &T);
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d: ", i);
      solve();
      printf("\n");
   }
   return 0;
}

