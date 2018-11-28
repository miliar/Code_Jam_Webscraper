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

typedef pair<int, int> node;

bool isOk[1234];

int main() {
  int TS;
  
  freopen("input.txt", "r", stdin);
  freopen("output.txt" ,"w", stdout);

  scanf("%d", &TS);
 
  for (int ts = 1; ts <= TS; ts++) {
    memset(isOk, 0, sizeof(isOk));
    int n;
    scanf("%d", &n);

    int total = 0;
    vector<node> scores;
    for (int i = 0; i < n; i++) {
      int score;
      scanf("%d", &score);
      scores.push_back(node(score, i));
      total += score;
    }

    vector<double> ans;
    int size = scores.size();
    printf("Case #%d: ", ts);
    int real_total = total;
    while (1) {
      ans.clear();
      double average = (total + real_total) / (double)size;

      int i;
      for (i = 0; i < scores.size(); i++) {
        if (!isOk[i]) {
          if (average - scores[i].first < 0.0) {
            total -= scores[i].first;
            size -= 1;
            isOk[i] = true;
            break;
          }
          ans.push_back((average - scores[i].first) / (double)real_total * 100.0);
        }
      }
      if (i == scores.size()) break;
    }
    int idx = 0;
    for (int i = 0; i < scores.size(); i++, idx++) {
      if (isOk[i]) {
        printf("%lf ", 0.0);
        idx -= 1;
      } else {
        printf("%lf ", ans[idx]);
      }
    }
    puts("");
  }

  return 0;
}