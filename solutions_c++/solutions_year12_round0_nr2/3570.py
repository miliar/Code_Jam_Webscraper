#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int t;
  int n, s, p, num;
  int s_min;
  int min;
  int ans;

  cin >> t;
  
  for(int i = 0; i < t; i++){
    cin >> n >> s >> p;
    min = p * 3 - 2;
    s_min = p * 3 - 4;
    if (s_min < 1) s_min = 1;
    ans = 0;
    for (int j = 0; j < n; j++) {
      cin >> num;
      if (num >= min) {
	ans++;
	continue;
      }
      if (num >= s_min && s > 0) {
	ans++;
	s--;
	continue;
      }
    }

    cout << "Case #" << (i+1) << ": " << ans << endl;
  }

  return 0;
}
