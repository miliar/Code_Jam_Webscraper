#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define VAR(name, val) __typeof(val) name = val
#define FOREACH(it, begin, end) for(VAR(it, begin), n=end; it != n; ++it)
#define PB push_back
#define FS first
#define SN second

int check(pair<int, int> &P, pair<int, int> &Q) {
   return (int)(P.FS >= Q.FS && P.SN <= Q.SN);
}

void solve(int T) {
   vector<pair<int, int> > V;
   int N;
   scanf("%d", &N);

   for (int i = 0; i < N; i++) {
      int A, B;
      scanf("%d%d", &A, &B);
      V.PB(make_pair(A,B));
   }

   int counter = 0;
   for (int i = 0; i < N; i++) {
      for (int j = i+1; j < N; j++) {
         counter += (check(V[i], V[j]) || check(V[j], V[i]));
      }
   }
   printf("Case #%d: %d\n", T, counter);
}

int main() {
   int T;
   scanf("%d", &T);

   for (int i = 1; i <= T; i++) {
      solve(i);
   }

   return 0;
}
