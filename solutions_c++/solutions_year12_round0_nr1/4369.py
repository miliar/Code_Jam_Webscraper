#include <iostream>
using namespace std;

char mapping[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
  int T;
  cin >> T;
  char message[101];
  cin.getline(message, 101);
  for (int t = 0; t < T; t++) {
    cout << "Case #" << (t + 1) << ": ";
    cin.getline(message, 101);
    for (char* c = message; *c; c++) {
      if (*c >= 'a' && *c <= 'z') {
        cout << mapping[*c-'a'];
      } else {
        cout << *c;
      }
    }
    cout << '\n';
  }
  return 0;
}
