#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

#include <assert.h>
#include <stdio.h>
#include <string.h>

typedef unsigned u;

const u maxT = 30;
const u maxD = 1000 * 1000 * 1000;
const u maxN = 10000;

u len[maxN];
u dist[maxN+1];

u swing[maxN];
u reached;

void doCase() {
   u N;
   cin >> N;
   assert(N >= 1 && N <= maxN);
   for (u n = 0; n < N; n++) {
      cin >> dist[n] >> len[n];
      assert(dist[n] > 0 && dist[n] <= maxD);
      assert(n == 0 || dist[n] > dist[n-1]);
      assert(len[n] > 0 && len[n] <= maxD);
   }
   u D;
   cin >> D;
   assert(D > 0 && D <= maxD && dist[N-1] < D);
   assert(dist[0] <= len[0]);

   dist[N] = D;
   swing[0] = dist[0];
   reached = 0;
   for (u n = 0; n <= reached && n < N; n++) {
      u s = swing[n];
      if (s > len[n]) s = len[n];
      while (reached < maxN) {
         u r = reached + 1;
         if (dist[r] <= dist[n] + s) {
            if (r == N) {
               cout << "YES";
               return;
            }
            swing[r] = dist[r] - dist[n];
            reached = r;
         } else {
            break;
         }
      }
   }
   cout << "NO";
}

int main() {
   u T;
   cin >> T;
   assert(T >= 1 && T <= maxT);

   for (u t = 1; t <= T; t++) {
      cout << "Case #" << t << ": ";
      doCase();
      cout << endl;
   }
   return 0;
}
