#include <string>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for ((i) = 0; (i) < (int)(n); (i)++)
// Type
#define OSS ostringstream
#define ISS istringstream
#define CAST(x,type)  *({OSS oss; oss << (x); ISS iss(oss.str()); static type _r; iss >> _r; &_r; })

int main() {
  int T;
  scanf("%d", &T);

  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);

    int numButtons;
    scanf("%d", &numButtons);
    long long time = 0;
    int orange = 1;
    int blue = 1;
    int orangeMovable = 0;
    int blueMovable = 0;
    for (int i = 0; i < numButtons; ++i) {
      char color; int k; int proceed;
      scanf(" %c %d", &color, &k);
      if (color == 'O') {
        proceed = max(abs(orange - k) - orangeMovable, 0) + 1;
        orange = k;
        orangeMovable = 0;
        blueMovable += proceed;
        time += proceed;
      } else {
        proceed = max(abs(blue - k) - blueMovable, 0) + 1;
        blue = k;
        blueMovable = 0;
        orangeMovable += proceed;
        time += proceed;
      }
    }
    printf("%lld\n", time);
  }
  return 0;
}
