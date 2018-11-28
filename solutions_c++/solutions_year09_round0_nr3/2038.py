#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

int main(void) {
  int n;
  string s, c = "welcome to code jam";
  char *st = (char *)malloc(sizeof(char) * 1024);
  cin >> n;
  cin.getline(st, 1024);
  for(int i = 0; i < n; ++i) {
    cin.getline(st, 1024);
    s = st;
    int count[s.length() + 1][c.length()];
    for(int j = 0; j < c.length(); ++j)
      count[0][j] = 0;
    for(int j = 1; j <= s.length(); ++j) {
      count[j][0] = count[j-1][0];
      if(s[j-1] == c[0]) ++count[j][0];
      for(int k = 1; k < c.length(); ++k) {
        count[j][k] = count[j-1][k];
        if(s[j-1] == c[k])
          count[j][k] += count[j-1][k-1];
        count[j][k] %= 10000;
      }
    }

    cout << "Case #" << (i + 1);
    printf(": %04i\n", count[s.length()][c.length()-1]);
  }
}
