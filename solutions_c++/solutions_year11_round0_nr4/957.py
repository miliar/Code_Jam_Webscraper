#include <cstdio>

#include <algorithm>
#include <vector>

using namespace std;

#define MAXN 10

typedef long long llong;

int N;
int P[MAXN];

double E[MAXN+1];

int main(int argc, char* argv[]) {
   E[1] = 0.0;
   P[0] = 0;
   int nfact = 1;
   for (N = 2; N <= MAXN; ++N) {
      P[N-1] = N-1;
   // sort(P, P+N);
      nfact *= N;
      double num = 0;
      int cnt_one_cycle = 0;
      do {
         vector<int> cycles;
         int used = 0;
         for (int i = 0; i < N; ++i) {
            if (used & (1<<i)) continue;
            int cnt = 0;
            for (int k = i; !(used & (1<<k)); k = P[k]) {
               used |= 1 << k;
               ++cnt;
            }
            cycles.push_back(cnt);
         }
         if (cycles.size() == 1)
            ++cnt_one_cycle;
         else {
            num += 1;
            for (int j = 0; j < cycles.size(); ++j)
               num += E[ cycles[j] ];
         }
      } while (next_permutation(P, P+N));
      E[N] = (num + cnt_one_cycle) / (nfact - cnt_one_cycle);
   // fprintf(stderr, "%d: %.5lf\n", N, E[N]);
   }

   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d", &N);
      for (int i = 0; i < N; ++i) {
         scanf("%d", P+i);
         --P[i];
      }
      vector<int> cycles;
      int used = 0;
      for (int i = 0; i < N; ++i) {
         if (used & (1<<i)) continue;
         int cnt = 0;
         for (int k = i; !(used & (1<<k)); k = P[k]) {
            used |= 1 << k;
            ++cnt;
         }
         cycles.push_back(cnt);
      }
      double res = 0.0;
      for (int j = 0; j < cycles.size(); ++j)
         res += E[ cycles[j] ];
      printf("Case #%d: %.8lf\n", tc, res);
   }

   return 0;
}
