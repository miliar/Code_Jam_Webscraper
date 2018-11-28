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
#define PROBLEM_ID "D"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int GetCode(char c) {
  if (isalpha(c) && islower(c)) {
    return c - 'a';
  } else if (isdigit(c)) {
    return c - '0' + 26;
  } else {
    cerr << "Wrong char: " << c << endl;
    exit(1);
  }
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  map<char, char> mapping;
  mapping['o'] = '0';
  mapping['i'] = '1';
  mapping['e'] = '3';
  mapping['a'] = '4';
  mapping['s'] = '5';
  mapping['t'] = '7';
  mapping['b'] = '8';
  mapping['g'] = '9';
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int k;
    cin >> k;
    string s;
    cin >> s;
    const int CODES = 36;
    vector< vector<int> > G(CODES, vi(CODES, 0));
    for (int i = 0; i + 1 < s.length(); ++i) {
      G[GetCode(s[i])][GetCode(s[i + 1])] = 1;
      if (mapping.count(s[i])) {
        G[GetCode(mapping[s[i]])][GetCode(s[i + 1])] = 1;
        if (mapping.count(s[i + 1])) {
          G[GetCode(mapping[s[i]])][GetCode(mapping[s[i + 1]])] = 1;
        }
      }
      if (mapping.count(s[i + 1])) {
        G[GetCode(s[i])][GetCode(mapping[s[i + 1]])] = 1;
      }
    }
    int result = 1;
    vector<int> diff(CODES);
    for (int i = 0; i < CODES; ++i) {
      for (int j = 0; j < CODES; ++j) {
        result += G[i][j];
        if (i != j) {
          diff[i] += G[i][j];
          diff[j] -= G[i][j];
        }
      }
    }
    int sum_more = 0;
    int sum_less = 0;
    for (int i = 0; i < CODES; ++i) {
      if (diff[i] > 0) {
        sum_more += diff[i];
      } else if (diff[i] < 0) {
        sum_less += -diff[i];
      }
    }
    cerr << sum_more << ' ' << sum_less << endl;
    if (sum_more > 0) {
      result += sum_more - 1;
    }
    cout << "Case #" << test_index + 1 << ": " << result << endl;
  }
  return 0;
}
