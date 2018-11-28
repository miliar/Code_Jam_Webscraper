#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define VAR(name, val) __typeof(val) name = val
#define FOREACH(it, begin, end) for(VAR(it, begin), n=end; it != n; ++it)
#define PB push_back
#define FS first
#define SN second

int W[520][520];

int findmax(int x, int y, int N, int M){
   int maxS = 0;
   for (int a = 0; a < min(N-x,M-y); a++) {
      bool ok = true;
      for (int q = y; q <= y +a ; q++) {
         for (int p = x; p <= x+a; p++) {
            if (W[q][p] != 2 && (p == x || W[q][p] == 1-W[q][p-1]) && (p == x || q == y || W[q][p] == W[q-1][p-1]) && (q == y || W[q][p] == 1 - W[q-1][p])){ 

            } else {
//               printf("Falsed: %d %d because %d %d: %d\n", x, y, p ,q, W[q][p]);
               ok = false;
               break;
            }
         }
         if (!ok) break;
      }
      if (ok) {
         maxS = a + 1;
//         printf("Found %d at %d %d, %d\n", maxS, x, y, W[y][x]);
      }
   }
   return maxS;
}

int hexof(char c){ 
   if (c >= 'A') return c - 'A' + 10;
   return c - '0';
}

void solve(int T){ 
   int M,N;
   scanf("%d%d\n", &M, &N);
   int sizes[1000];
   for (int i = 0; i < 1000; i++) {
      sizes[i] = 0;
   }
   for (int i = 0; i < M; i++) {
      for (int j = 0; j < N / 4; j++) {
         char x;
         scanf("%c", &x);
         if (x == ' ' || x == '\n') {
            j --;continue;
         }
         int c = hexof(x);
         W[i][4*j+3] = c & 1;
         W[i][4*j+2] = (c & 2) >> 1;
         W[i][4*j+1] = (c & 4) >> 2;
         W[i][4*j] = (c & 8) >> 3;
      }
      scanf("%*c");
   }


      int gmaxS = 0;
      int gmaxY = 0;
      int gmaxX = 0;

      do {
         gmaxS = 0;

      for (int y = 0; y < M; y++) {
         for (int x = 0; x < N; x++) {
//            printf("Serch at %d %d\n", x, y);
            int maxS = findmax(x,y,N,M);
            if (maxS > gmaxS) {
               gmaxS = maxS;
               gmaxX = x;
               gmaxY = y;
            }
         }
      }
      sizes[gmaxS] += 1;
      for (int y = gmaxY; y < gmaxY + gmaxS; y++) {
      for (int x = gmaxX; x < gmaxX + gmaxS; x++) {
//         printf("clear: %d %d\n", y, x);
         W[y][x] = 2;
      }
      }
      }while (gmaxS > 0);

      int cnt = 0;
   for (int i = 1; i < 1000; i++) {
      if (sizes[i] != 0) cnt++;
   }

   printf("Case #%d: %d\n", T, cnt);
   for (int i = 999; i > 0; i--) {
      if (sizes[i] > 0 ) printf("%d %d\n", i, sizes[i]);
   }

}

int main() {

   int T;
   scanf("%d", &T);
   for (int i = 1; i <= T; i++) {
      solve(i);
   }

   return 0;
}
