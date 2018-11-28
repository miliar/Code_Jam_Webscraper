#include <iostream>
#include <fstream>

using namespace std;

int main() {
  fstream file;
  file.open("A-large.in");

  long long T;
  file >> T;
  long long N, M;
  long long c = 1;
  while (file >> N && file >> M) {
    while (N > 0) {
      if (M % 2) {
        if (N == 1)
          cout << "Case #" << c << ": ON\n";
      }
      else {
        cout << "Case #" << c << ": OFF\n";
        break;
      }
      M = M >> 1;
      N--;
    }
    c++;
  }
  return 0;
}
