#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
  
  // freopen ( "input.txt", "rb", stdin );
  // freopen ( "output.txt", "w", stdout );
  
  int T;
  cin >> T;
  int N, K;
  vector<int> mybits;
  
  for ( int i = 1; i <= T; i++ ) {
    cout << "Case #" << i << ": ";
    cin >> N >> K;
    if ( (K+1) % (1<<N) == 0 ) cout << "ON" << endl; else cout << "OFF" << endl;
  }
  
  return 0;
}
