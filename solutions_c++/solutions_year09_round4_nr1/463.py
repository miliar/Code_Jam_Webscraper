#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
int one[64];
int N;

int main() {
  int numcase;
  cin >> numcase;
  for (int ncase = 1; ncase <= numcase; ++ncase) {
    cin >> N;
    memset(one, 0, sizeof(one));
    for (int i = 0; i < N; ++i) {
      char c;
      for (int j = 0; j < N; ++j) {
	cin >> c;
	if (c == '1') one[i] = j+1;
      }
    }

    int ans = 0;
    for (int i = 0; i < N; ++i) {
      for (int j = i; j < N; ++j) {
	if (one[j] <= i+1) {
	  ans += j-i;
	  int temp = one[j];
	  for (int k = j; k > i; --k) {
	    one[k] = one[k-1];
	  }
	  one[i] = temp;
	  break;
	}
      }
    }
    cout << "Case #" << ncase << ": " << ans << endl;
  }
}
