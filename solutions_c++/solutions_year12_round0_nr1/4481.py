#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

char s[400];

char v[]= {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x','d', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

void translate() {
  for (int i = 0; s[i] && s[i] != '\n'; i++) {
    if (s[i] == ' ') continue;
    s[i] = v[s[i]-'a'];
  }
}

int main() {
  int tt;
  scanf("%d\n", &tt);
  for (int t = 0; t < tt; t++) {
    fgets(s, sizeof(s), stdin);
    translate();
    cout << "Case #" << t+1 << ": " << s;
  }
  return 0;
}
