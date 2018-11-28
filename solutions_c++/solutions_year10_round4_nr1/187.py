#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

#define filename "A-large"

int diamond[64][64];

int main()
{
  freopen (filename ".in", "rt", stdin);
  freopen (filename ".out", "wt", stdout);
  
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
	  int k;
	  cin >> k;
	  for (int i = 0; i < k; ++i) {
		  for (int j = 0; j <= i; ++j) {
			  cin >> diamond[i - j][j];
		  }
	  }
	  for (int i = 1; i < k; ++i) {
		  for (int j = 0; j < k-i; ++j) {
			  cin >> diamond[k - 1 - j][j + i];
		  }
	  }
	  int size, x, y;
	  bool found = false;
	  for (size = k; !found; ++size) {
		  for (int dx = 0; dx <= size-k && !found; ++dx) {
			  for (int dy = 0; dy <= size-k && !found; ++dy) {
				  bool ok = true;
				  for (int i = 0; ok && i < k; ++i) {
					  for (int j = 0; ok && j < k; ++j) {
						  x = dy + j - dx;
						  y = dx + i - dy;
						  if (x >= 0 && x < k && y >= 0 && y < k &&
							  diamond[i][j] != diamond[x][y]
							 )
							  ok = false;
                          x = size - 1 - dy - j - dx;
						  y = size - 1 - dx - i - dy;
						  if (x >= 0 && x < k && y >= 0 && y < k &&
							  diamond[i][j] != diamond[x][y]
							 )
							  ok = false;
					  }
				  }
				  if (ok) found = true;
			  }
		  }
	  }
	  cout << "Case #" << test << ": " << (size-1)*(size-1) - k*k << endl;
  }

  return 0;
}