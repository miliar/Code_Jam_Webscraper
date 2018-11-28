#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

const string map = "yhesocvxduiglbkrztnwjpfmaq";

char trans(char c) {

  return 'a' <= c && c <= 'z' ? map[c - 'a'] : c;

}

int main() {

  int T;
  scanf("%d ", &T);
  for (int t = 1; t <= T; ++t) {
    string line;
    getline(cin, line);
    cout << "Case #" << t << ": ";
    for (int i = 0; i < line.length(); ++i) {
      cout << trans(line[i]);
    }
    cout << endl;
  }

  return 0;

}
