#include <iostream>
#include <cassert>
#include <string>
#include <vector>
using namespace std;

int main() {
  int l, d, n;
  scanf(" %d %d %d", &l, &d, &n);
  vector<string> words;
  for (int i = 0; i < d; ++i) {
    string temp;
    cin >> temp;
    words.push_back(temp);
  }
  int test_case = 0;
  for (int i = 0; i < n; ++i) {
    string temp;
    cin >> temp;
    vector<string> parts;
    string build = "";
    for (int j = 0; j < temp.size(); ++j) {
      if (temp[j] == '(') {
        j++;
        build = "";
        while (temp[j] != ')') {
          build = build + temp[j];
          j++;
        }
      } else {
        build = temp[j];
      }
      parts.push_back(build);
    }
    assert(parts.size() == l);
    int matches = 0;
    for (int j = 0; j < words.size(); ++j) {
      bool flag = true;
      for (int k = 0; k < l; k++) {
        if (parts[k].find(words[j][k]) == string::npos) {
          flag = false;
          break;
        }
      }
      if (flag)
        matches++;
    }
    cout << "Case #" << ++test_case << ": " << matches << endl;
  }
  return 0;
}
