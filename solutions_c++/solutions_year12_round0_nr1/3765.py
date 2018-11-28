#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
  int t; scanf("%d\n", &t);
  for (int tt = 1; tt <= t; tt++){
    cout << "Case #" << tt << ": ";
    char s[256]; cin.getline(s, 256);

    int L = strlen(s);
    for (int i = 0; i < L; i++){
      if (s[i] == ' ') cout << " ";
      else if (s[i] == 'a') cout << "y";
      else if (s[i] == 'o') cout << "k";
      else if (s[i] == 'z') cout << "q";
      else if (s[i] == 'e') cout << "o";
      else if (s[i] == 'j') cout << "u";
      else if (s[i] == 'p') cout << "r";
      else if (s[i] == 'm') cout << "l";
      else if (s[i] == 'y') cout << "a";
      else if (s[i] == 's') cout << "n";
      else if (s[i] == 'l') cout << "g";
      else if (s[i] == 'c') cout << "e";
      else if (s[i] == 'k') cout << "i";
      else if (s[i] == 'd') cout << "s";
      else if (s[i] == 'x') cout << "m";
      else if (s[i] == 'v') cout << "p";
      else if (s[i] == 'n') cout << "b";
      else if (s[i] == 'i') cout << "d";
      else if (s[i] == 'r') cout << "t";
      else if (s[i] == 'b') cout << "h";
      else if (s[i] == 't') cout << "w";
      else if (s[i] == 'h') cout << "x";
      else if (s[i] == 'w') cout << "f";
      else if (s[i] == 'f') cout << "c";
      else if (s[i] == 'u') cout << "j";
      else if (s[i] == 'g') cout << "v";
      else if (s[i] == 'q') cout << "z";
      else cout << "?";
    }
    cout << endl;
  }
  return 0;
}
