#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>

#define D if(0)
using namespace std;

typedef long long Int;
int r,c,d;
Int w[512][512];
Int s[512][512];
Int sc[512][512];
int xc,yc;

Int get_s(int y, int x) { if (y < 0 || x < 0) return 0; else return s[y][x];}
Int get_w(int y, int x) { if (y < 0 || x < 0) return 0; else return w[y][x];}

int main(int argc, char const* argv[])
{
  int case_count;
  scanf("%d", &case_count);
  for (int case_index = 0; case_index < case_count; case_index++) {
    printf("Case #%d: ", case_index + 1);
    scanf("%d%d%d", &r,&c,&d);
    for (int y = 0; y < r; y++) {
      for (int x = 0; x < c; x++) {
        char ch;
        scanf(" %c", &ch);
        w[y][x] = ch - '0';
        s[y][x] = get_s(y,x-1)+get_s(y-1,x)-get_s(y-1,x-1)+w[y][x];
      }
    }

    // assume a center
    int k;
    for (k = r; k >= 3; k--) {
      bool succ = false;
      for (int yl = 0; yl < r; yl++) {
        if (yl + k > r) break;
        for (int xl = 0; xl < c; xl++) {
          if (xl + k > c) break;
          D printf("  (%d,%d), k = %d\n", yl, xl, k);
          // sum
          Int sumx = 0, sumy = 0;
          yc = yl + yl + k - 1;
          xc = xl + xl + k - 1;

          for (int y = yl; y < yl + k;y++){
            for (int x = xl; x < xl + k;x++) {
              if ((y == yl || y == yl + k - 1) 
                && (x == xl || x == xl + k - 1)) continue;
              sumx+=w[y][x] * (x * 2 - xc);
              sumy+=w[y][x] * (y * 2 - yc);
            }
          }
          D printf("sumx = %lld, sumy = %lld\n", sumx, sumy);
          if (sumx == 0&& sumy == 0) {
            succ = true;
            break;
          }
        }
        if (succ) break;
      }
      if (succ) {
        printf("%d\n", k);
        k=-1;
        break;
      }
    }
    if (k >= 0) printf("IMPOSSIBLE\n");






  }
  return 0;
}


