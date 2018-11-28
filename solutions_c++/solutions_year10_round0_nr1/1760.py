#include <cstdio>

using namespace std;

int main() {
   int T;

   scanf("%d", &T);
   for(int tp = 0; tp < T; ++tp) {
      int n, k;
      scanf("%d%d", &n, &k);
      
      printf("Case #%d: %s\n", tp+1, ((k & ((1<<n)-1)) == ((1<<n)-1) ? "ON" : "OFF" ));
   }

   return 0;
}
