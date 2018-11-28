#include <cstdio>
#include <ctype.h>
#include <string.h>
#include <set>

#define DEBUG(...)
//#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int T;

int A,B;

void readInput() {
   scanf("%d %d", &A, &B);
}


long long int solve() {
   long long int res = 0;
   for (int n=A; n<=B; ++n) {
      DEBUG("n=%d\n", n);
      char ns[20]; // n as string, twice
      sprintf(ns, "%d%d", n, n);
      int l = strlen(ns)/2;
      set<int> S;
      
      // go through all possible m, starting with eg 51234
      char* b = ns + l - 1; // beginning pointer
      char* e = ns + 2*l - 1; // end pointer (where we write '\0')
      do {
         *e = '\0';
         int m;
         sscanf(b, "%d", &m);
         DEBUG("   %d\n", m);
         if (m > n && m <= B) {
            S.insert(m);
         }
         b--;
         e--;
      } while (b > ns);
      res += S.size();
   }
   return res;
}



int main() {
   scanf("%d ", &T);
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d: %lld\n", i, solve());
      solve();
   }
   return 0;
}

