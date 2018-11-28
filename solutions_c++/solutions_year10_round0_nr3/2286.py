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

  int N;
  is >> N;
  for (int n = 1; n <= N; ++n) {
    int s = 0;
    int R, k, N;
    is >> R >> k >> N;
    vector<int> v(N, 0);
    for (int i = 0; i < N; ++i) is >> v[i];
    int j = 0;
    for (int i = 0; i < R; ++i) {
      int r = 0, g = N;
      while (r + v[j] <= k && g-- > 0) {
        r += v[j];
        j = (j + 1) % N;
      }
      s += r;
    }
    cout << "Case #" << n << ": " << s << endl;
  }

  return 0;
}
