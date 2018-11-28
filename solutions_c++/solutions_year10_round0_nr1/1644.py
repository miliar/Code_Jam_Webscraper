#include <iostream>

using namespace std;

int main() {

  int T, N, K;
  cin >> T;
  for (int i=0; i < T; ++i) {
	   cin >> N >> K;
	   int m = (1 << N)-1;
	   int b = (K & m)==m;
	   cout << "Case #" << i+1 << ": " << (b ? "ON":"OFF") << "\n";
  }

}
