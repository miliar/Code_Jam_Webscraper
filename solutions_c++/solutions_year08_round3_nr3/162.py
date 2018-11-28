#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

const int MAX_M = 500000;
const long long MOD = 1000000007;

int n, m, X, Y, Z;
long long A[MAX_M];
int x[MAX_M];
long long cnt[MAX_M];

void generate ()
{
  int i;
  for ( i = 0; i < n; i++ )
  {
    x[ i ] = (int)A[ i % m ];
    A[ i % m ] = (X * A[ i % m ] + Y * (long long)(i + 1)) % Z;
  }
}

int main ()
{
  int num;
  cin >> num;
  int i, j, k;
  long long c;
  for ( i = 0; i++ < num; )
  {
    cin >> n >> m >> X >> Y >> Z;
    for ( j = 0; j < m; j++ )
    {
      cin >> c;
      A[j] = c;
    }
    generate();
    memset( cnt, 0, sizeof(cnt) );

    cnt[0] = 1;
    for ( j = 1; j < n; j++ )
    {
      cnt[j] = 1;
      for ( k = 0; k < j; k++ )
        if ( x[k] < x[j] )
          cnt[j] = (cnt[j] + cnt[k]) % MOD;
    }
    long long total = cnt[0];
    for ( j = 1; j < n; )
      total += cnt[j++];

    cout << "Case #" << i << ": " << (total % MOD) << endl;
  }

  return 0;
}
