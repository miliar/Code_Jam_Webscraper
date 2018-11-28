#include <iostream>

using namespace std;

const int N = 501;
const long MOD = 100003;

int main() {
  long binom[N][N];
  long pure[N][N];
  long A[N];

  for(int i = 0; i < N; i++) {
    binom[0][i] = 0;
    binom[i][0] = 1;
    pure[i][0] = 0;
    pure[0][i] = 0;
    pure[1][i] = 0;
  }
  
  for(int n = 1; n < N; n++) {
    for(int k = 1; k < N; k++) {
      binom[n][k] = (binom[n-1][k-1] + binom[n-1][k]) % MOD;
    }
  }

  for(int i = 2; i < N; i++) {
    pure[i][1] = 1;
  }

  A[0] = 0;
  A[1] = 0;
  A[2] = 1;

  for(int n = 3; n < N; n++) {
    A[n] = 1;
    for(int k = 2; k < n; k++) {
      pure[n][k] = 0;
      for(int i = 1; i < k; i++) {
	pure[n][k] += pure[k][i] * binom[n-k-1][k-i-1];
	pure[n][k] %= MOD;
      }
      A[n] += pure[n][k];
      A[n] %= MOD;
    }
  }
  
  int T,n;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> n;

    cout << "Case #" << i << ": " << A[n] << endl;
  }

  return 0;
}
