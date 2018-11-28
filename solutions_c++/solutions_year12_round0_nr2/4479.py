#include <cstdio>
#include <string>

using namespace std;

int minValue(int S, int sub) {
   sub = max(0, S - sub);
   return S + 2*sub;
}

void solve() {
   int a[222] = {0};
   int N, surp, minS;
   scanf("%d %d %d", &N, &surp, &minS);
   const int minSurp = minValue(minS, 2), minBoring = minValue(minS, 1);

   int sol = 0;
   for (int i=0; i<N; i++) {
      int totalScore;
      scanf("%d", &totalScore);
      if (totalScore >= minBoring) {
         sol++;
      } else if (totalScore >= minSurp && surp > 0) {
         surp--;
         sol++;
      }
   }
   printf("%d\n", sol);
}

int main() {
   freopen("B-small-attempt0.in", "rb", stdin);
   freopen("B-data.txt", "wb", stdout);

   int tst;
   scanf("%d\n", &tst);
   for (int i=1; i<=tst; i++) {
      printf("Case #%d: ", i);
      solve();
   }
   fclose(stdout);
}