#include <iostream>
#include <algorithm>
#include <limits>

int read_data()
{
  int N;
  std::cin >> N;
  int mink = std::numeric_limits<int>::max();
  int sum = 0;
  int checksum = 0;
  for ( int i=0; i<N; ++i )
  {
    int C;
    std::cin >> C;
    checksum ^= C;
    sum += C;
    mink = std::min(mink, C);
  }
  if ( checksum != 0 )
    return -1;
  return sum - mink;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t=1; t<=T; ++t )
  {
    int v = read_data();
    std::cout << "Case #" << t << ": ";
    if ( v < 0 )
      std::cout << "NO\n";
    else
      std::cout << v << '\n';
  }
  return 0;
}
