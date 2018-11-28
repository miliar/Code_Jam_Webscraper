#include <iostream>
#include <cstring>
using namespace std;

int B[200][200];
/*
void pr() {
  for (int i = 0; i < 10; ++i, cout << endl)
    for (int j = 0; j < 10; ++j)
      cout << B[i][j] << ' ';
  cout << endl;
}
*/
int main() {
  int nt, C = 1;
  cin >> nt;
  int nr, x1, y1, x2, y2;
  while (nt-- && cin >> nr) {
    memset(B, 0, sizeof B);
    while (nr-- && cin >> x1 >> y1 >> x2 >> y2) {
      --x1, --y1, --x2, --y2;
      for (int i = x1; i <= x2; ++i)
	for (int j = y1; j <= y2; ++j)
	  B[i][j] = 1;
    }
    
    int k = 0;
    bool f;
    do {
      //pr();
      f = false;
      ++k;
      for (int i = 99; i >= 0; --i)
	for (int j = 99; j >= 0; --j) {
	  if (B[i][j] == k)
	    f = true;
	  if ((B[i][j] < k && i > 0 && B[i-1][j] == k &&
	       j > 0 && B[i][j-1] == k) ||
	      (B[i][j] == k && ((i > 0 && B[i-1][j] == k) ||
				(j > 0 && B[i][j-1] == k))))
	    B[i][j] = k+1, f = true;
	}
    } while (f);

    cout << "Case #" << C++ << ": " << k-1 << endl;
  }
}
