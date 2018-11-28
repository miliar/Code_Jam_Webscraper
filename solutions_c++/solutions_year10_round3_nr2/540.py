#include <iostream>
#include <cstdio>

using namespace std;

int L, P, C;

int calc_low(int low, int time)
{
  int rval = low;

  if(time == 0){
    return low * C;
  }

  return calc_low(calc_low(low, time - 1), time - 1);
}

int solve()
{
  int low, high;

  cin >> L >> P >> C;

  for(int i=0;; i++){
    if(calc_low(L, i) >= P)return i;
  }
}

int main()
{
  int T;

  cin >> T;

  for(int i=0; i<T; i++){
    printf("Case #%d: %d\n", i+1, solve());
  }
}
