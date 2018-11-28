#include <iostream>
#include <vector>
using namespace std;
typedef long long lint;

lint solve(void)
{
  int R, k, N;
  cin >> R >> k >> N;
  vector<int> g(N);
  for( int i = 0 ; i < N ; ++i ) cin >> g[i];

  lint euro = 0;
  lint gi = 0, gj = 0;
  for( int i = 0 ; i < R ; ++i ) {
    lint ride = 0;
    int j;
    for( j = gi ; j < N ; ++j ) {
      lint r = ride + g[j];
      if( r > k ) {
        break;
      }
      ride = r;
    }
    if( j == N ) {
      for( j = 0 ; j < gi ; ++j ) {
        lint r = ride + g[j];
        if( r > k ) {
          gj = j;
          break;
        }
        ride = r;
      }
    }
    gi = j;
    euro += ride;
  }
  
  return euro;
}
int main(void)
{
  int C;
  cin >> C;
  for( int i = 1 ; i <= C ; ++i ) {
    cout << "Case #" << i << ": " << solve() << "\n";
  }
  return 0;
}
