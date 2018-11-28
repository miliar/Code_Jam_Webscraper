#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <stdint.h>

using namespace std;

int main(int argc, char *argv[]) {
  int cases;
  cin >> cases;

  for(int cas = 1; cas <= cases; ++cas) {
    uint64_t N, K;
    cin >> N >> K;
    cout << "Case #" << cas << ": " << (((K % (1 << N)) == ((1 << N) -1)) ? "ON" : "OFF") << endl;
  }

  return 0;
}
