#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int N, T;
long long K;
int main() {
   int Case = 1;
   scanf("%d", &T);
   while (T --) {
      scanf("%d%lld", &N, &K);
      K %= (1LL << N);
      printf("Case #%d: %s\n", Case ++, (K + 1 == (1LL << N)) ? "ON" : "OFF");
   }
   return 0;
}


