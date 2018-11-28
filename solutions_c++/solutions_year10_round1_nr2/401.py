
#include <iostream>

using namespace std;

int main() {
  int T, D, I, M, N, A[100], B[101][256];
  for (int i = 0; i < 256; i++)
    B[0][i] = 0;
  cin >> T;
  for (int z = 1; z <= T; z++) {
    cin >> D >> I >> M >> N;
    for (int i = 0; i < N; i++)
      cin >> A[i];
    
    //cout << D << "," << I << "," << M << "," << N << "\n";
    //for (int i = 0; i < N; i++)
    //  cout << A[i] << " ";
    //cout << "\n";

    int x;
    for (int i = 1; i <= N; i++) {
      x = 1000000000;
      for (int j = 0; j < 256; j++) {
	int y = j < A[i-1] ? A[i-1]-j : j-A[i-1];
	B[i][j] = 1000000000;
	for (int k = 0; k < i; k++) {
	  if (M == 0) {
	    int d = y + B[k][j] + D*(i-k-1);
	    //if (z == 8) cout << k << "," << y << "," << B[k][j] << "," << D*(i-k-1) << "\n";
	    if (d < B[i][j]) B[i][j] = d;
	  }
	  else for (int l = 0; l < 256; l++) {
	    int c = l < j ? j-l : l-j;
	    int d = y + B[k][l] + D*(i-k-1);
	    if (c > 0) d += (c - 1)/M*I;
	    if (d < B[i][j]) {
	      B[i][j] = d;
	      //if (z == 16) cout << l << "," << j << "," << c << "," << y << "," << B[k][l] << "," << D*(i-k-1) << "," << (c-1)/M*I << "\n";
	    }
	  }
	}
	if (B[i][j] < x) {
	  x = B[i][j];
	  //if (z == 16) cout << i << "," << j << ": " << B[i][j] << "\n";
	}
      }
    }
    cout << "Case #" << z << ": " << x << "\n";
  }
}
