#include <iostream>
using namespace std;

typedef long long lint;

int main(void)
{
  lint t;
  cin >> t;
  for( lint i = 1 ; i <= t ; ++i ) {
    lint n, k;
    cin >> n >> k;
    lint flg = (1LL << n) - 1;
    if( (flg & k) == flg ) {
      cout << "Case #" << i << ": ON\n";
    } else {
      cout << "Case #" << i << ": OFF\n";
    }
  }
  return 0;
}
