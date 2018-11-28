#include <iostream>
#include <cstring>
using namespace std;

const int di[] = {1, 0, -1, 1};
const int dj[] = {0, 1, 1, 1};
char A[60][60], B[60][60];
int wins[200];

int main() {
  int nt, C = 1;
  cin >> nt;
  int n, nw;
  while (nt-- && cin >> n >> nw) {
    memset(B, '.', sizeof B);
    for (int i = 0; i < n; ++i) {
      cin >> A[i];
      int jj = n-1;
      for (int j = n-1; j >= 0; --j)
	if (A[i][j] != '.')
	  B[i][jj--] = A[i][j];
    }

    memset(wins, 0, sizeof wins);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
	if (B[i][j] != '.') {
	  for (int k = 0; k < 4; ++k) {
	    int ii = i+di[k], jj = j+dj[k];
	    int r = 1;
	    while (ii >= 0 && ii < n && jj >= 0 && jj < n &&
		   B[ii][jj] == B[i][j])
	      ii += di[k], jj += dj[k], ++r;
	    if (r >= nw)
	      ++wins[B[i][j]];
	  }
	}
    cout << "Case #" << C++ << ": ";
    if (wins['B'] && wins['R'])
      cout << "Both";
    else if (wins['B'])
      cout << "Blue";
    else if (wins['R'])
      cout << "Red";
    else
      cout << "Neither";

    cout << endl;
  }
}
