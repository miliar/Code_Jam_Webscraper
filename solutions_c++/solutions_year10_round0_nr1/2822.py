#include <iostream>
using namespace std;

long pow(long base, long exp)
{
  if(exp == 1){
    return base;
  } else {
    long ret = pow(base, exp / 2);
    if(exp % 2){
      return ret * ret * base;
    } else {
      return ret * ret;
    }
  }
}

int main()
{
  int T, t;
  cin >> T;
  for(t = 1; t <= T; t++){
    long N, K;
    cin >> N >> K;
    long fac = pow(2, N);
    if( (K + 1) % fac == 0){
      cout << "Case #" << t << ": ON" << endl;
    } else {
      cout << "Case #" << t << ": OFF" << endl;
    }
  }
  return 0;
}

