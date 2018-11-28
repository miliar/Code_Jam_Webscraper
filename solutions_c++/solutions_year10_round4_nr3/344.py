#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define VAR(name, val) __typeof(val) name = val
#define FOREACH(it, begin, end) for(VAR(it, begin), n=end; it != n; ++it)
#define PB push_back
#define FS first
#define SN second

int T[102][102];

void testcase(int TESTCASE) {

   int R;
   scanf("%d", &R);
   for (int y = 0; y <= 101; y++) {
      for (int x = 0; x <= 101; x++) {
         T[y][x] = 0;
      }
   }

   for (int i = 0; i < R; i++) {
      int x1, y1, x2, y2;
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      for (int y = y1; y <= y2; ++y) {
         for (int x = x1; x <= x2; ++x) {
            T[y][x] = 1;
         }
      }
   }
   int turns = 0;
   while (true) {
      bool hasOne = false;
      for (int y = 100; y >= 0; --y) {
         for (int x = 100; x >= 0; --x) {
            if (T[y][x] == 1) hasOne = true;
            if (T[y-1][x] == 1 && T[y][x-1] == 1) T[y][x] = 1;
            if (T[y-1][x] == 0 && T[y][x-1] == 0) T[y][x] = 0;
         }
      }
      if (!hasOne) break;
      ++turns;
   }
   printf("Case #%d: %d\n", TESTCASE, turns);
}

int main() {

   int T;
   scanf("%d", &T);
   for (int i = 1; i <= T; ++i) {
      testcase(i);
   }

   return 0;
}
