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

    int C; scanf("%d", &C);
    vector<string> combine;
    for (int i = 0; i < C; ++i) { char tmp[3]; scanf("%s", tmp); combine.push_back(tmp); }

    int D; scanf("%d", &D);
    vector<string> opposed;
    for (int i = 0; i < D; ++i) { char tmp[2]; scanf("%s", tmp); opposed.push_back(tmp); }
    int N; scanf("%d", &N);

    string ans = "";
    char c;
    scanf("%c", &c);
    for (int i = 0; i < N; ++i) {
      scanf("%c", &c);

      ans += c;
      int n = ans.size();
      if (n < 2) continue;

      bool found = false;
      for (int e = 0; e < combine.size(); ++e) {
        if (((ans[n - 1] == combine[e][0]) && (ans[n - 2] == combine[e][1])) ||
            ((ans[n - 1] == combine[e][1]) && (ans[n - 2] == combine[e][0]))) {
          ans = ans.substr(0, n - 2);
          ans += combine[e][2];
          found = true;
          break;
        }
      }
      if (found) continue;
      for (int e = 0; e < opposed.size(); ++e) {
        int p = string::npos;
        if (ans[n - 1] == opposed[e][0]) {
          p = ans.find(opposed[e][1]);
        } else if (ans[n - 1] == opposed[e][1]){
          p = ans.find(opposed[e][0]);
        }
        if (p != string::npos) {
          ans = "";
        }
      }
    }
    printf("[");
    for (int i = 0; i < ans.size(); ++i) {
      if (i == ans.size() - 1) {
        printf("%c", ans[i]);
      } else {
        printf("%c, ", ans[i]);
      }
    }
    printf("]\n");
  }
  return 0;
}
