#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

const int MAXN = 1010;
int freq[MAXN];

int main(void)
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) 
  {
    int N, L, H;
    scanf("%d %d %d", &N, &L, &H);
    for (int i = 0; i < N; ++i)
      scanf("%d", &freq[i]);
    
    int ret = -1;
    for (int f = L; f <= H; ++f) {
      int fail = 0;
      for (int i = 0; i < N; ++i)
        if (!(f % freq[i] == 0 || freq[i] % f == 0)) {
          fail = 1;
          break;
        }
      if (fail) continue;
      ret = f;
      break;
    }

    printf("Case #%d: ", t);
    if (ret == -1) 
      puts("NO");
    else 
      printf("%d\n", ret);
  }

  return 0;
}
