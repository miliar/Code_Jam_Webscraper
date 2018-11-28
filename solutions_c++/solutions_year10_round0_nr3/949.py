#include <iostream>
using namespace std;

int main() {
  int t, r, k, n;
  int group[1001];
  int next[1001];
  int cost[1001];
  cin >> t;
  for(int i=1; i<=t; i++) {
    cin >> r >> k >> n;
    for(int j=0; j<n; j++) {
      cin >> group[j];
      next[j] = -1;
    }

    // calculate next and cost
    int j = 0;
    while(next[j] == -1) {
      int sum = group[j], last = j;
      while(sum <= k) {
	cost[j] = sum;
	last = (last + 1) % n;
	sum += group[last];
	if(last == j)
	  break;
      }
      next[j] = last;
      j = last;
    }

    // rounds
    int total = 0;
    j = 0;
    for(int round=1; round<=r; round++) {
      total += cost[j];
      j = next[j];
    }
    cout << "Case #" << i << ": " << total << endl;
  }
  return 0;
}
