#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int T;

int main() {
  cin >> T;
  for (int nn = 1; nn <= T; nn++) {
    int K; cin >> K;
    list<int> data; int res[5001];
    for (int i = 0; i < K; i++) data.push_back(i);
    list<int>::iterator it = data.begin(), ol;

    for (int i = 1; i <= K; i++) {
      for (int j = 1; j < i; j++) { it++; if (it == data.end()) it = data.begin(); }
      res[*it] = i;
      ol = it; it++; if (it == data.end()) it = data.begin();
      data.erase(ol);
    }

    cout << "Case #" << nn << ":";

    int n; cin >> n;
    for (int i = 0; i < n; i++) {
      int t; cin >> t;
      cout << " " << res[t - 1];
    }
    cout << endl;
  }
  return 0;
}