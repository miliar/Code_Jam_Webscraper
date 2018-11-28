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

int T, k;
string s;
vector<int> perm;

int res() {
  string res = s;
  for (int start = 0; start < s.size(); start += k) {
    for (int i = 0; i < k; i++) res[start + i] = s[start + perm[i]];
  }
  int r = 0, pos = -1; char last = 0;
  while (++pos < res.size()) {
    if (res[pos] != last) { last = res[pos]; r++; }
  }

  return r;
}

int main() {

  cin >> T;
  for (int nn = 1; nn <= T; nn++) {
    cin >> k >> s;
    int f = 1;
    
    perm.clear();
    for (int i = 1; i <= k; i++) {
      f *= i;
      perm.push_back(i - 1);
    }

    int r = 1000000000;
    for (int i = 0; i < f; i++) {
      r = min(r, res());
      next_permutation(perm.begin(), perm.end());
    }

    cout << "Case #" << nn << ": " << r << endl;
  }

  return 0;
}