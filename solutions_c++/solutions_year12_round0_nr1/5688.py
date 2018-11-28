#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "A"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  string from = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string to = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
  map<char, char> code;
  for (int i = 0; i < from.length(); ++i) {
    code[from[i]] = to[i];
  }
  code['z'] = 'q';
  code['q'] = 'z';
  /*for (char c = 'a'; c <= 'z'; ++c) {
    if (!code.count(c)) {
      cerr << c << " is not present" << endl;
    } else {
      cerr << c << ' ' << code[c] << endl;
    }
  }*/
  int test_count;
  cin >> test_count;
  char buf[10000];
  gets(buf);
  for (int test_index = 0; test_index < test_count; ++test_index) {
    gets(buf);
    string output = buf;
    for (int i = 0; i < output.length(); ++i) {
      output[i] = code[buf[i]];
    }
    cout << "Case #" << test_index + 1 << ": " << output << endl;
  }
  return 0;
}
