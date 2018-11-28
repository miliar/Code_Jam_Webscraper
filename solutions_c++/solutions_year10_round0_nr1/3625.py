#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
int main() {
  int T, N, K;
  cin >> T;
  for (int rr = 1; rr <= T; ++rr) {
    cin >> N >> K;
    printf("Case #%d: %s\n", rr, 
	   ((K+1)%(1<<N)) ? "OFF" : "ON");
  }
  return 0;
}
