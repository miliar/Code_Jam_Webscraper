#include <cstdio>
#include <string.h>
#include <map>

// equal sums

#define DEBUG(...)
//#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int T;

int N;

int S[500];

map<long long int, unsigned int> M; // sum => bitmask

void readInput() {
   scanf("%d", &N);
   for (int i=0; i<N; ++i) {
      scanf("%d", &(S[i]));
   }
}



void solve() {
   M.clear();
   for (unsigned int i = 0; i<=0xfffff; ++i) {
      long long int sum = 0;
      int j = 0;
      for (unsigned int mask = 1; mask <= 0x80000; mask = mask*2) {
         if ((mask & i) != 0) sum += S[j];
         j++;
      }
      if (M.find(sum) != M.end()) {
         unsigned int other = M[sum];
         j=0;
         for (unsigned int mask = 1; mask <= 0x80000; mask = mask*2) {
            if ((mask & other) != 0) printf("%d ", S[j]);
            j++;
         }
         printf("\n");
         j=0;
         for (unsigned int mask = 1; mask <= 0x80000; mask = mask*2) {
            if ((mask & i) != 0) printf("%d ", S[j]);
            j++;
         }
         printf("\n");
         return;
      } else {
         M[sum] = i;
      }
   }
   printf("Impossible\n");
}



int main() {
   scanf("%d ", &T);
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d:\n", i);
      solve();
   }
   return 0;
}

