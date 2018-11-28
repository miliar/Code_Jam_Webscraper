#include <iostream>
using namespace std;

long long solve(long long L, long long P, int C)
{
  if(C*L >= P)
    return 0;
  
  long long l = L;
  long long p = P;
  while(l < p)
  {
    l *= C;
    p /= C;
  }
  
  return 1 + max(solve(L, l, C), solve(l, P, C));
}

int main()
{
  int T;
  cin >> T;
  
  for(int i = 1; i < T+1; i++)
  {
    long long L, P, C;
    cin >> L >> P >> C;
    cout << "Case #" << i << ": " << solve(L, P, C) << endl;
  }
  return 0;
}
