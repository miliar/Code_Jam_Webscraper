#include <iostream>
#include <string>

using namespace std;

string str;

void translate(int k) {
  switch (str[k]) {
    case 'a':
      str[k] = 'y';
      return;
    case 'b':
      str[k] = 'h';
      return;
    case 'c':
      str[k] = 'e';
      return;
    case 'd':
      str[k] = 's';
      return;
    case 'e':
      str[k] = 'o';
      return;
    case 'f':
      str[k] = 'c';
      return;
    case 'g':
      str[k] = 'v';
      return;
    case 'h':
      str[k] = 'x';
      return;
    case 'i':
      str[k] = 'd';
      return;
    case 'j':
      str[k] = 'u';
      return;
    case 'k':
      str[k] = 'i';
      return;
    case 'l':
      str[k] = 'g';
      return;
    case 'm':
      str[k] = 'l';
      return;
    case 'n':
      str[k] = 'b';
      return;
    case 'o':
      str[k] = 'k';
      return;
    case 'p':
      str[k] = 'r';
      return;
    case 'q':
      str[k] = 'z';
      return;
    case 'r':
      str[k] = 't';
      return;
    case 's':
      str[k] = 'n';
      return;
    case 't':
      str[k] = 'w';
      return;
    case 'u':
      str[k] = 'j';
      return;
    case 'v':
      str[k] = 'p';
      return;
    case 'w':
      str[k] = 'f';
      return;
    case 'x':
      str[k] = 'm';
      return;
    case 'y':
      str[k] = 'a';
      return;
    case 'z':
      str[k] = 'q';
      return;
    default:
      return;
  }
  return;
}

int main(void) {
  int T = 0;
  cin >> T;
  cin.get();
  for (int i = 1; i <= T; ++i) {
    getline(cin, str);
    int length = str.length();
    for (int j = 0; j < length; ++j)
      translate(j);
    cout << "Case #" << i << ": " << str << endl;
  }
  return 0;
}
