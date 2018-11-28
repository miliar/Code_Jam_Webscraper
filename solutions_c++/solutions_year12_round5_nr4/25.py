#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int special(char c) {
  return (c == 'o' ||
          c == 'i' ||
          c == 'e' ||
          c == 'a' ||
          c == 's' ||
          c == 't' ||
          c == 'b' ||
          c == 'g');
}

int main() {
  int t; cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    int k; cin >> k;

    set<string> s;
    int edges = 0;
    map<char, int> deg;

    string dummy; getline(cin, dummy);
    string input; getline(cin, input);

    for (int i = 0; i < input.size() - 1; ++i) {
      string curr = input.substr(i, 2);
      if (s.count(curr)) {
        continue;
      } else {
        s.insert(curr);
        if (special(curr[0]) && special(curr[1])) {
          edges += 4;
          deg[curr[0]] += 4;
          deg[curr[1]] -= 4;
        }
        else if (special(curr[0])) {
          edges += 2;
          deg[curr[0]] += 2;
          deg[curr[1]] -= 2;
        }
        else if (special(curr[1])) {
          edges += 2;
          deg[curr[0]] += 2;
          deg[curr[1]] -= 2;
        }
        else {
          edges += 1;
          deg[curr[0]] += 1;
          deg[curr[1]] -= 1;
        }
      }
    }

    int count = 0;
    for (map<char, int>::iterator iter = deg.begin(); iter != deg.end(); ++iter) {
      if (iter->second > 0) count += iter->second;
    }
    if (count == 0) count = 1;
    count += edges;

    cout << "Case #" << case_num << ": " << count << endl;
  }
  return 0;
}