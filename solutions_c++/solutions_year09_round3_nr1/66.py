#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int T;

void work() {
  string str;
  cin >> str;
  set<char> H;
  int diff = 0;
  for (int i = 0; i < (int) str.length(); i++) {
    if (H.find(str[i]) == H.end()) {
      H.insert(str[i]);
      diff++;
    }
  }
  int base = max(2, diff);
  
  vector<int> digit = vector<int>(base);
  for (int i = 0; i < base; i++) {
    digit[i] = i;
  }
  swap(digit[0], digit[1]);
  int p = 0;
  map<char, int> S;
  long long result = 0;
  for (int i = 0; i < (int) str.length(); i++) {
    if (S.find(str[i]) == S.end()) {
      S[str[i]] = digit[p];
      p++;
    }
    result *= base;
    result += S[str[i]];
  }
  cout << result;
}

int main() {
  cin >> T;
  
  for (int i = 0; i < T; i++) {
    cout << "Case #" << (i + 1) << ": ";

    work();

    cout << endl;
  }
  
  return 0;
}
