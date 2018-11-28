#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define VAR(name, val) __typeof(val) name = val
#define FOREACH(it, begin, end) for(VAR(it, begin), n=end; it != n; ++it)
#define PB push_back
#define FS first
#define SN second

int P;
int M[2000];
int cost[5000];
long long int overall[5000][12];
const long long INFTY = 1E9;

void testcase(int TESTCASE) {
   scanf("%d", &P);
   int teams = 1<<P;
   for (int i = 0; i < 5000; i++) {
      for (int j = 0; j < 12; j++) {
         overall[i][j] = INFTY;
      }
   }
   for (int i = 0; i < teams; ++i) {
      scanf("%d", M+i);
   }
   for (int i = P-1; i >= 0; --i) {
      for (int j = 0; j < (1<<i); ++j) {
         scanf("%d", &cost[j+(1<<i)]);
      }
   }

   for (int i = 0; i < teams; i++) {
      for (int j = 0; j < P - M[i]; ++j) overall[(1<<P)+i][j] = INFTY;
      for (int j = P - M[i]; j <= P; j++) overall[(1<<P)+i][j] = 0;
   }

   for (int level = P-1; level >= 0; --level) {
      for (int node = 0; node < (1<<level); ++node) {
//         printf("{");
         for (int maxv = 0; maxv <= level; ++maxv) {
            int address = (1<<level)+node;
            overall[address][maxv] = min(cost[address] + overall[2*address][maxv+1] + overall[2*address+1][maxv+1],
                                         overall[2*address][maxv] + overall[2*address+1][maxv]);
//            printf("(%d,%d): (%d) %lld   ", node, maxv, cost[address], overall[address][maxv]);
         }
//         printf("} ");
      }
//      printf("\n");
   }

   printf("Case #%d: %lld\n", TESTCASE, overall[1][0]);
}

int main() {

   int T;
   scanf("%d", &T);
   for (int i = 1; i <= T; ++i) {
      testcase(i);
   }

   return 0;
}
