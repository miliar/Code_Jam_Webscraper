#include <cstdio>
#include <iostream>

using namespace std;

char m[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};

int main() {
  int n;
  cin >> n;
  string a;
  getline(cin, a);
  char rev[26];
  for (int i = 0; i < 26; i++) rev[m[i] - (int)'a'] = i + (int)'a';
  for (int i = 0; i < n; i++) {
    getline(cin, a);
    for (int j = 0; j < a.length(); j++)
      if (a[j] != ' ') a[j] = rev[a[j] - (int)'a'];
    cout << "Case #" << i + 1 << ": " << a << endl;
  }
  return 0;
}