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

map<int, vector<int> > M;

int main() {
  int TS;
  
  freopen("input.txt", "r", stdin);
  freopen("output.txt" ,"w", stdout);

  scanf("%d", &TS);
 
  for (int ts = 1; ts <= TS; ts++) {
    int n;
    M.clear();
    vector<int> v;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      int number;
      scanf("%d", &number);
      v.push_back(number);
    }

    for (int i = 0; i < (1<<n); i++) {
      int sum = 0;
      for (int j = 0; j < n; j++) {
        if (i & (1<<j)) {
          sum += v[j];
        }
      }
      M[sum].push_back(i);
    }

    map<int, vector<int> >::iterator it = M.begin();
    bool flag = false;
    int a, b;
    while (it != M.end() && !flag) {
      vector<int>& w = it->second;
      for (int i = 0 ; i < w.size() && !flag; i++) {
        for (int j = i + 1; j < w.size(); j++) {
          if ((w[i] & w[j]) == 0) {
            a = w[i];
            b = w[j];
            flag = true;
            break;
          }
        }
      }
      ++it;
    }
    printf("Case #%d:\n", ts);
    if (flag ) {
      for (int i = 0; i < n; i++) {
        if (a & (1<<i)) {
          printf("%d ", v[i]);
        }
      }
      puts("");
      for (int i = 0; i < n; i++) {
        if (b & (1<<i)) {
          printf("%d ", v[i]);
        }
      }
      puts("");
    } else {
      printf("Impossible\n");
    }
  }

  return 0;
}