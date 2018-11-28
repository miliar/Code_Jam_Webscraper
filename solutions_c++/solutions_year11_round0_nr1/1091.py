#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    int n;
    cin >> n;
    cout << "Case #" << tcase << ": ";
    int op = 1, bp = 1;
    int ot = 0, bt = 0;
    int t = 0;
    for(int i=0;i<n;i++){
      char c;
      int p;
      cin >> c >> p;
      if(c=='O') {
	t = t + 1 + max(abs(op - p) - abs(ot - t), 0);
	ot = t;
	op = p;
      } else {
	t = t + 1 + max(abs(bp - p) - abs(bt - t), 0);
	bt = t;
	bp = p;
      }
    }
    cout << t << '\n';
  }
}
