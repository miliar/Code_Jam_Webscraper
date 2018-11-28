#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {

  char mapping[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};

  char actualMapping[26];
  for (int i = 0; i < 26; i++) {
    actualMapping[mapping[i] - 'a'] = i + 'a';
  }

  string str;
  int N; scanf("%d", &N);
  getline(cin, str);
  for (int i = 0; i < N; i++) {
    getline(cin, str);
    cout << "Case #" << i + 1 << ": ";
      for (int i = 0; i < str.size(); i++) {
        if (str[i] <= 'z' && str[i] >= 'a') {
          cout << actualMapping[str[i] - 'a'];
        } else {
          cout << str[i];
        }
      }
    cout << endl;
  }

  return 0;
}
