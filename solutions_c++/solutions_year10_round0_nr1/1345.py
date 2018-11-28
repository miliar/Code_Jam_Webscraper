#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, K; cin >> N >> K;
    int mask = (1<<N)-1;
    printf("Case #%d: %s\n", t, (K&mask) == mask ? "ON" : "OFF");
  }
}
