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

struct Digit {
  Digit(int d) {
    digits = bitset<64>(d);
    row = d;
  }
  bool operator<(const Digit &d) const { return row < d.row; }
  bitset<64> digits;
  int row;
};

int main() {
  int T;
  scanf("%d", &T);
  bitset<8> b(10);
  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);
    int N;
    scanf("%d", &N);
    vector<int> candies;
    for (int i = 0; i < N; ++i) { int c; scanf("%d", &c); candies.push_back(c); }
    sort(candies.begin(), candies.end());

    vector<Digit> ds(candies.begin(), candies.end());
    bool valid = true;
    for (int i = 0; i < ds[0].digits.size(); ++i) {
      int sum = 0;
      for (int j = 0; j < ds.size(); ++j) sum += ds[j].digits[i];
      if (sum % 2 == 1) {
        valid = false;
        break;
      }
    }

    if (!valid) {
      printf("NO\n");
    } else {
      long long ans = 0;
      for (int i = 1; i < ds.size(); ++i) ans += ds[i].row;
      printf("%lld\n", ans);
    }
  }
  return 0;
}
