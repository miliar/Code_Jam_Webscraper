#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

#define PROBLEM_ID "C"

const int MOD = 10000;

int SubsequenceCount(const string& s1, const string& s2) {
  vector< vector<int> > answer(s1.length() + 1, vector<int>(s2.length() + 1, 0));
  for (int i = 0; i <= s1.length(); ++i) {
    answer[i][0] = 1;
  }
  for (int first_elements = 1; first_elements <= s2.length(); ++first_elements) {
    for (int prefix_length = 1; prefix_length <= s1.length(); ++prefix_length) {
      for (int last = prefix_length - 1; last >= 0; --last) {
        if (s1[last] == s2[first_elements - 1]) {
          answer[prefix_length][first_elements] += answer[last][first_elements - 1];
          if (answer[prefix_length][first_elements] >= MOD) {
            answer[prefix_length][first_elements] -= MOD;
          }
        }
      }
    }
  }
  return answer[s1.length()][s2.length()];
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests_count;
  cin >> tests_count;
  char buf[10000];
  gets(buf);
  for (int test_number = 0; test_number < tests_count; ++test_number) {
    gets(buf);
    string s1 = buf;
    string s2 = "welcome to code jam";
    printf("Case #%d: %.4d\n", test_number + 1, SubsequenceCount(s1, s2));
  }
  return 0;
}
