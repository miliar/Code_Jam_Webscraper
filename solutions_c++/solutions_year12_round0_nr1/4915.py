#include <iostream>
#include <string>

using namespace std;

char table[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
                'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
                'j', 'p', 'f', 'm', 'a', 'q'};

char transform(char x) {
  if (x == ' ')
    return x;
  return table[x - 'a'];
}

int main() {
  int n;
  cin >> n;
  string s;
  getline(cin, s);
  for (int i = 1; i <= n; ++i) {
    getline(cin, s);
    for (int j = 0; j < s.length(); ++j)
      s[j] = transform(s[j]);
    cout << "Case #" << i << ": " << s << endl;
  }

  return 0;
}
