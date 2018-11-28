#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

char B[2][104][104];

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      int R;
      scanf("%d", &R);
      memset(B, '0', sizeof(B));
      while (R-- > 0) {
         int X1, X2, Y1, Y2;
         scanf("%d %d %d %d", &X1, &Y1, &X2, &Y2);
         FOR(r, Y1, Y2) FOR(c, X1, X2)
            B[0][r][c] = '1';
      }

      int nones = 0;
      FOR(r, 1, 100) FOR(c, 1, 100)
         if (B[0][r][c] == '1')
            ++nones;
      
      int res = 0;
      for (; ; ++res) {
         if (nones == 0)
            break;
         int t = res & 1;
         int nt = 1 - t;
         FOR(r, 1, 100) FOR(c, 1, 100) {
            if ((B[t][r-1][c] == '1') ^ (B[t][r][c-1] == '1')) {
               B[nt][r][c] = B[t][r][c];
               continue;
            }
            if (B[t][r][c] == '1') {
               B[nt][r][c] = B[t][r-1][c] == '0' ? '0' : '1';
               if (B[nt][r][c] == '0')
                  --nones;
            }
            else {
               B[nt][r][c] = B[t][r-1][c] == '1' ? '1' : '0';
               if (B[nt][r][c] == '1')
                  ++nones;
            }
         }
      }
      printf("Case #%d: %d\n", tc, res);
   }
   return 0;
}
