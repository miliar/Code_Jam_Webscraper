#include <cstdio>


using namespace std;

int N;
int A[16];

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d", &N);
      for (int i = 0; i < N; ++i)
         scanf("%d", A+i);
      int best_sum = -1;
      for (int mask = (1<<N)-2; mask > 0; --mask) {
         int pile1 = 0, pile2 = 0, sum = 0;
         for (int j = 0; j < N; ++j) {
            if (mask & (1<<j)) {
               pile1 ^= A[j];
               sum += A[j];
            }
            else
               pile2 ^= A[j];
         }
         if (pile1 == pile2)
            if (best_sum < sum)
               best_sum = sum;
      }
      printf("Case #%d: ", tc);
      if (best_sum < 0)
         puts("NO");
      else
         printf("%d\n", best_sum);
   }
   return 0;
}
