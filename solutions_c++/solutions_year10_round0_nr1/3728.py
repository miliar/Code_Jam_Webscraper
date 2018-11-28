#include <iostream>

using namespace std;

bool ison(long N, long K)
{
  long magic = (1L << N) - 1;
  return (K & magic) == magic;
}

int main()
{
  long T, N, K;
  cin >> T;
  for ( int t=1; t<=T; ++t )
  {
    cin >> N >> K;
    if ( ison(N, K) )
      cout << "Case #" << t << ": ON" << endl;
    else
      cout << "Case #" << t << ": OFF" << endl;
  }
  return 0;
}
