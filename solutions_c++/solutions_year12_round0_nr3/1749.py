#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <cctype>
#include <numeric>
#include <bitset>
using namespace std;

#define rep(i,n) for(int (i)=0; (i)<(int)(n); ++(i))
#define foreach(c,i) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)

enum { kN = 2000001 };
// enum { kN = 10000 };
vector<int> v[kN];

void f() {
  for (int i = 12; i < kN; ++i) {
    stringstream ss;
    ss << i;
    string s(ss.str());
    for (int j = 0; j < s.size() - 1; ++j) {
      rotate(s.begin(), s.begin() + 1, s.end());
      if (s[0] == '0') continue;
      if (atoi(s.c_str()) <= i) continue;
      v[i].push_back(atoi(s.c_str()));
    }
    sort(v[i].begin(), v[i].end());
    v[i].erase(unique(v[i].begin(), v[i].end()), v[i].end());
  }
}

int main() {
  f();
  int T;
  scanf("%d", &T);
  rep(loop,T) {
    int A, B, ans = 0;
    scanf("%d%d", &A, &B);
    for (int i = A; i < B; ++i) {
      for (int j = 0; j < v[i].size(); ++j) {
        if (v[i][j] <= B) {
          ++ans;
          // printf("%d : %d %d\n", ans, i, v[i][j]);
        }
      }
    }
    printf("Case #%d: %d\n", loop+1, ans);
  }
  return 0;
}
