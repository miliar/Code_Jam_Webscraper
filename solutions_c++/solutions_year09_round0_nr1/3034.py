#include <iostream>
#include <string>
#include <set>

using namespace std;

int L, D, N;
string dict[5000];
set<char> H;

bool match(const string &token, const string &pattern) {
  int p = 0;
  for (int i = 0; i < L; i++) {
    if (token[p] == '(') {
      H.clear();
      while (token[++p] != ')') {
	H.insert(token[p]);
      }
      if (H.find(pattern[i]) == H.end()) {
	return false;
      }
      p++;
    } else {
      if (token[p] != pattern[i]) {
	return false;
      }
      p++;
    }
  }
  return true;
}

int cnt(const string &token) {
  int result = 0;
  for (int i = 0; i < D; i++) {
    if (match(token, dict[i])) {
      result++;
    }
  }
  return result;
}

int main() {
  cin >> L >> D >> N;
  for (int i = 0; i < D; i++) {
    cin >> dict[i];
  }
  for (int i = 0; i < N; i++) {
    string token;
    cin >> token;
    static int kase = 0;
    cout << "Case #" << (++kase) << ": " << cnt(token) << endl;
  }
  return 0;
}
