
#include <iostream>

#define ABS(a) ((a) < 0 ? -(a) : (a))
#define MAX(a, b) ((a) < (b) ? (b) : (a))

using namespace std;

int main() {
  char r;
  int n, p, t;
  cin >> t;
  for (int z = 1; z <= t; ++z) {
    cin >> n;
    int a = 1, b = 1, c = 1, d = 1, q = 0;
    for (int i = 0; i < n; ++i) {
      cin >> r >> p;
      if (r == 'O') {
	int x = a + ABS(p - b);
	//cout << "O " << x << "," << q+1 << "\n";
	q = MAX(q + 1, x);
	a = q + 1;
	b = p;
      }
      else {
	int x = c + ABS(p - d);
	//cout << "O " << x << "," << q+1 << "\n";
	q = MAX(q + 1, x);
	c = q + 1;
	d = p;
      }
      //cout << "move " << i+1 << " at " << q << "\n";
    }
    cout << "Case #" << z << ": " << q << "\n";
  }
}
