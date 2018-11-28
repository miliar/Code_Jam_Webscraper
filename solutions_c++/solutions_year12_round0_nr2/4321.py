#include <algorithm>
#include <bitset>
#include <cmath>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

int main() {
  int TS;
  
  freopen("input.txt", "r", stdin);
  freopen("output.txt" ,"w", stdout);

  scanf("%d\n", &TS);
  for (int ts = 1; ts <= TS; ts++) {
    long long ans = 0;
    int n, s, p;

    scanf("%d %d %d", &n, &s, &p);
    for (int i = 0, temp; i < n; i++) {
      scanf("%d", &temp);
     
      if (temp >= p*3 - 2) {
        ans += 1;
      } else if (s >= 1 && temp >= 0 && p > 1 && temp >= p*3 - 4) {
        ans += 1;
        s -= 1;
      }
    }

    printf("Case #%d: %lld", ts, ans);

    puts("");
  }

  return 0;
}