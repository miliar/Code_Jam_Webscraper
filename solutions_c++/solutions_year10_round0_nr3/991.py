#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef unsigned long long UINT64;
typedef long long INT64;

#if 0
printf("%lld %lld %lld\n", iR, iK, iN);
for (UINT64 i = 0; i < iN; ++i) printf("%lld ", iGList[i]);
printf("\n");
#endif

int main() {
  //  freopen("C.in","r",stdin);
  freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
  //	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
  //	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
  int testcase; scanf("%d",&testcase);
  for (int caseId=1; caseId <= testcase; caseId++) {
    UINT64 iR, iK, iN;
    UINT64 iGList[1001];
    scanf("%lld %lld %lld\n", &iR, &iK, &iN);
    for (UINT64 i = 0; i < iN; ++i) scanf("%lld", &iGList[i]);

    UINT64 nRounds = 0;
    UINT64 total = 0;
    UINT64 curGp = 0;
    while (nRounds < iR) {
      UINT64 curNum = 0;
      UINT64 curGpNum = 0;
      while (1) {
        if (curGpNum >= iN ||
            curNum + iGList[curGp] > iK) {
          total += curNum;
          break;
        } else {
          curGpNum++;
          curNum += iGList[curGp];
          curGp = (curGp + 1) % iN;
        }
      }
      nRounds++;
    }

    printf("Case #%d: ",caseId);
    printf("%lld", total);
    printf("\n");
  }
  return 0;
}
