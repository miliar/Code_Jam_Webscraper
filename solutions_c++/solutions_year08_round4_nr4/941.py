#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

int enc(vector <int> &kk, string &s) {
  size_t bs(kk.size());
  string s1("");
  for (size_t i(0); i<s.size(); i += bs) {
    string block(s, i, bs);
    string from(block);
    for (size_t j(0); j<bs; j++)
      block[j] = from[kk[j]-1];
    s1 += block;
  }

  int ret(1);
  char cur(s1[0]);
  for (size_t i(1); i<s1.size(); i++) {
    if (s1[i] != cur) {
      ret++;
      cur = s1[i];
    }
  }

  return ret;
}

int solve(int k, string &s) {
  vector <int> kk(k, 0);
  for (int i(1); i<=k; i++) kk[i-1] = i;

  int ret(INT_MAX);
  do {
    ret = min(ret, enc(kk, s));
  } while(next_permutation(kk.begin(), kk.end()));

  return ret;
}

int main(int argc, char **argv) {
  int c;
  cin >> c;
  for (int i(1); i<=c; i++) {
    int k;
    string s;
    cin >> k;
    cin >> s;
    cout << "Case #" << i << ": " << solve(k, s) << endl;
  }

  return 0;
}
