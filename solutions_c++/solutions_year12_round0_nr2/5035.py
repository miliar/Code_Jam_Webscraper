#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;

  cin >> T;
  for (int i = 0; i < T; i++) {
    int n, s, p;
    cin >> n >> s >> p;
    
    int x, y;
    int ret = 0;
    int one = 0;
    for (int j = 0; j < n; j++) {
      cin >> x;
      y = x / 3 + (x % 3 > 0);
      if (y >= p)
	++ret;
      else if (y == p-1 && x % 3 != 1 && x > 1)
	++one;
    }
    
    ret += min(s, one);
    cout << "Case #" << i+1 << ": " << ret << endl;
  }
  
  return 0;
}
