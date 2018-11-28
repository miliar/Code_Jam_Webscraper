#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve()
{
  int N, K, B, T;
  cin >> N >> K >> B >> T;
  vector<int> x(N), v(N);
  for( int i = 0 ; i < N ; ++i ) cin >> x[i];
  for( int i = 0 ; i < N ; ++i ) cin >> v[i];

  int nSwap = 0, nOK = 0;
  vector<int>::iterator px, pv, qx, qv;
  reverse(x.begin(), x.end());
  reverse(v.begin(), v.end());
  for( int i = 0 ; i < N && nOK < K ; ++i ) {
    if( x[i] + v[i] * T >= B ) {
      nSwap += i - nOK;
      ++nOK;
    }
  }
  if( nOK < K ) return -1;

  return nSwap;
}

int main(void)
{
  int C;
  cin >> C;
  for( int i = 1 ; i <= C ; ++i ) {
    cerr << "Case #" << i << "\n";
    int r = solve();
    if( r >= 0 ) {
      cout << "Case #" << i << ": " << r << "\n";
    } else {
      cout << "Case #" << i << ": IMPOSSIBLE\n";
    }
  }
  return 0;
}
