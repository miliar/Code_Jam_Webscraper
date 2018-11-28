#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define VAR(name, val) __typeof(val) name = val
#define FOREACH(it, begin, end) for(VAR(it, begin), n=end; it != n; ++it)
#define PB push_back
#define FS first
#define SN second

long long W[2000][2000][11];
int T[2000][2000][11];

long long lpyt(int A, int B, int C) {
   if (T[A][B][C] == 1) return W[A][B][C];
   if (C * A >= B) return 0;
//   if ( A == B - C ) return 0;
   long long V = 1000000000;
   int minidx = 0;
   for (int x = A+1; x < B; x++) {
      int t = 1+max(lpyt(A, x, C), lpyt(x, B, C));
      if (t < V) {
         V = t;
         minidx =x;
      }
   }
//   printf("%d: %d min idx: %d (val: %lld)\n", A, B, minidx, V);
   W[A][B][C] = V;
   T[A][B][C] = 1;
   return V;
}

void solve(int T) {
   int A, B, C;
   scanf("%d%d%d", &A, &B, &C);

   long long res = W[A][B][C];
   printf("Case #%d: %lld\n", T, res);
}

int main() {
   for (int i = 2; i <= 10; i++) 
      lpyt(1, 1000, i);

   int T;
   scanf("%d", &T);

   for (int i = 0; i < T; i++) {
      solve(i+1);
   }

   return 0;
}
