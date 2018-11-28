#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <cstdio>
#include <cmath>

using namespace std;

int A,B;
int used[10];
int mod;

int count(int a){
  int v = a;
  int ret = 0;
  used[0] = a;
  for (int i = 1; ; ++i) {
    v *= 10;
    v = v % mod + v / mod;
    for (int j = 0; j < i; ++j) {
      if (used[j] == v) return ret;
    }
    if (a < v && v <= B) {
      //      cout << a << " " << v << endl;
      ++ret;
    }
    used[i] = v;
  }
  return ret;
}

int solve(){
  int ans = 0;
  for (int i = A; i < B; ++i) {
    ans += count(i);
  }
  return ans;
}

int main(){
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> A >> B;
    mod = 1;
    while(mod <= B) {
      mod *= 10;
    }
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
