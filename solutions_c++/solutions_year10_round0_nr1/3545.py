#include <iostream>

using namespace std;

int main() {
  int T, N, K;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
	// create target
    int target = (1<<(N-1));
    target |= (target >> 1);
    target |= (target >> 2);
    target |= (target >> 4);
    target |= (target >> 8);
	target |= (target >> 16);
    printf("Case #%d: %s\n", t,	((K & target) == target) ? "ON" : "OFF");
  } 
}