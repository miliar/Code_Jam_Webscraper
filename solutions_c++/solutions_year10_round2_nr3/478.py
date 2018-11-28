#include <iostream>
using namespace std;

const int MOD = 100003;
int ans[501];

void init(void)
{
  int cmb[501][501];
  int tmp[501][501];
  cmb[0][0] = 1;
  for( int n = 1 ; n <= 500 ; ++n ) {
    cmb[n][0] = cmb[n][n] = 1;
    for( int k = 1 ; k < n ; ++k ) {
      cmb[n][k] = (cmb[n-1][k] + cmb[n-1][k-1]) % MOD;
    }
  }
  for( int n = 2 ; n <= 500 ; ++n ) {
    tmp[n][1] = tmp[n][2] = 1;
    for( int k = 3 ; k < n ; ++k ) {
      int ret = 0;
      for( int i = k - 1 ; i >= 2 * k - n && i >= 1 ; --i ) {
        ret = (ret + tmp[k][i] * cmb[n-k-1][k-i-1]) % MOD;
      }
      tmp[n][k] = ret;
    }
    tmp[n][n] = 0;
  }

  for( int i = 2 ; i <= 500 ; ++i ) {
    int ret = 0;
    for( int j = 1 ; j < i ; ++j ) {
      ret = (ret + tmp[i][j]) % MOD;
    }
    ans[i] = ret;
  }
}

int main(void)
{
  int T;
  cin >> T;
  init();
  for( int i = 1 ; i <= T ; ++i ) {
    int n;
    cin >> n;
    cerr << "Case #" << i << "\n";
    cout << "Case #" << i << ": " << ans[n] << "\n";
  }
  return 0;
}
