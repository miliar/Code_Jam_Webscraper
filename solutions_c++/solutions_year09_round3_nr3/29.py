#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

const int N = 200000;
const int M = 200;

const __int64 INFTY = 1000000000000000LL;

int n, m;
int released[N];
int pos[M];
bool cached[M][M];
__int64 opt[M][M];

__int64 cost(int from, int i, int to) {
  return pos[to] - pos[from] - 1 - 1;
}

__int64 calc(int from, int to) {
  if (to - from - 1 < 1) {
    return 0;
  }
  if (cached[from][to]) {
    return  opt[from][to];
  }
  __int64 result = INFTY;
  for (int i = from + 1; i < to; i++) {
    result = min(result, calc(from, i) + calc(i, to) + cost(from, i, to));
  }
  cached[from][to] = true;
  opt[from][to] = result;
 // std::cout << "[" << from << ", " << to << "] = " << result << endl;
  return result;
}

int main() {
  ifstream input("test.in");
  ofstream output("test.out");

  int test_cases;
  input >> test_cases;
  for (int test = 0; test < test_cases; test++) {
    input >> n >> m;
    memset(released, 0, sizeof(released));
    for (int i = 0; i < m; i++) {
      int id;
      input >> id;
      released[id] = true;
    }

    int count = 0;
    for (int i = 1; i <= n; i++) {
      if (released[i]) {
        ++count;
        pos[count] = i;
      }
    }
    pos[0] = 0;
    pos[m + 1] = n + 1;

    memset(cached, 0, sizeof(cached));
    output << "Case #" << test + 1 << ": " << calc(0, m + 1) << endl;
  }

  input.close();
  output.close();

  return 0;
}