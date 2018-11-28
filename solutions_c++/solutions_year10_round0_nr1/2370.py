#include <iostream>
#include <iomanip>
#include <iterator>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char* argv[]) {
  ifstream is("data.in");

  int T;
  is >> T;
  for (int t = 1; t <= T; ++t) {
    int N, K;
    is >> N >> K;
    int m = (1 << N) - 1;
    bool on = (K & m) == m;
    cout << "Case #" << t << ": " << (on ? "ON" : "OFF") << endl;
  }

  return 0;
}
