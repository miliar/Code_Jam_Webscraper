#include <iostream>

using namespace std;

const char *answer[2] = { "OFF", "ON" };

int main ()
{
  int N, T;
  unsigned K;
  cin >> T;
  for ( int i = 0; i++ < T; )
  {
    cin >> N >> K;
    cout << "Case #" << i << ": " << answer[ ((K ^ (K+1)) >> N) & 1 ] << endl;
  }

  return 0;
}
