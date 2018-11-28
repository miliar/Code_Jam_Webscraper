#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

long T, N, K;

void do_case (int no_case) {
  cout << "Case #" << no_case << ": ";
  cin >> N >> K;
  ++K;
  while (N >= 0 && (K & 1) == 0) {
    --N;
    K >>= 1;
  }
  cout << (N <= 0? "ON":"OFF") << endl;
}

int main () {
  cin >> T;
  for (int i = 1; i <= T; ++i)
    do_case (i);
}
